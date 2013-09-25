from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from markdown import markdown
from django.db.models import F

class TagManager(models.Manager):
    '''tag manager'''
    def decrement_count(self, ids, isolate_clear=True):
        '''decrement count'''
        c = F('count')-1
        self.filter(id__in=ids).update(count=c)
        if isolate_clear:
            self.filter(count__lte=0).delete()

    def increment_count(self ,ids):
        '''increment count'''
        c = F('count')+1
        self.filter(id__in=ids).update(count=c)
    
    def tops(self, num):
        return self.order_by('-count')[:num]

class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    count = models.IntegerField(default=0, editable=False)
    objects = TagManager()

    def __unicode__(self):
        return '%s' % self.name

class Article(models.Model):
    '''article model'''
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    text_html = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)
    
    class Meta:
        ordering = ['-created_date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_article_detail', (),
                {
                    'slug':self.slug,
                })
    #autogenerate,if value is 'joel is a slug',the out put will be 'joel-is-a-slug'.
    def save(self, *args, **kwargs):
        self.text_html = markdown(self.text, ['codehilite'])

        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

class Register(models.Model):
    '''register model'''
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64, unique=True)
    website = models.URLField(max_length=128, null=True, blank=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s,%s' %(self.name,self.email)

class Comment(models.Model):
    '''comment model'''
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    website = models.URLField(max_length=128, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.text

