from django.forms import ModelForm, Textarea, TextInput, EmailInput
from blog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

        widgets = {
            "text": Textarea(
                attrs={
                    "class": "dis-block s-text7 size18 bo12 p-l-18 p-r-18 p-t-13 m-b-20",
                    "placeholder": "Comment",
                    'rows': 4
                }
            ),
        }
