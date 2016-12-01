from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Question
import datetime

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def gettimetest(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def cpptest(request):
    res=HttpResponse("Not for web!")
    res.__setitem__("ans","1")
    return HttpResponse(res)
