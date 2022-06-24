import json
import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Course, Post, Reply


class GetCoursesList(View):

    def get(self, request):
        try:
            courses = Course.objects.all()
        except Exception as e:
            print(e)
            return JsonResponse({'code':400,
                                 'errmsg':'cannot get Course List'})
        courseList = []
        for course in courses:
            courseList.append({
                "course_name":course.course_name
            })

        return JsonResponse({'code':0,
                             'errmsg':'OK',
                             'course_name':courseList})


class getPostsList(View):
    def get(self, request, id):
        try:
            posts = Post.objects.filter(course=id).order_by('-createtime')
        except Exception as e:
            return JsonResponse({'code':400,
                                 'errmsg':'cannot get Post List'})
        postList = []
        for post in posts:
            postList.append({
                "id":post.id,
                "title":post.headline,
                "createtime": post.createtime,
                "course_name": post.course
            })

        return JsonResponse({'code':0,
                             'errmsg':'OK',
                             'post':postList})

class NewPost(View):

    def post(self, request):
        '''get param and save to database'''

        dict = json.loads(request.body)
        headline = dict.get('headline')
        course_name = dict.get('course_name')
        content = dict.get('content')

        if not all([headline, course_name, content]):
            return JsonResponse({'code': 400,
                                 'errmsg': 'lose param'})

        post = Post.objects.create(headline=headline,
                                   content=content,
                                   course = course_name,
                                   createtime= datetime.datetme.now())
        return JsonResponse({'code': 0,
                             'errmsg': 'ok'})



class getPostDetail(View):
    def get(self, request, id):
        try:
            posts = Post.objects.filter(id=id)
        except Exception as e:
            return JsonResponse({'code':400,
                                 'errmsg':'cannot get Post List'})
        postInfo = []
        for post in posts:
            comment_list = []
            comment_obj_list = Reply.objects.filter(post_id = id)
            for com in comment_obj_list:
                comment_list.append({"id":com.id,
                                     "content":com.content,
                                     "post":post.id})
            postInfo.append({
                "id":post.id,
                "title":post.headline,
                "createtime": post.createtime,
                "course_name": post.course,
                "content":post.content,
                "comment": comment_list
            })

        return JsonResponse({'code':0,
                             'errmsg':'OK',
                             'post':postInfo})

class NewComment(View):

    def post(self, request):
        '''get param and save to database'''

        dict = json.loads(request.body)
        post = dict.get('post_id')
        content = dict.get('content')

        if not all([post, content]):
            return JsonResponse({'code': 400,
                                 'errmsg': 'lose param'})

        comment = Reply.objects.create(post=post,
                                   content=content)
        return JsonResponse({'code': 0,
                             'errmsg': 'ok'})


