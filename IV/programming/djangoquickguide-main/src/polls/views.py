from django.shortcuts import HttpResponse, render, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# первый тестовый view
# def index(request):
#     latest_questions_list = Question.objects.order_by("-id")[:5]
#     # output = ", ".join([q.question_text for q in latest_questions_list])
#     # return HttpResponse(output)
#     # template = loader.get_template("index.html")
#     context = {
#         "latest_questions_list": latest_questions_list,
#     }
#     return render(request, "index.html", context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     # return HttpResponse("It is question %s." % question_id)
#     return render(request, "detail.html", {"question": question})

# def result(request, question_id):
#     # response = "It is result of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "results.html", {"question": question})

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_questions_list"

    def get_queryset(self):
        """Return last five questions"""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'

def vote(request, question_id):
    # return HttpResponse(f"It is vote on question {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You shuld select anything.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))