from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()


#     def __str__(self):
#         return self.title


class User(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.TextField()


    def __str__(self):
        return self.name