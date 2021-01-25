from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class AuctionList(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField(max_length=1000)
    startingbid = models.IntegerField()
    image = models.URLField(blank=True)
    categories = models.CharField(max_length=64, blank=True)
    closed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} | Category : {self.categories} | Bid : {self.startingbid}"

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    bid = models.IntegerField()

    def __str__(self):
        return f"({self.user_id}) bid ({self.auctionlist_id}) for ({self.bid})"


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)

class UserList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)

class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.user_id}) add ({self.auctionlist_id}) to Watch List"
