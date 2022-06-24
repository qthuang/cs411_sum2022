from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.CharField(max_length=30, unique=True, verbose_name='email_address', null=True)
    password = models.CharField(max_length=30, unique=True, verbose_name='password', null=True)
    class Meta:
        db_table = "tb_user"
    def __str__(self):
        return self.username


class ProjectUser(models.Model):
    email = models.CharField(max_length=30, unique=True, verbose_name='email_address', null=True)
    password = models.CharField(max_length=30, unique=True, verbose_name='password', null=True)


    class Meta:
        db_table = "tb_ProjectUser"
    def __str__(self):
        return self.email



from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=20, null=True, default=None, verbose_name="course_name")
    class Meta:
        db_table = "tb_label"

    def __str__(self):
        return self.course_name


class Post(models.Model):
    headline = models.CharField(max_length=100, null=True, default=None, verbose_name="title")
    content = models.CharField(max_length=1000, null=True, default=None, verbose_name="content")
    labels = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='posts')
    createtime = models.DateTimeField(auto_now_add=True, null=True, verbose_name="datetime")

    class Meta:
        db_table = "tb_question"
        ordering = ['-createtime']

    def __str__(self):
        return self.headline


class Reply(models.Model):
    content = models.CharField(max_length=1000, null=True, default=None, verbose_name="content")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies", default=None,
                                verbose_name="postID")
    class Meta:
        db_table = "qa_reply"

    def __str__(self):
        return self.content
