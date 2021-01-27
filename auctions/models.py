from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

# Model for Storing Categories
class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"

# Model for Storing Auction Data 
class AuctionList(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField(max_length=1000)
    startingbid = models.IntegerField()
    image = models.URLField(blank=True)
    categories = models.ForeignKey(Categories, blank=True, null=True, on_delete=models.SET_NULL, related_name="listing")
    closed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | Category : {self.categories} | Bid : {self.startingbid}"

# Model for Storing Bid Data
class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    bid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.user_id}) bid ({self.auctionlist_id}) for ({self.bid})"

# Model for Comments
class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

# Model for Storing List of Listing Items a User Have
class UserList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)

# Model for Storing List of Watchlist a User Have
class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionlist_id = models.ForeignKey(AuctionList, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.user_id}) add ({self.auctionlist_id}) to Watch List"