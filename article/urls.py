from django.conf.urls import url, include

from article import views


urlpatterns = [

        url(r'^1/', views.basic_one),
        url(r'^2/', views.template_two),
        url(r'^3/', views.template_three_simple),
        url(r'^articles/all/', views.articles),
        url(r'^articles/get/(?P<article_id>\d+)/$', views.article),
        url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike),
        url(r'^articles/addcomment/(?P<article_id>\d+)/(?P<page>\d+)/(?P<comments_count>\d+)/$', views.addcomment),
        url(r'^page/(\d+)/$', views.articles),
           url(r'^article/(\d+)/(\d+)/$', views.article),
        url(r'^', views.articles),
]
