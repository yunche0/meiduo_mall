from http.client import responses

from django.shortcuts import render
from django.views import View
from apps.users.models import User
from django.http import JsonResponse
import re
class UsernamecountView(View):
    def get(self, request,username):
        '''if not re .match('[a-zA-Z0-9_-]{5,20}',username):
            return JsonResponse({'code':200,'errmsg':'用户名不满足需求'})'''
        count=User.objects.filter(username=username).count()
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})

import json
class RegisterView(View):

    def post(self,request):
        body_bytes=request.body
        body_str=body_bytes.decode()
        body_dict=json.loads(body_str)

        username = str(body_dict.get('username', ''))
        password = str(body_dict.get('password', ''))
        password2 = str(body_dict.get('password2', ''))
        mobile = str(body_dict.get('mobile', ''))
        allow = body_dict.get('allow')

        if not all([username,password,password2,mobile,allow]):
            return JsonResponse({'code':400,'errmsg':'参数不全'})

        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return JsonResponse({'code':400,'errmsg':'用户名不满足规则'})

        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,20}$', password):
            return JsonResponse({
                'code': 400,
                'errmsg': '密码必须为8-20位，且同时包含字母和数字'
            })

        if password != password2:
            return JsonResponse({'code': 400, 'errmsg': '两次输入的密码不一致'})

        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return JsonResponse({'code': 400, 'errmsg': '手机号格式不正确'})


        if User.objects.filter(mobile=mobile).exists():
            return JsonResponse({'code': 400, 'errmsg': '该手机号已被注册'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'code': 400, 'errmsg': '用户名已存在'})
        #User.objects.create(username=username,password=password,mobile=mobile)
        user=User.objects.create_user(username=username,password=password,mobile=mobile)

        from django.contrib.auth import login
        login(request,user)
        return JsonResponse({'code':0,'errmsg':'ok'})

class LoginView(View):

    def post(self,request):
        data=json.loads(request.body.decode())
        username=data.get('username')
        password=data.get('password')
        remember=data.get('remember')

        if not all([username,password]):
            return JsonResponse({'code':400,'errmsg':'参数不全'})

        if re.match('1[3-9]\d{9}',username):
            User.USERNAME_FIELD='mobile'
        else:
            User.USERNAME_FIELD='username'
        from django.contrib.auth import authenticate

        user=authenticate(username=username,password=password)
        if user is None:
            return JsonResponse({'code':400,'errmsg':'账号或密码错误'})

        from django.contrib.auth import login
        login(request,user)

        if remember:
            request.session.set_expiry(None)

        else:
            request.session.set_expiry(0)

        response=JsonResponse({'code':0,'errmsg':'ok'})

        response.set_cookie('username',username)

        return response

from django.contrib.auth import logout

class LogoutView(View):

    def delete(self,request):
        logout(request)
        response= JsonResponse({'code':0,'errmsg':'ok'})
        response.delete_cookie('username')
        return response



from utils.views import LoginRequiredJSONMixin
class CenterView(LoginRequiredJSONMixin,View):

    def get(self,request):

        return JsonResponse({'code':0,'errmsg':'ok'})