from django.db import models


# Create your models here.

class User(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)
    FirstName = models.CharField(db_column='FirstName', max_length=225)
    LastName = models.CharField(db_column='LastName', max_length=225)
    UserName = models.CharField(db_column='UserName', max_length=225)
    Email = models.CharField(db_column='Email', max_length=225)
    ProfilePic = models.ImageField(upload_to="uploads", null=True, blank=True)
    Password = models.CharField(db_column='Password', max_length=20)
    RegisterDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User'
