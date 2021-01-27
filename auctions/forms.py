from django import forms
from .models import AuctionList, Categories
from django.utils.translation import gettext_lazy as _

#Forms for Create Auctions Page
class NewAuction(forms.ModelForm):
    class Meta:
        model = AuctionList
        fields = ['title', 'desc', 'startingbid', 'image', 'categories']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add product names...'}),
            'desc': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your product descriptions...'}),
            'startingbid': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$ Input your starting price'}),
            'image':forms.URLInput(attrs={'class':'form-control', 'placeholder':'Inpur valid image URL'}),
            'categories': forms.Select(attrs={'class':'form-control'})
        }

        labels = {
            'title': _('Product Name'),
            'desc': _('Description'),
            'startingbid': _('Starting Bid'),
            'image': _('Product Image URL'),
            'categories': _('Select Category'),
        }

#Forms for Bidding in Listing Item Page
class BidForm(forms.Form):
    place_bid = forms.IntegerField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '$ Place your bid...',
            'label': 'Add new category if not available'
        }
    ))

#Forms for Adding Comments in Listing Page 
class CommentForm(forms.Form):
    comment = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write your comment...'
        }
    ))

#Forms for Adding New Category through Create Auction Page
class AddCategory(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }