import pytest
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from count_word_api.helpers.base_test import BaseTest


@pytest.mark.django_db
class TestCountWordView(BaseTest):

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

    def test_get_authorized_client_status_code(self, authorized_client):
        url = reverse('core:count_word')
        url += "?url=http://www.uol.com.br/"
        url += "&word=feijão"
        with self.vcr():
            resp = authorized_client.get(url)
        assert resp.status_code == status.HTTP_200_OK

    def test_get_authorized_client_ocurrences_of_word(self, authorized_client):
        expected_content = {'Senado': 4}
        url = reverse('core:count_word')
        url += "?url=http://www.uol.com.br/"
        url += "&word=Senado"
        with self.vcr():
            resp = authorized_client.get(url)
        assert resp.json() == expected_content
