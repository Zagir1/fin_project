from django.db import models
from phone_field import PhoneField


# Create your models here.


class Section(models.Model):
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.topic


class User(models.Model):
    username = models.CharField(max_length=255, blank=True)
    mail = models.EmailField(max_length=255, unique=True, blank=True)
    date_of_birth = models.DateField(blank=True)
    tel_number = PhoneField(null=False, blank=True, unique=True)
    is_act = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Review(models.Model):
    username = models.ForeignKey('User', on_delete=models.PROTECT, blank=True)
    comment = models.TextField(max_length=2550, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.created


class Discussion(models.Model):
    username = models.ForeignKey('User', on_delete=models.PROTECT, blank=True)
    topic = models.ManyToManyField(Section)
    d_title = models.CharField(max_length=255, blank=True)
    branch = models.TextField(max_length=2550, blank=True)
    picture = models.ImageField(upload_to="images/", null=True, blank=True)
    created_d = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.created_d


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    mail_address = models.EmailField(max_length=255, unique=True, blank=True)
    tel_num = PhoneField(null=False, blank=True, unique=True)
    birth_day = models.DateField(blank=True)
    portrait = models.ImageField(upload_to="images/", null=True, blank=True)
    inf_about = models.TextField(max_length=2550, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class News(models.Model):
    title = models.CharField(max_length=255, blank=True)
    topic = models.ManyToManyField(Section)
    summary = models.TextField(max_length=25500, blank=True)
    picture = models.ImageField(upload_to="images/", null=True, blank=True)
    auth_opinion = models.TextField(max_length=2550, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    source = models.URLField(max_length=255, null=True)
    d_created = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s, %s' % (self.title, self.author)


# class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#    avatar = models.ImageField(
#        default='avatar.jpg',  # default avatar
#        upload_to='profile_avatars'  # dir to store the image
#    )
#
#    def __str__(self):
#       return f'{self.user.username} Profile'
#
#    def save(self, *args, **kwargs):
#        # save the profile first
#        super().save(*args, **kwargs)
#
#        # resize the image
#        img = Image.open(self.avatar.path)
#        if img.height > 300 or img.width > 300:
#            output_size = (300, 300)
#            # create a thumbnail
#            img.thumbnail(output_size)
#            # overwrite the larger image
#            img.save(self.avatar.path)
