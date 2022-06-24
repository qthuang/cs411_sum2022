from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
import json
import re
from django.http import JsonResponse
from django.views import View
import json
from django.contrib.auth import login, authenticate, logout

from .models import ProjectUser


class RegisterView(View):

    def post(self, request):
        '''get param and save to database'''

        # 1.receive params
        dict = json.loads(request.body)
        password = dict.get('password')
        email = dict.get('email')

        # 2. check all params
        if not all([password, email]):
            return JsonResponse({'code': 400,
                                 'errmsg': 'lose param'})
        print(password)
        print(email)
        user = User.objects.create(password=password,
                                   email=email)
        return JsonResponse({'code': 0,
                             'errmsg': 'ok'})


class LoginView(View):
    def post(self, request):

        dict = json.loads(request.body)
        email = dict.get('email')
        password = dict.get('password')

        if not all([email, password]):
            return JsonResponse({'code': 400,
                                 'errmsg': 'lose param'})

        user = authenticate(email=email,
                            password=password)

        if user is None:
            return JsonResponse({'code': 400,
                                 'errmsg': '用户名或者密码错误'})

        login(request, user)

        request.session.set_expiry(None)

        return JsonResponse({'code': 0,
                             'errmsg': 'ok'})
#
#
class LogoutView(View):

    def delete(self, request):

        logout(request)

        response = JsonResponse({'code':0,
                                 'errmsg':'ok'})

        response.delete_cookie('username')

        return response