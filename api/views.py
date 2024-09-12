from django.shortcuts import render
from api.serializers import PhoneSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from contacts.models import phone
from rest_framework.status import HTTP_201_CREATED,HTTP_200_OK,HTTP_400_BAD_REQUEST

# Create your views here.
