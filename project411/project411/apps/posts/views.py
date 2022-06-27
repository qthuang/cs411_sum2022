import json
import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Course, Post, Reply

# get the course list from front page
class GetCoursesList(View):
    # try to get data from database course
    def get(self, request):
        try:
            courses = Course.objects.all()
        except Exception as e:
            print(e)
            return JsonResponse({'code':400,
                                 'errmsg':'cannot get Course List'})
        # generalize return data
        courseList = []
        for course in courses:
            courseList.append({
                "course_name":course.course_name
            })
        # return
        return JsonResponse({'code':0,
                             'errmsg':'OK',
                             'course_name':courseList})

# get post list under a course
class getPostsList(View):
    def get(self, request, id):
        # try to get data from database Post
        try:
            posts = Post.objects.filter(course=id).order_by('-createtime')
        except Exception as e:
            return JsonResponse({'code':400,
                                 'errmsg':'cannot get Post List'})
        postList = []
        # generalize return data
        for post in posts:
            postList.append({
                "id":post.id,
                "title":post.headline,
                "createtime": post.createtime,
                "course_name": post.course
            })

        # return data
        return JsonResponse({'code':0,
                             'errmsg':'OK',
                             'post':postList})


# create new post
class NewPost(View):

    def post(self, request):
        '''get param and save to database'''

        dict = json.loads(request.body)
        headline = dict.get('headline')
        course_name = dict.get('course_name')
        content = dict.get('content')
        # check params
        if not all([headline, course_name, content]):
            return JsonResponse({'code': 400,
                                 'errmsg': 'lose param'})
        # add data to database Post
        post = Post.objects.create(headline=headline,
                                   content=content,
                                   course = course_name,
                                   createtime= datetime.datetme.now())
        return JsonResponse({'code': 0,
                             'errmsg': 'ok'})


# get detail of a post
class getPostDetail(View):
    def get(self, request, id):
        # try to get post detail data by filter from database Post
        try:
            posts = Post.objects.filter(id=id)
        except Exception as e:
            return JsonResponse({'code':400,
                                 'errmsg':'cannot get Post List'})
        postInfo = []
        # generalize return content
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
        # return
        return JsonResponse({'code':0,
                             'errmsg':'OK',
                             'post':postInfo})


# create new comment
class NewComment(View):

    def post(self, request):
        '''get param and save to database'''

        dict = json.loads(request.body)
        post = dict.get('post_id')
        content = dict.get('content')
        # check params
        if not all([post, content]):
            return JsonResponse({'code': 400,
                                 'errmsg': 'lose param'})
        # save data to database Reply
        comment = Reply.objects.create(post=post,
                                   content=content)
        # return data
        return JsonResponse({'code': 0,
                             'errmsg': 'ok'})


