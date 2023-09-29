from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s by %s" % (self.question, self.getUsername())
        # return "q: {question}".format(question=self.question)

    def getUsername(self):
        if self.user.first_name or self.user.last_name:
            return " %s %s" % (self.user.first_name, self.user.last_name)
        return self.user.username


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE)
    answer = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    votes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "\"%s\" for question:\"%s\"" % (self.answer, self.question.question)
        # return "a: {answer} for question: {question}".format(answer=self.answer, question=self.question.pk)

    def getQuestion(self):
        return self.question.question

    def getUsername(self):
        if self.user.first_name or self.user.last_name:
            return " %s %s" % (self.user.first_name, self.user.last_name)
        return self.user.username
