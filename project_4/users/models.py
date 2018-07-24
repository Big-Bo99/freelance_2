from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models



class User(AbstractUser):

    CUSTOMER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (CUSTOMER, _(u"Заказчик")),
        (EXECUTOR, _(u"Исполнитель")),
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=EXECUTOR)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
