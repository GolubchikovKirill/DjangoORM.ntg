from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название раздела")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    # Связь многие ко многим через промежуточную модель
    sections = models.ManyToManyField(Section, through='ArticleSection', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)  # Основной ли раздел?

    class Meta:
        unique_together = ('article', 'is_primary')  # У одной статьи может быть только один основной раздел

    def __str__(self):
        return f"{self.article.title} - {self.section.name}"