from django import forms
from Lulz_orders.models import STL

class GenericSTLForm(forms.ModelForm):
    class Meta:
        model = STL
        fields = ('title', 'stl_file' )
