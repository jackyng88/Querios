from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Question viewset class extending Django's ModelViewSet class. The 
    ModelViewSet gives us CRUD (Create Read Update Delete) functionality.
    """
    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Overriding of perform_create method so that the author field can 
        # be added automatically i.e. author field will be request.user
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    """
    Answer create API view extending the CreateAPIView concrete class.

    1. Allows us to answer a single specific question based on a slug parameter
    passed via endpoint which will allow us to bind request.user as an author
    of a newly created instance.

    2. Will check if request.user has already answered the question. If so, 
    it will raise a Validation Error.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError('You have already answered this question!')

        serializer.save(author=request_user, question=question)


class AnswerListAPIView(generics.ListCreateAPIView):
    # APIView for listing out all the answers for a specific question.
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # overriding of the get_queryset function
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=kwarg_slug).order_by('-created_at')