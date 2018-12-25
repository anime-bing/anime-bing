from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    STATUS_CHOICE = {
        ('draft','Draft'),('published','Published')
    }
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length=150)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    description = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to='images',null=True,blank=True,default='default_post.jpg')
    status = models.CharField(max_length=20,choices = STATUS_CHOICE ,default = 'draft')
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',args = [self.id , self.slug])

@receiver(pre_save,sender=Post)
def pre_save_slug(sender,**kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_comments')
    content = models.TextField(max_length=200)
    reply = models.ForeignKey('Comment',on_delete=models.CASCADE,null=True,related_name="replies")
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}-{}'.format(self.post.title,str(self.user.username))
