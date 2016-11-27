from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.username

		
		

class itemclass(models.Model):
    shortcuts=models.CharField(max_length=50)      #简述
    descriptions=models.TextField()         #描述
    user=models.ForeignKey(User)
    pub_date = models.DateTimeField('date published')

    
    def __str__(self):
        return self.shortcuts

