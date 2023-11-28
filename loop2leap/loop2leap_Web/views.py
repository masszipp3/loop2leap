from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Group, Group_members
from .serializers import RegisterUser_Serializer
from django.contrib.auth.hashers import make_password

# Create your views here.
def success_response(message):
    dictionary={}
    dictionary['status_code']=200
    dictionary['message']=message
    data = {"results": dictionary}
    return data

def failed_response(message,reason):
    dictionary={}
    dictionary['status_code']=401
    dictionary['message']=message
    dictionary['reason']=reason
    data = {"results": dictionary}
    return data



class RegistrationView(APIView):

    def post(self, request, *args, **kwargs):
        is_group = request.data.get('is_group')
        if not is_group:
            data = request.data
            data['password'] = make_password('admin@123') 
            serializer = RegisterUser_Serializer(data=request.data)
        else :
                users_list = request.data.get('users',[])
                if len(users_list) >1:
                    users_list = [{**user, 'is_group': True,'password': make_password('admin@123')} for user in users_list]
                    serializer = RegisterUser_Serializer(data=users_list, many=True)
                else:
                    return Response(failed_response('Registration Failed','user data is empty'))
        if serializer.is_valid():
            serializer.save()
            users= serializer.data
            if is_group :
                group = Group.objects.create()
                for user in users:
                    Group_members.objects.create(user_id=int(user["id"]),group_id=group.id)
            return Response(success_response('Successfully Registerd'))
        else:
            return Response(failed_response('Registration Failed',serializer.errors))
               