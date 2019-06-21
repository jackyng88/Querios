from django.db import models
from django.conf import settings


class Question(models.Model):
    # class for Questions

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=512)
    slug = models.SlugField(max_length=255, unique=True)
    # The author of a question is going to be the user who created it. 
    # Considering that we are using a custom user model, it's good practice to
    # reference the AUTH_USER_MODEL in the main settings.py file.
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='questions')

    def __str__(self):
        return self.content


class Answer(models.Model):
    # class for Answers

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    # field for likes
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='votes') 

    def __str__(self):
        return self.author.username