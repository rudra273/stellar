from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): 
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)  


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'post')

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text
