from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Review(models.Model):
    review=models.TextField()
    date=models.DateField()

class Contact(models.Model):
    name=models.CharField(max_length=50, default="")
    year=models.CharField(max_length=10, default="")
    email=models.EmailField()
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
        
class PreviousEvent(models.Model):
    title= models.CharField(max_length=50, default="")
    slug = AutoSlugField(populate_from='title')
    desc= models.TextField()
    def __str__(self):
        return self.title

class UpComingEvent(models.Model):
    up_event_id=models.AutoField
    title= models.CharField(max_length=50, default="")
    desc= models.TextField()
    slug = AutoSlugField(populate_from='title')
    image= models.ImageField(upload_to="upcomingevents/images", default="")
    def __str__(self):
        return self.title

class Result(models.Model):
    eventname= models.ForeignKey(PreviousEvent, default="", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='eventname', default="")
    studentname= models.CharField(max_length=60, default="")
    position= models.CharField(max_length=10, default="")
    year= models.CharField(max_length=10, default="")
    department= models.CharField(max_length=50, default="")
    college= models.CharField(max_length=100, default="")
    image= models.ImageField(upload_to="result/images", default="")
    def __str__(self):
        return self.studentname

class Blog(models.Model):
    blogs_id= models.AutoField
    BlogTitle = models.CharField(max_length=80, default="")
    Studentname= models.CharField(max_length=50, default="")
    aboutstudent= models.CharField(max_length=500, default="")
    Date= models.CharField(max_length=20, default="")
    Content = models.TextField()
    image= models.ImageField(upload_to="blogs/blog/images", default="")
    studentimage= models.ImageField(upload_to="blogs/student/images", default="")
    def __str__(self):
        return self.BlogTitle

class Gallery(models.Model):
    gallery_id = models.AutoField
    Event_name = models.CharField(max_length=80, default="")
    Event_id = models.CharField(max_length=80, default="")
    image= models.ImageField(upload_to="gallery")
    def __str__(self):
        return self.Event_name

# class Member(models.Model):
#     member_id=models.AutoField
#     name = models.CharField(max_length=80, default="")
#     email= models.CharField(max_length=50, default="")
#     session= models.CharField(max_length=150, default="")
#     department= models.CharField(max_length=20, default="")
#     contact = models.TextField()
#     date=models.DateField()
#     def __str__(self):
#         return self.name

class ArtCraft(models.Model):
    participant_id=models.AutoField
    name = models.CharField(max_length=100, default="")
    email= models.CharField(max_length=100, default="")
    college= models.CharField(max_length=250, default="")
    department= models.CharField(max_length=100, default="")
    year= models.CharField(max_length=100, default="")
    contact= models.CharField(max_length=100, default="")
    image= models.FileField(upload_to="Creativarty/")
    date=models.DateField()
    def __str__(self):
        return self.name

class quizomania(models.Model):
    participant_id1=models.AutoField
    name = models.CharField(max_length=100, default="")
    email= models.CharField(max_length=100, default="")
    department= models.CharField(max_length=100, default="")
    contact= models.CharField(max_length=100, default="")
    date=models.DateField()
    def __str__(self):
        return self.name
        