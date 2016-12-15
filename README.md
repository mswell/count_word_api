[![Build Status](https://travis-ci.org/rafaelhenrique/count_word_api.svg?branch=master)](https://travis-ci.org/rafaelhenrique/count_word_api)

# count_word_api

API to count occurrences of one word on any site

## Instalation

Create virtualenv:

```
python3.5 -m venv .venv
```

Activate your virtualenv:

```
source .venv/bin/activate
```

Run installation:

```
make install
```

## Run project for development

```
make run
```

## Help

```
make help
```

## How i use API?

You need to create a superuser first:

```
make createsuperuser
```

Now access url from your favorite browser:

[http://localhost:8000/admin](http://localhost:8000/admin)

Do login and create an api user and api key. Now you call count word with curl like this:

```
curl -X GET -H "Authorization: Token <YOUR API KEY HERE>" "http://localhost:8000/count-word?url=http://www.uol.com.br/&word=senado"
```

The response will be similar to this below:

```
{"senado": 4}
```

This response represent 4 words found on site [http://www.uol.com.br](http://www.uol.com.br).

## Error messages

- Message: Site informado indisponível no momento.
    - Site unavailable;
- Message: Este campo não pode ser nulo.
    - Field cannot be null;
- Message: Entrar um URL válido.
    - URL is not valid;

To translate messages to your language see Django documentation here: [https://docs.djangoproject.com/en/1.10/ref/settings/#language-code](https://docs.djangoproject.com/en/1.10/ref/settings/#language-code).

*IMPORTANT*: All error messages return HTTP status code 400.
