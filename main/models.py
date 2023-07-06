from django.db import connections
from django.db import models

# Create your models here.

class tweets(models.Model):
    NUETRAL = 'NM'
    OFFENSIVE = 'OL'
    HATEFUL = 'HM'
    categories = [
        (NUETRAL, "Nuetral"),
        (OFFENSIVE, "Offensive Language"),
        (HATEFUL, "Hateful Message")
    ]
    twitterUser = models.CharField(max_length=255)
    tweet = models.CharField(max_length=255)
    tweetURL = models.CharField(max_length=255)
    category = models.CharField(
        max_length=30,
        choices=categories,
        default='Not yet analysed'
    )

    def __str__(self):
        return self.tweet
    
class twitterUser(models.Model):
    NUETRAL = 'Nuetral'
    OFFENSIVE = 'Offensive Language'
    HATEFUL = 'Hateful Message'
    categories = [
        (NUETRAL, "Nuetral"),
        (OFFENSIVE, "Offensive Language"),
        (HATEFUL, "Hateful Message")
    ]
    twitterUser = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    category = models.CharField(
        max_length=30,
        choices=categories,
        default='Not yet analysed'
    )

    def __str__(self):
        return self.bio