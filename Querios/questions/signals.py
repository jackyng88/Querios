from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from questions.models import Question



@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    """
    Function that takes randomly generated string from the utils.py file from
    the core folder. This slug is added to the question to guarantee a 
    unique slug for use in question model for that particular instance.
    """
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string