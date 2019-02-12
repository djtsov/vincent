from django.db import models
from django.utils import timezone
from . choices import PriorityEnum
from django.contrib.auth import get_user_model


class TODOModel(models.Model):
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300,
                                   blank=True, null=True)
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=10,
                                choices=PriorityEnum.choices(),
                                default=PriorityEnum.NORM.name)

    def __str__(self):
        return "user: {}, task: {}".format(self.owner.username, self.title)
