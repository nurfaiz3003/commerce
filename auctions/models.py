from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchlist = models.ManyToManyField('AuctionList', blank=True, related_name="watcher")
    userlist = models.ManyToManyField('AuctionList', blank=True, related_name="owner")

class AuctionList(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField(max_length=1000)
    currentbid = models.IntegerField()
    image = models.URLField()
    categories = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    bid = models.IntegerField()

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)