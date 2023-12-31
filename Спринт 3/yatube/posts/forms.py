from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')
        help_texts = {
            'group': 'Выберите группу',
            'text': 'Введите сообщение'
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Заполните эту форму!')
        return data
