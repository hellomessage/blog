from django.conf.urls import url
from django.contrib import admin

from bookmark.models import Bookmark
from bookmark.views import BookmarkLV, BookmarkDV


urlpatterns = [
    # Class-base views
    url(r'^$', BookmarkLV.as_view(model=Bookmark), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(model=Bookmark), name='detail'),
]
