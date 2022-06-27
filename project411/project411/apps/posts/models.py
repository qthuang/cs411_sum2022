from django.db import models

# database course
class Course(models.Model):
    course_name = models.CharField(max_length=20, null=True, default=None, verbose_name="course_name")
    class Meta:
        db_table = "tb_label"

    def __str__(self):
        return self.course_name

# database Post
class Post(models.Model):
    headline = models.CharField(max_length=100, null=True, default=None, verbose_name="title")
    content = models.CharField(max_length=1000, null=True, default=None, verbose_name="content")
    course = models.ForeignKey(Course, related_name='posts')
    createtime = models.DateTimeField(auto_now_add=True, null=True, verbose_name="datetime")

    class Meta:
        db_table = "tb_question"
        ordering = ['-createtime']

    def __str__(self):
        return self.headline

# database Reply
class Reply(models.Model):
    content = models.CharField(max_length=1000, null=True, default=None, verbose_name="content")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies", default=None,
                                verbose_name="postID")
    class Meta:
        db_table = "qa_reply"

    def __str__(self):
        return self.content
