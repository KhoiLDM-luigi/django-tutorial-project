from rest_framework import serializers
from qna.models import Question, Answer, User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'user_id',
            'pub_date',
        ]

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        user = User.objects.get(pk=user_id)
        question = Question.objects.create(**validated_data, user_id=user_id)
        return question


class AnswerSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer(many=False)
    question_id = serializers.PrimaryKeyRelatedField(
        many=False, read_only=True)

    class Meta:
        model = Answer
        fields = [
            'id',
            'question_id',
            'answer',
            'user_id',
            'pub_date',
        ]

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        question_id = self.context.get('question_id')
        answer = Answer.objects.create(
            **validated_data, user_id=user_id, question_id=question_id)
        return answer


class AnswerSerializerWithQuestion(serializers.ModelSerializer):
    question = QuestionSerializer(many=False, read_only=True)

    class Meta:
        model = Answer
        fields = [
            'id',
            'question',
            'answer',
            'user_id',
            'pub_date',
        ]


class QuestionSerializerWithAnswers(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'user_id',
            'pub_date',
            'answers'
        ]
