from django.http import *
from django.shortcuts import *
from .models import *
from .urls import *
from django.views import generic

def index(request):
    questions = Question.objects.all()
    context = {
        "questions":questions
    }
    return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.all()

def detail(request,question_id):
       try:
           question=Question.objects.get(id=question_id)
       except Question.DoesNotExist:
          msg="Question not found"
          return render(request,'polls/details.html',{'error':msg})
       return render(request,'polls/details.html',{'question':question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detailS.html'


def vote(request,question_id):
       selected_choice = request.POST['vote']
       question = Question.objects.get(id=question_id) #que id saving in variable
       choice =question.choice_set.get(id=selected_choice)
       choice.votes = choice.votes + 1
       choice.save()
       return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

def result(request,question_id):
       question = get_object_or_404(Question, pk=question_id)
       return render(request, 'polls/results.html', {'question':question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
