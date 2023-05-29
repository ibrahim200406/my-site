from django.shortcuts import redirect, render
from .fomrs import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from home.models import About,Design,Development,Database,Portfolio
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('emails/contactform.html',{
                'name':name,
                'email':email,
                'content':content,
            })

            send_mail('the contact form subject', 'This is the message', 'birinic@gmail.com',['ikinci@gmail.com'],html_message=html)
            return redirect("index")
    else:
        form = ContactForm()   

    about = About.objects.first() 
    design = Design.objects.first()
    development = Development.objects.first()
    database = Database.objects.first()
    portfolios = Portfolio.objects.all()

    return render(request,'index.html',{
        'form':form,
        'about':about,
        'design': design,
        'development': development,
        'database': database,
        'portfolios':portfolios,
    })


