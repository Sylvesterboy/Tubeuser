from django import forms
from testapp.models import Customer
from testapp.models import MyVideos
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class VideoForm(forms.ModelForm):
    class Meta:
        model = MyVideos
        fields = "__all__"