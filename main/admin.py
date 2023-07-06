from django.contrib import admin
from .models import tweets, twitterUser

# Register your models here.
admin.site.register(tweets)
admin.site.register(twitterUser)
