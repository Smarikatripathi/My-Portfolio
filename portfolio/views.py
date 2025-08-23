from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    PersonalInfo, Project, Skill, Education, 
    Certification, Testimonial, ContactMessage
)
from .forms import ContactForm

def home(request):
    """Home page view with all portfolio data"""
    personal_info = PersonalInfo.objects.first()
    context = {
        'personal_info': personal_info,
        'projects': Project.objects.filter(featured=True)[:6],
        'skills': Skill.objects.all(),
        'education': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'testimonials': Testimonial.objects.filter(featured=True)[:3],
        'contact_form': ContactForm(),
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About page view"""
    personal_info = PersonalInfo.objects.first()
    context = {
        'personal_info': personal_info,
        'skills': Skill.objects.all(),
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """Projects page view"""
    projects_list = Project.objects.all()
    context = {
        'projects': projects_list,
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f"New Contact Message: {contact_message.subject}",
                    message=f"""
                    Name: {contact_message.name}
                    Email: {contact_message.email}
                    Subject: {contact_message.subject}
                    Message: {contact_message.message}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                
                # Send confirmation email to user
                send_mail(
                    subject="Thank you for your message",
                    message=f"""
                    Dear {contact_message.name},
                    
                    Thank you for reaching out to me. I have received your message and will get back to you as soon as possible.
                    
                    Best regards,
                    {PersonalInfo.objects.first().name if PersonalInfo.objects.exists() else 'Portfolio Owner'}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[contact_message.email],
                    fail_silently=True,
                )
                
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again.')
            
            return redirect('portfolio:contact')
    else:
        form = ContactForm()
    
    context = {
        'contact_form': form,
    }
    return render(request, 'portfolio/contact.html', context)

def download_resume(request):
    """Download resume view"""
    personal_info = PersonalInfo.objects.first()
    if personal_info and personal_info.resume:
        return redirect(personal_info.resume.url)
    else:
        messages.error(request, 'Resume not available.')
        return redirect('portfolio:home') 