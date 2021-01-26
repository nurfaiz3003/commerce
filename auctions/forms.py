from django import forms
from .models import AuctionList, Categories

class NewAuction(forms.ModelForm):
    class Meta:
        model = AuctionList
        fields = ['title', 'desc', 'startingbid', 'image', 'categories']

class BidForm(forms.Form):
    place_bid = forms.IntegerField()

class CommentForm(forms.Form):
    comment = forms.CharField()

class AddCategory(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'