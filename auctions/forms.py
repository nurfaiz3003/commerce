from django import forms
from .models import AuctionList

class NewAuction(forms.ModelForm):
    class Meta:
        model = AuctionList
        fields = '__all__'