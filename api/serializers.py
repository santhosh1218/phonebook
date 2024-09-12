from contacts.models import phone
from rest_framework.serializers import Serializer

class PhoneSerializer(Serializer):
    class Meta:
        model=phone
        fields='__all__'
