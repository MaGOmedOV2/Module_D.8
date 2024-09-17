from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'author',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if content is not None and len(content) < 20:
            raise ValidationError({
                "content": "Описание не может быть меньше 20 символов."
            })

        title = cleaned_data.get('title')
        if title == content:
            raise ValidationError({
                "title": "Описание не должно быть идентичным названию."
            })

        title = self.cleaned_data["title"]
        if title[0].islower():
                raise ValidationError({
                    "title": "Название должно начинаться с заглавной буквы."
                })

        return cleaned_data