from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone

from .models import Question,Choice
from .forms import NewPollForm

# Create your views here.

#Here we create views the hard way, above this commented lines we use generic views
"""def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context, content_type='text/html')"""

#def detail(request, question_id):
"""try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists!")
    return render(request, "polls/detail.html", {'question': question})"""
# A Shortcut
"""question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', content_type='text/html', context={'question': question})"""

"""def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})"""


"""class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']"""

def index(request):
    if request.method == 'GET':
       print('GET REQUEST')
       latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:100]
       context = {
           'latest_question_list': latest_question_list,
       }
       return render(request, 'polls/index.html', context)
    elif request.method == 'POST':
       print('POST REQUEST')
       poll_form = NewPollForm(request.POST)
       if poll_form.is_valid():
           question_text = poll_form.cleaned_data['question_input']
           choice_1 = poll_form.cleaned_data['choice_1']
           choice_2 = poll_form.cleaned_data['choice_2']
           #choice_3 = poll_form.cleaned_data['choice_3']
           print("""DATA RECEIVED:
                    question: %s
                    choice 1: %s
                    choice 2: %s
                    choice 3: """ %(question_text, choice_1, choice_2))

           # Insert vslues received from the form into the database
           question = Question(question_text= question_text, pub_date= timezone.now())
           question.save()

           foreign_key = question.id
           print('question id:', foreign_key)
           choices = [choice_1, choice_2]
           for choice in choices:
               if choice == '':
                   continue
               else:
                   c = Choice(choice_text= choice, question_id=foreign_key)
                   c.question_id = foreign_key
                   c.save()



           latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:100]
           context = {
               'latest_question_list': latest_question_list,
               'saved_success': True
           }
           #return render(request, 'polls/index.html', context)
           return render(request, 'polls/index.html', context)
    else:
       print('UNKNOWN')


def get_queryset(self):
    # Return the last five published questions.
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:100]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte= timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Return an HttpResponseRedirect after successfully dealing with POST data
        # This prevents data from beign posted twice if a user hits the Back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.pk,)))


def PollFormTemplate(request):
    poll_form = NewPollForm()
    context = {'poll_form': poll_form}
    return render(request, 'polls/newPoll.html', context=context ,content_type='text/html')

def SavePoll(request):
    if request.method == 'POST':
        poll_form = NewPollForm(request.POST)
        if poll_form.is_valid():
            question_text = poll_form.cleaned_data['question_input']
            print('The question received is: ' + question_text)
            print('The choices: ')
            choice_1 = poll_form.cleaned_data['choice_1']
            choice_2 = poll_form.cleaned_data['choice_2']

            print(choice_1 + '\n' + choice_2)
            latest_question_list = Question.objects.order_by('-pub_date')[:100]




