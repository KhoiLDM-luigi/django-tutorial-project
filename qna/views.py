from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from qna.models import *
from django.views.generic import View

# # Create your views here.


def qna(request):
    questions = Question.objects.all()
    for i in questions:
        print(i)
    return render(request, 'question_list.html', {"questions": list(questions)})


class QnAView(View):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all().order_by('-pub_date').values()
        return render(request, 'question_list.html', {"questions": list(questions)})

    def post(self, request, *args, **kwargs):
        question = request.POST["question"]
        user = request.user
        question = Question(question=question, user=user)
        print(question.getUsername())
        question.save()
        return redirect(self.request.path_info)


class QuestionView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        question = Question.objects.get(pk=id)
        answer = Answer.objects.all().filter(question=question)
        return render(request, 'question.html', {'question': question, 'answers': list(answer)})

    def post(self, request, *args, **kwargs):
        id = kwargs["id"]
        question = Question.objects.get(pk=id)
        user = request.user
        a = request.POST["answer"]
        answer = Answer(question=question, answer=a, user=user)
        answer.save()
        return redirect(self.request.path_info)


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        question = Question.objects.get(pk=id)
        return JsonResponse(dict(question))
