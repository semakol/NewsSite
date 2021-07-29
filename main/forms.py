from .models import News
from django.forms import ModelForm, TextInput, Textarea, FileInput


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["TitleNews", "SomeNews", "Author", "Image", "Tags"]
        widgets = {"TitleNews": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
                  "SomeNews": Textarea(attrs={'class': 'form-control', 'placeholder': 'Новость'}),
                  "Author": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
                  "Image": FileInput(attrs={'class': 'form-control', "accept": "image/*"}),
                  "Tags": TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги, через запитую'})}
