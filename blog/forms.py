from blog.models import BlogPost
from mailing.forms import StyleFormMixin
from django import forms


class BlogForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для модели Client с добавленными стилями.
    """

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview']
