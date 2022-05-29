from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, verbose_name='Название')
    articles = models.ManyToManyField(
        Article, 
        related_name='tags', 
        through='ArticleTag'
    )

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['name']

    def __str__(self):
        return self.name


class ArticleTag(models.Model):    
    class Meta:
        unique_together = (('article', 'tag'),)
        ordering = ['-is_main']

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name='Статья'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name='Раздел'
    )
    is_main = models.BooleanField(verbose_name='Основной')