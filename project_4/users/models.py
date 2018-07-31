from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, F
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
import math
from decimal import *




class User(AbstractUser):

    CUSTOMER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (CUSTOMER, _(u"Заказчик")),
        (EXECUTOR, _(u"Исполнитель")),
    )

    name = CharField(_("Name of User"), blank=True, max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=CUSTOMER)
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    # def update_balance(self, reason, money, **kwargs):
    #     from billing.models import MoneyLog
    #     ml_filter = {}
    #     task = kwargs.get('task', None)
    #     ml_filter['reason'] = reason
    #     ml_filter['user'] = self
    #     #ml_filter['debit'] = math.fabs(money) if money < 0 else 0
    #     #ml_filter['credit'] = math.fabs(money) if money > 0 else 0
    #     ml_filter['money'] = money
    #     ml_filter['task'] = task
    #
    #     #current_balance = User.objects.select_for_update().get(pk=self.pk).balance
    #     #User.balance = current_balance + Decimal(money)
    #
    #     User.objects.select_for_update().filter(pk=self.pk).update(balance=F('balance') + Decimal(money))
    #
    #     try:
    #         ml = MoneyLog.objects.get(**ml_filter)
    #     except MoneyLog.DoesNotExist:
    #         try:
    #             ml = MoneyLog.objects.create(**ml_filter)
    #         except IntegrityError:
    #             ml = MoneyLog.objects.get(**ml_filter)

    def update_balance(self, creator_id, money, **kwargs):

        User.objects.select_for_update().filter(pk=self.pk).update(balance=F('balance') + Decimal(money))
        User.objects.select_for_update().filter(pk=creator_id).update(balance=F('balance') - Decimal(money))
