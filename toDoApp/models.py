# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class toDo(models.Model):
    text = models.CharField(max_length=120)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

