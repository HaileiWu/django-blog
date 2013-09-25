from django.db import models
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db.models import F

from models import Article,Register,Comment,Tag
from forms import ArticleForm

class ArticleAdmin(admin.ModelAdmin):
    '''article admin'''
    date_hierarchy = 'created_date'
    exclude = ('slug','text_html')
    list_filter = ['tags',]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    form = ArticleForm

    def save_model(self, request, obj, form, change):
        '''override the save_model method for correct the tag count'''
        old_tags = set()
        if obj.id:
            old_tags = set(Article.objects.get(id=obj.id).tags.values_list('id', flat=True))
        #before adding tags ,you should save article and override m2m method
        _save_m2m = form.save_m2m
        def after_save():
            _save_m2m()
            # get the correct tag count
            if obj.id:
                new_tags = set(obj.tags.values_list('id', flat=True))
                decrement_tags = old_tags - new_tags
                increment_tags = new_tags - old_tags
                if decrement_tags:
                    Tag.objects.decrement_count(decrement_tags)
                if increment_tags:
                    Tag.objects.increment_count(increment_tags)
            else:
                obj.tags.all().update(count=F('count') + 1)
        form.save_m2m = after_save
        return super(ArticleAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        '''override delete_model'''
        tags = obj.tags.values_list('id',flat=True)
        if tags:
            Tag.objects.decrement_count(tags)
        return super(ArticleAdmin, self).delete_model(request, obj)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Register)
admin.site.register(Comment)
admin.site.register(Tag)
