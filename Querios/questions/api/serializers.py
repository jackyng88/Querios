from rest_framework import serializers

from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    """
    class for answer serializer.
    note - SerializerMethod field will call a method of the field it is being
    used for. For example created_at -> get_created_at() 
    """
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ['question', 'voters', 'updated_at']

    def get_created_at(self, instance):
        """
        strftime() returns a string representation of a date. 
        %B - Full month name i.e. January, February
        %d - Zero padded decimal for day i.e. 01, 02
        %Y - Year with century decimal number i.e. 2019 
        """
        return instance.created_at.strftime('%B %d, %Y')

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get('request')
        return instance.voters.filter(pk=request.user.pk).exists()


class QuestionSerializer(serializers.ModelSerializer):
    # Class for question serializer
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()