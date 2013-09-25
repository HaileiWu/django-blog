from django.conf.urls import patterns, include, url
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from django.contrib.syndication.views import Feed

from models import Article

class BlogFeed(Feed):
    title = "MySite"
    description = "my first django blog"
    link = "/blog/feed/"

    def items(self):
        return Article.objects.all().order_by("-created_date")[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.text
    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('',
        url(r'^article/(?P<slug>[-\w]+)$',
            'blog.views.view_article',
            name='blog_article_detail',
            ),

        url(r'^articles$',
            'blog.views.view_list',
            name='blog_article_list',
            ),
        url(r'^articles/(?P<year>\w+)/(?P<month>\w+)$',
            'blog.views.view_archive_in_cur_year',
            name='blog_article_archive',
            ),
        url(r'^articles/tag-(?P<tag>\w+)$',
            'blog.views.view_tag',
            name='blog_article_tag',
            ),
        url(r'^search/$',SearchView(
            template='search/search.html',
            form_class=SearchForm,
            ),name='haystack_search',
            ),
        url(r'^feed/$',BlogFeed(),),
        )
