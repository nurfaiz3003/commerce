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
    path("<int:listing_id>/delete", views.removewatchlist, name="removewatchlist")
]
