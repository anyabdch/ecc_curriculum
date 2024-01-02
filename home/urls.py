from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import image_upload_view
from home.views import (
    landing_view,
    home_redirect_view,
    simple_form_view,
    post_form_view,
    test_markdownify,
    PlaylistDetailView
)

urlpatterns = [
    path("", landing_view, name="landing"),
    path("<slug:slug>", PlaylistDetailView.as_view(), name="landing_content"),
    path("simple-form/", simple_form_view, name="simple_form"),
    path("post-form/", post_form_view, name="post_form"),
    path("test-markdownify/", test_markdownify, name="test_markdownify"),
    path('upload/', image_upload_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)