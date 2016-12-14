from django.conf.urls import url

from .views import CountView


urlpatterns = [
    url(r'count/(?P<site>\S+)$',
        CountView.as_view(),
        name='count_word'),
]
