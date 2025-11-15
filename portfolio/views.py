from django.shortcuts import render, get_object_or_404, redirect

from .models import Project, Skill, Experience, BlogPost
from .forms import ContactForm
from django.contrib import messages

from django.core.mail import send_mail
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    projects = Project.objects.all()[:6]
    posts = BlogPost.objects.all()[:3]
    skills = Skill.objects.all()[:6]
    context = {'projects': projects, 'posts': posts, 'skills': skills}
    return render(request, 'portfolio/home.html', context)

def about(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/about.html', {'skills': skills, 'experiences': experiences})

def projects_list(request):
    query = request.GET.get('q')

    project_list = Project.objects.all()
    if query:
        project_list = project_list.filter(title__icontains=query)
    paginator = Paginator(project_list, 5)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    return render(request, 'portfolio/projects_list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def blog_list(request):
    query = request.GET.get('q')
    posts = BlogPost.objects.all()
    if query:
        posts = posts.filter(title__icontains=query)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'portfolio/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'post': post})

def resume(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/resume.html', {'skills': skills, 'experiences': experiences})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Portfolio Contact: {form.cleaned_data['name']}",
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['your-email@example.com'],
            )
            form.save()
            messages.success(request, 'Thanks — your message has been received. I will get back to you soon.')
            return redirect('portfolio:contact')
            # return render(request, 'portfolio/contact.html', {'form': ContactForm(), 'success': True}) 
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
