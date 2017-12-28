from django.contrib import admin
from article.models import Article, Comments

# Register your models here.
class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_data']
    inlines = [ArticleInLine]
    list_filter = ['article_data']


admin.site.register(Article, ArticleAdmin)