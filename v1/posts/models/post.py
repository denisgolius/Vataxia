from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Post(CreatedModified):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.body
