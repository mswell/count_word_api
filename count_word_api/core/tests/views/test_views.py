import pytest
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCountWordView(object):

    @pytest.fixture
    def authorized_client(self):
        user = mixer.blend(User, username="a")
        token = mixer.blend(Token, user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        return client

    @pytest.fixture
    def unauthorized_client(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token XPTO')
        return client

    def test_get_authorized_client(self, authorized_client):
        url = reverse('core:count_word',
                      kwargs={'site': 'www.google.com'})
        url += "?word=feijão"
        resp = authorized_client.get(url)
        assert resp.status_code == status.HTTP_200_OK
