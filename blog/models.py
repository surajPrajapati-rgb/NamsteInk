from django.db import models

# class Member(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     phone = models.IntegerField(null = True)
#     joined_date = models.IntegerField(null = True)

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name=models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField( max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user_name = models.CharField(max_length=150) # Your Name
    user_mail = models.EmailField(max_length=254) # YOur Email
    text = models.TextField(max_length=500) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.user_name
