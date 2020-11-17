from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'Your description',
                                          'row': 10,
                                          'cols': 120
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=199.99)

    email = forms.EmailField(initial="bgunduz43@gmail.com")

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


"""def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get("title")
    if "CFE" in title:
        raise forms.ValidationError("This is not valid")
    return title


def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get("email")
    if not email.endswith('com'):
        raise forms.ValidationError("This is not valid")
    return email"""


class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Your tle"}))  # max_length
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={'placeholder': 'your description',
                                             "class": "new-class-name two",
                                             "id": "my-id-for-textarea",
                                             'row': 20,
                                             'cols': 120
                                             }
                                  )
                                  )
    price = forms.DecimalField(initial=199.99)
