from django.contrib import admin

from .models import User, AuctionList, Bid, Comments, UserList, WatchList
# Register your models here.

admin.site.register(User)
admin.site.register(AuctionList)
admin.site.register(Bid)
admin.site.register(Comments)
admin.site.register(UserList)
admin.site.register(WatchList)