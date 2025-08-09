"""
Definition of views.
"""

from datetime import datetime
#from sys import exception
# from telnetlib import STATUS
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.shortcuts import render
from .service.openai_service import get_openai_response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, HttpResponse
# from .models import UserRequestLog
# from django.utils.timezone import now
import requests
from django.conf import settings

from app.models import Nonprofit
from app.models import Event
from app.models import Post
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Our Story',
            'message':'Our application description page.',
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    posts = Post.objects.all()
    return render(
        request,
        'app/blog.html',
        {
            'title':'Fresh updates from the Homeless Stop Team',
            'message':'Our application description page.',
            'year':datetime.now().year,
            'posts': posts,
        }
    )

def bp1(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bp1.html',
        {
            'title':'Fresh updates from the Homeless Stop Team',
            'message':'Our application description page.',
            'year':datetime.now().year,
        }
    )
def nonprofitlist(request):
    """Renders the nonprofit list page."""
    assert isinstance(request, HttpRequest)
    nonprofits = Nonprofit.objects.all()
    return render(
        request,
        'app/nonprofitlist.html',
        {
            'title':'Nonprofit List',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'nonprofits':nonprofits,
        }
    )

def nonprofitdetails(request, id):
    """Renders the nonprofit details page."""
    assert isinstance(request, HttpRequest)
    # nonprofits = Nonprofit.objects.all()
    object = get_object_or_404(Nonprofit,id = id)
    return render(
        request,
        'app/nonprofitdetails.html',
        {
            'title':'Nonprofit Details (CHANGE TO NONPROFIT NAME)',
            'message':'Your application description page. (CHANGE TO NONPROFIT CATEGORY',
            'year':datetime.now().year,
            'object': object 
        }
    )

def infonotprovided(request):
    """Renders the info not found page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/infonotprovided.html',
        {
            'title':"Info Not Provided ",
            'message':'',
            'year':datetime.now().year,
        }
    )

@csrf_exempt 
def openai_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('user_input', '')
            recaptcha_response = data.get('g-recaptcha-response', '')
            if recaptcha_response != '':
                # captcha_response = request.POST['g-recaptcha-response']
                captcha_response = recaptcha_response
                payload = {
                    'secret': settings.RECAPTCHA_SECRET_KEY,
                    'response': captcha_response,
                }
                response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
                result = response.json()

                if result.get('success'):
                    # Process chatbot request
                    request.META['HTTP_RATE_LIMIT_EXCEEDED'] = False
                    
                    # return JsonResponse({"status":"success","message":response_text},status_code=200)
                # else:
                #     return render(request, 'app/captcha.html')  # Create this template
                    # return JsonResponse(data='CAPTCHA verification failed.', safe=False)

            # If rate limit is exceeded, render CAPTCHA
            if request.META.get('HTTP_RATE_LIMIT_EXCEEDED'):
                return render(request, 'app/captcha.html', { 'user_input': user_input })  # Create this template
            
            # data = json.loads(request.body)
            # user_input = data.get('user_input', '')
            response_text = 'Your input is empty!'
            if user_input != '':
                response_text = get_openai_response(user_input)
            return JsonResponse(data=response_text, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse(data=str(e), safe=False)
            # return JsonResponse({"status":"error","message":str(e)},status_code=500)
     #  return render(request, 'openai_form.html')
    return JsonResponse(data="Invalid request", safe=False)
    # return JsonResponse({"status":"error","message":"Invalid request"},status_code=400)

def eventslist(request):
    """Renders the eventslist page."""
    assert isinstance(request, HttpRequest)
    events = Event.objects.all()
    return render(
        request,
        'app/eventslist.html',
        {
            'title':'Nonprofit Events',
            'message':'Ongoing nonprofit events you can contribute to.',
            'year':datetime.now().year,
            'events':events,
        }
    )

def eventdetails(request, id):
    """Renders the event details page."""
    assert isinstance(request, HttpRequest)
    # nonprofits = Nonprofit.objects.all()
    object = get_object_or_404(Event,id = id)
    return render(
        request,
        'app/eventdetails.html',
        {
            'title':'Event Details (CHANGE TO EVENT NAME)',
            'message':'Your application description page. (CHANGE TO NONPROFIT CATEGORY',
            'year':datetime.now().year,
            'object': object 
        }
    )


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')



#def locate(request):
