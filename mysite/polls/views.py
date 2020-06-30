from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Question
from .models import Choice, Question
from django.urls import reverse
from django.views import generic

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list':latest_question_list,
#     }
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'polls/index.html',context)

## Generic
class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]




# # def details(request, question_id):
# #     return HttpResponse("You are looking at the question %s." % question_id)
# def details (request, question_id):
#     # try:
#     #     question:Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, "polls/details.html",{'question':question})

#Generic
class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'






# # def results(request, question_id):
# #     return HttpResponse("You are looking at the results of question %s." % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html',{'question':question})


#Generic 
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'








# def vote(request, question_id):
#     return HttpResponse("You are voting on question %s." % question_id)

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         print("in try")
#         selected_choice=question.choice_set.get(pk=request.POST['choice'])
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print("int try")
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        print("in except")
        return render(request, 'polls/details.html',{
            'question':question,
            'error_message':"You didnt select a choice"
        })
    else:
        print("in else")
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
