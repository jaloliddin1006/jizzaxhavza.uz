from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "phone", "body")



    # def save(self, request, commit=True):
    #     contact = self.instance
    #     contact.author = request.user
    #     super().save(commit)
    #     return contact