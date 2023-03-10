from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    imagem = models.ImageField(upload_to='profile_images', default='blank-profile-picutre.jpg')
    seguidores = models.IntegerField(default=0)
    post = models.ForeignKey('Post', models.DO_NOTHING, null=True, blank=True, default = None)

    class Meta:
        db_table = 'profile'


class Comments(models.Model):
    comment_date = models.DateField()
    comment_text = models.CharField(max_length=200)
    post = models.ForeignKey('Post', models.DO_NOTHING)
#    profile = models.ForeignKey('Profile', models.DO_NOTHING)

    class Meta:
        db_table = 'comments'

class Post(models.Model):
    post_date = models.DateField()
    likes = models.IntegerField(default=0)
    foto = models.CharField(max_length=50)
#   profilio = models.ForeignKey('Profile', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Post'


class Referencia(models.Model):
    post_id = models.ForeignKey('Post', models.DO_NOTHING)
    ref_descricao = models.CharField(max_length=25)

    class Meta:
        db_table = 'referencia'
