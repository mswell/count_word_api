import pytest
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
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
        resp = authorized_client.get(resolve_url('core:count_word'))
        assert resp.status_code == status.HTTP_200_OK
