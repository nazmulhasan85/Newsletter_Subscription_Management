"""newsletter_subscription_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from article.views import CreatePostView, PostDetailView, PostListView, post_detail_view, rating_list
from django.views.decorators.cache import cache_page
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$',index, name='home'),
    url(r'^$', cache_page(60*15)(PostListView.as_view()), name='home'),
    url(r'post/new/$',CreatePostView.as_view(), name='post_new'),
    #url(r'post/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
    url(r'post/(?P<pk>\d+)$', post_detail_view, name='post_detail'),
    url(r'admin/rating/list/$', rating_list, name="post_rating_list"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
