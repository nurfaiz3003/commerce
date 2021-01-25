from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from .models import User, AuctionList, UserList, WatchList, Bid
from .forms import NewAuction, BidForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings": AuctionList.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def add(request):
    if request.method == "POST":
        form = NewAuction(request.POST)
        if form.is_valid():
            form.save()
            auction = AuctionList.objects.latest('id')
            userlistdata = UserList(user_id = request.user, auctionlist_id = auction)
            userlistdata.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/add.html", {
                "form": form
            }) 

    return render(request, "auctions/add.html", {
        "form": NewAuction() 
    })

def listingpage(request, listing_id):
    if request.user.is_authenticated:
        auction = AuctionList.objects.get(pk=listing_id)
        currentuser= UserList.objects.filter(auctionlist_id = auction, user_id = request.user)
        check = WatchList.objects.filter(auctionlist_id = auction, user_id = request.user)
        return render(request, "auctions/listingpage.html", {
            "listing": AuctionList.objects.get(pk=listing_id),
            "currentbid": Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid')),
            "check": check,
            "form": BidForm(),
            "close": currentuser
        })
    else:
        auction = AuctionList.objects.get(pk=listing_id)
        currentbid = Bid.objects.filter(auctionlist_id = auction)
        if currentbid:
            bid = currentbid.aggregate(Max('bid'))
            return render(request, "auctions/listingpage.html", {
                "listing": AuctionList.objects.get(pk=listing_id),
                "currentbid": bid
            })
        else:
            return render(request, "auctions/listingpage.html", {
                "listing": AuctionList.objects.get(pk=listing_id),
                "currentbid": None,
            })

@login_required
def addwatchlist(request, listing_id):
    if request.method == "POST":
        auction = AuctionList.objects.get(pk=listing_id)
        watch = WatchList(user_id = request.user, auctionlist_id = auction)
        watch.save()
        return HttpResponseRedirect(reverse("listingpage", args=[listing_id]))

@login_required
def removewatchlist(request, listing_id):
    if request.method == "POST":
        auction = AuctionList.objects.get(pk=listing_id)
        WatchList.objects.filter(user_id = request.user, auctionlist_id = auction).delete()
        return HttpResponseRedirect(reverse("listingpage", args=[listing_id]))
    
@login_required
def placebid(request, listing_id):
    if request.method == "POST":
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            bid = bid_form.cleaned_data['place_bid']
            auction = AuctionList.objects.get(pk=listing_id)
            lbid = Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid'))
            latestbid = lbid['bid__max']
            startingbid = AuctionList.objects.get(pk=listing_id).startingbid
            check = WatchList.objects.filter(auctionlist_id = auction, user_id = request.user)
            if latestbid:
                if bid > latestbid:
                    placebid = Bid(user_id = request.user, auctionlist_id = auction, bid = int(bid))
                    placebid.save()
                    return render(request, "auctions/listingpage.html", {
                            "listing": AuctionList.objects.get(pk=listing_id),
                            "currentbid": Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid')),
                            "check": check,
                            "form": BidForm(),
                            "message": "Place Bid Succesful"
                        })
                else:
                    return render(request, "auctions/listingpage.html", {
                            "listing": AuctionList.objects.get(pk=listing_id),
                            "currentbid": Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid')),
                            "check": check,
                            "form": BidForm(),
                            "message": "Bid must be larger than Current or Starting Bid"
                        })
            else:
                if bid > startingbid:
                    placebid = Bid(user_id = request.user, auctionlist_id = auction, bid = int(bid))
                    placebid.save()
                    return render(request, "auctions/listingpage.html", {
                            "listing": AuctionList.objects.get(pk=listing_id),
                            "currentbid": Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid')),
                            "check": check,
                            "form": BidForm(),
                            "message": "Place Bid Succesful"
                        })
                else:
                    return render(request, "auctions/listingpage.html", {
                            "listing": AuctionList.objects.get(pk=listing_id),
                            "currentbid": Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid')),
                            "check": check,
                            "form": BidForm(),
                            "message": "Bid must be larger than Current or Starting Bid"
                        })
        else:
            return render(request, "auctions/listingpage.html", {
                "listing": AuctionList.objects.get(pk=listing_id),
                "currentbid": Bid.objects.filter(auctionlist_id = auction).aggregate(Max('bid')),
                "form": BidForm(),
                "message": "Form is Not Valid"
            })

@login_required
def close(request, listing_id):
    pass