from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add, name="add"),
    path("<int:listing_id>", views.listingpage, name="listingpage"),
    path("<int:listing_id>/watch", views.addwatchlist, name="addwatchlist"),
    path("<int:listing_id>/delete", views.removewatchlist, name="removewatchlist"),
    path("<int:listing_id>/placebid", views.placebid, name="placebid"),
    path("<int:listing_id>/close", views.close, name="close"),
    path("<int:listing_id>/addcomment", views.addcomment, name="addcomment"),
    path("watchlist", views.mylists, name="mylists")
]
