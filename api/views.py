# -*- coding: utf-8 -*-
import json
from django.db import transaction
from django.db.transaction import TransactionManagementError

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
#from billing.models import TaskExpense
from .serializers import UserSerializer, TaskSerializer
from project_4.users.models import User
from task.models import Task


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type=User.EXECUTOR)
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type=User.CUSTOMER)
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


