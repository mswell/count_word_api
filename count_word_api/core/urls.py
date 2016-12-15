from django.conf.urls import url

from .views import CountView


urlpatterns = [
    url(r'count-word$',
        CountView.as_view(),
        name='count_word'),
]
