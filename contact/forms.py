from django.forms import ModelForm, Textarea, TextInput, EmailInput
from contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "full_name": TextInput(
                attrs={
                    "class": "sizefull s-text7 p-l-22 p-r-22",
                    "placeholder": "Full Name",
                }
            ),
            "phone_number": TextInput(
                attrs={
                    "class": "sizefull s-text7 p-l-22 p-r-22",
                    "placeholder": "Phone Number",
                }
            ),
            "email_address": EmailInput(
                attrs={
                    "class": "sizefull s-text7 p-l-22 p-r-22",
                    "placeholder": "Email Address",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "dis-block s-text7 size20 bo4 p-l-22 p-r-22 p-t-13 m-b-20",
                    "placeholder": "Message",
                    'rows': 4
                }
            ),
        }
