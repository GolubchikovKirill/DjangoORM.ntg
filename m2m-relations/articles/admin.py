from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Section, ArticleSection


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        primary_count = sum(1 for form in self.forms if form.cleaned_data.get('is_primary', False))
        if primary_count != 1:
            raise ValidationError('Каждая статья должна иметь один основной раздел!')
        return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
