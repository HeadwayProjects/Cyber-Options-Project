from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about01.html")

def contact(request):
    if request.method == 'POST':
        form_data = request.POST
        message = form_data['message']
        name = form_data['name']
        email = form_data['email']
        subject = form_data['subject']
        html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message':message,
            })

        send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['codewithtestein@gmail.com'], html_message=html)
        return redirect('index')
    else: 
        return redirect('contact')
    return render(request, "contact01.html",  )