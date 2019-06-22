from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # Answer details API view that allows us to Retrieve, Update and Delete.
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class AnswerLikeAPIView(APIView):
    """
    View for leaving or removing a like on an answer utilizing only two
    HTTP methods - post and delete.
    """
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
