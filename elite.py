===============>>>><img src="{% static 'images/logo/logo-light.png'  %}" 


<img alt="image" src="{{user_object.userimg.url}}"  class="rounded-circle author-box-picture">
/media/2.png

user and profile are 1-1

tmp=User.objects.get(username=request.user.username)
	user_object = Profile.objects.get(user_id=tmp.id)
	context={
	'user_object':user_object,
	}

https://stackoverflow.com/questions/70656495/importerror-cannot-import-name-ugettext-lazy

booking_no_for_enquiry = models.CharField(primary_key=True,default='{}{:%Y%m%d%H%M%S}'.format(str(uuid.uuid4().hex), datetime.now()), max_length=100, editable=False)	

A-- CURD Search
IMUL-- Media Settings
NIC-------signup email

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'elite',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',  
        'PORT': '3306',
    }
}

import pymysql

pymysql.install_as_MySQLdb()
-----------------------------
<input type="checkbox" name="checks[]" value="1" />
<input type="checkbox" name="checks[]" value="2" />
<input type="checkbox" name="checks[]" value="3" />
<input type="checkbox" name="checks[]" value="4" />

views.py

some_var = request.POST.getlist('checks[]')
------------------------------------------
from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
------------------------------------------------

from django.db import models
from django_random_id_model import RandomIDModel
user = models.CharField(max_length=100,default="Open")

class Customer(models.Model):
    name = models.CharField(max_length=50)
class Customer(RandomIDModel):
    name = models.CharField(max_length=50)

By default the ID will be 12 digits long, but you can override this in settings.py with the ID_DIGITS_LENGTH

-----------------------------------------------------------
from django.db import models
from django.contrib.auth import get_user_model
#import uuid
#from datetime import datetime
User = get_user_model()

==================================
user = models.ForeignKey(User, on_delete=models.CASCADE)

from django.contrib.auth.models import AbstractUser

def user_avatar_path(instance, filename):
    return 'user_{0}/avatar/{1}'.format(instance.id, filename)

class User(AbstractUser):
    phone=models.IntegerField(max_length=12,default=0)

    def __str__(self):
        return self.username

# myproject/settings.py
# .......
# .......
AUTH_USER_MODEL = 'core.User'	






customer_name = models.CharField(max_length=30,null=False)
	type_of_shifting = models.CharField(max_length=30)
	customer_email = models.EmailField(max_length=30,null=False)
	customer_phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	location_from = models.CharField(max_length=30)
	location_to = models.CharField(max_length=30)
	shifting_date = models.DateField()

#from django.contrib.auth.models import AbstractUser


"""class User(AbstractUser):
	userimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
	userphone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
"""
















=========================================
