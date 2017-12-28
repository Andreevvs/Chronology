from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</html></body>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template ('myview.html')
    html = t.render({'name': view})
    return HttpResponse(html)

def template_three_simple(request):
    view = "template_three_simple"
    return render_to_response ('myview.html', {'name': view})

def articles(request, page_number = 1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles,2)
    return render_to_response ('articles.html', {'articles':  current_page.page(page_number), 'username': auth.get_user(request).username})

def article(request, article_id=1, page_number = 1):
    comment_form = CommentForm
    all_comments = Comments.objects.filter(comments_article_id=article_id)
    current_page = Paginator(all_comments,8)
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args ['comments']=current_page.page(page_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response ('article.html', args)

def addlike (request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save ()
    except ObjectDoesNotExist:
        raise Http404
    return redirect ('/')

def addcomment (request, article_id, page, comments_count):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
    count = int(comments_count)
    intpage = int (page)
    if (count%2 == 0):
        num_pages=intpage+1
    else:
        num_pages=intpage
    return redirect('/article/%s/%s/' % (article_id, num_pages))
