from django.db import models

# 导入内置的User模型
from django.contrib.auth.models import User

# timezone 用于处理时间相关的事务
from django.utils import timezone


# 博客文章数据模型
class ArticlePost(models.Model):

    # 文章作者。参数。 on_delete用于指定数据删除的方式，2.0以后这个参数必须添加
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章')

    # 文章标题。 model.CharField 为字符串字段，用于保存较短的字符串，比如标题.max_length指定字符最大长度
    title = models.CharField(max_length=100, verbose_name='标题')

    # 文章正文，保存大量文本使用TextField
    body = models.TextField(verbose_name='正文')

    # 文章的创建时间。参数default=timezone.now指定其在创建数据时候将默认写入当前的时间
    created_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    # 文章的更新时间。参数 auto_now=True，指定每次数据跟新是自动写入当前的时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 函数 __str__定义当调用对象的str()方法的时候的返回值内容，这里后台管理系统的可以看到标题，不写这个看到的会是字段
    def __str__(self):
        return self.title

    # 内部class Meta用于给model定义元数据
    class Meta:

        # ordering 指定模型返回的数据的排列顺序
        # '-created_time'表明数据已改以倒序排列
        ordering = ('-created_time',)  # 注意这里是元组（Tuple）
        verbose_name = "文章"
        verbose_name_plural = '文章'





