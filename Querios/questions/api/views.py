from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import QuestionSerializer
from questions.models import Question


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
