import datetime
from django import template

from blog.models import Article,Tag
register = template.Library()

@register.inclusion_tag('blog/sidebar/tags.html')
def tags():
    tags = Tag.objects.all()
    return {
            'tags': tags
            }

@register.inclusion_tag('blog/sidebar/archives.html')
def archives():
    articles = Article.objects.all()
    today = datetime.date.today()
    articlesInCurYear = articles.exclude(created_date__gte = today+datetime.timedelta(days=1)).filter(created_date__gte = datetime.datetime(today.year, 1, 1))
    archives = {}
    
    for article in articlesInCurYear:
        created_on = article.created_date
        #key = '%d-%d' %(created_on.year,created_on.month)
        key = datetime.datetime(created_on.year, created_on.month, 1)
        archives[key] = archives.get(key,0) + 1
    return {
            'archives': archives,
            }
            


