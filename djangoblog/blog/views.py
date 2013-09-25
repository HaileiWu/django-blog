import datetime
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import CommentForm
from models import Article

def view_article(request, slug):
    '''article detail'''
    article = get_object_or_404(Article, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article=article
        comment.save()
        '''save data to session'''
        request.session["name"] = comment.name
        request.session["email"] = comment.email
        request.session["website"] = comment.website
        return redirect(request.path)
    form.initial["name"] = request.session.get("name")
    form.initial["email"] = request.session.get("email")
    form.initial["website"] = request.session.get("website")
    return render_to_response(
            'blog/blog_article.html',
            {
                'article': article,
                'form': form,
            },
            context_instance=RequestContext(request))

def view_list(request):
    '''article list'''
    article_list = Article.objects.all()
    paginator = Paginator(article_list,3)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response(
            'blog/article_list.html',
            {
                'articles': articles,
            },
            context_instance=RequestContext(request))
def view_archive_in_cur_year(request, year, month):
    '''article archive'''
    article_list = Article.objects.filter(created_date__gte=datetime.datetime(int(year),int(month),1)-datetime.timedelta(days=1))
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response(
            'blog/article_list.html',
            {
                'articles': articles,
            },
            context_instance=RequestContext(request))

def view_tag(request, tag):
    '''articles of specified tag'''
    article_list = Article.objects.filter(tags__name=tag)
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response(
            'blog/tag_articles.html',
            {
                'tag': tag,
                'articles': articles,
            },
            context_instance=RequestContext(request))


        
