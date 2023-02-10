from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



# Create your models here.



class Comments(models.Model):
    comment_date = models.DateField()
    comment_text = models.CharField(max_length=200)
    post = models.ForeignKey('Post', models.DO_NOTHING)

    class Meta:
        db_table = 'comments'

class Post(models.Model):
    post_date = models.DateField()
    profile_id = models.IntegerField(unique=True)
    likes = models.IntegerField()
    foto = models.CharField(max_length=50)
    ref = models.ForeignKey('Referencia', models.DO_NOTHING)

    class Meta:
        db_table = 'Post'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    imagem = models.ImageField(upload_to='profile_images', default='blank-profile-picutre.jpg')
    seguidores = models.IntegerField(default=0)
    post = models.ForeignKey('Post', models.DO_NOTHING, null=True, blank=True, default = None)

    class Meta:
        db_table = 'profile'

class Referencia(models.Model):
    post_id = models.IntegerField()
    ref_descricao = models.CharField(max_length=25)

    class Meta:
        db_table = 'referencia'
