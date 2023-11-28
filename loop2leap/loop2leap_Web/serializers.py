from rest_framework import serializers
from .models import User, Group, Group_members


class RegisterUser_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'

    



    






