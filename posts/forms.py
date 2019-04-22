from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'kategoriler']  # Blog modelindeki hangi alanları ile çalışacaksın

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)  # kalıtım aldığı init fonksiyonları
        for field in self.fields:
            # print(field, self.fields[field])
            self.fields[field].widget.attrs = {'class': 'form-control'}
            self.fields['content'].widget = forms.Textarea(attrs={'class': 'form-control'})

    def clean_content(self):
        icerik = self.cleaned_data.get('content')
        if len(icerik) < 10:
            uzunluk = len(icerik)
            msg = 'Lütfen en az 250 karakter giriniz girilen karakter sayısı (%s)' % (uzunluk)
            raise forms.ValidationError(msg)
        return icerik
