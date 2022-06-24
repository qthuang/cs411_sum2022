from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^courses/$', views.GetCoursesList.as_view()),
    re_path(r'^posts/(?P<id>[1-9]\d*)/course/$', views.getPostsList.as_view()),
    re_path(r'^posts/$', views.NewPost.as_view()),
    re_path(r'^posts/(?P<id>[1-9]\d*)/$', views.getPostDetail.as_view()),
    re_path(r'^comment/$', views.NewComment.as_view()),

]