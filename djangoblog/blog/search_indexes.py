import datetime
from haystack import indexes
from blog.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_date = indexes.DateTimeField(model_attr='created_date')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(created_date__lte=datetime.datetime.now())
