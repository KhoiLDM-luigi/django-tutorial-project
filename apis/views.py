from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework import status
from qna.models import Question, Answer
from apis.serializers import QuestionSerializer, QuestionSerializerWithAnswers, AnswerSerializer, AnswerSerializerWithQuestion
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import authentication, permissions
# Create your views here.


class QuestionsView(GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    authentication_classes = [
        authentication.TokenAuthentication
    ]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            instance = get_object_or_404(Question, pk=id)
            data = QuestionSerializerWithAnswers(instance).data
            return Response(data)

        instances = Question.objects.all()
        data = QuestionSerializerWithAnswers(instances, many=True).data
        return Response(data)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            data = AnswerSerializer(data=request.data, context={
                'user_id': request.data['user_id'], 'question_id': id})
            print(data)
            if (data.is_valid()):
                data.save()
                return Response(data.data)
            print(data.error_messages)
            return HttpResponseBadRequest()

        data = QuestionSerializer(data=request.data, context={
                                  'user_id': request.data['user_id']})
        if data.is_valid():
            data.save()
            return Response(data.data)

        return HttpResponseBadRequest()

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = get_object_or_404(Question, pk=id)
        data = QuestionSerializer(instance, data=request.data)
        if (data.is_valid()):
            data.save()
            return Response(data.data)
        return HttpResponseBadRequest()

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = get_object_or_404(Question, pk=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerView(GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            instance = get_object_or_404(Answer, pk=id)
            data = AnswerSerializerWithQuestion(instance).data
            return Response(data)

        instances = Answer.objects.all()
        data = AnswerSerializerWithQuestion(instances, many=True).data
        return Response(data)

    def post(self, request, *args, **kwargs):
        data = AnswerSerializer(data=request.data, context={
            'user_id': request.data['user_id'], 'question_id': request.data['question_id']})
        if (data.is_valid()):
            data.save()
            return Response(data.data)
        return HttpResponseBadRequest()
