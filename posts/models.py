from django.db import models
import os
from uuid import uuid4
from django.shortcuts import reverse
from django.template.defaultfilters import slugify, safe
from unidecode import unidecode


def upload_to(instance, filename):
    uzanti = filename.split('.')[-1]
    new_name = "%s.%s" % (str(uuid4()), uzanti)
    unique_id = instance.unique_id
    return os.path.join('post', unique_id, new_name)


class Kategori(models.Model):
    isim = models.CharField(max_length=10, verbose_name='Kategori İsmi', null=True)

    class Meta:
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.isim


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Başlık ',
                             help_text='Başlık bilgisi burada girilir.')
    # user = models.ForeignKey(User, default=1, null=True, verbose_name='User', on_delete=True, related_name='blog')

    content = models.TextField(max_length=5000, verbose_name='İçerik', null=True, blank=False)
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(null=True, unique=True, editable=False)

    unique_id = models.CharField(max_length=100, editable=True, null=True)
    kategoriler = models.ManyToManyField(to=Kategori, related_name='blog', null=True)
    image = models.ImageField(verbose_name='Resim', upload_to=upload_to,
                              null=True, help_text='Kapak Fotoğrafı Yükleyiniz', blank=True)

    class Meta:
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'
        ordering = ['-id']

    def __str__(self):
        return '{} '.format(self.title)#, self.user)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Post.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s" % (slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.unique_id = str(uuid4())
            self.slug = self.get_unique_slug()
        else:
            post = Post.objects.get(slug=self.slug)
            if post.title != self.title:
                self.slug = self.get_unique_slug()

        super(Post, self).save(*args, **kwargs)
