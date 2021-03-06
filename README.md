[![Build Status](https://travis-ci.org/rafaelhenrique/count_word_api.svg?branch=master)](https://travis-ci.org/rafaelhenrique/count_word_api)

# count_word_api

API to count occurrences of one word on any site

## Instalation

Clone this project:

```
git clone https://github.com/rafaelhenrique/count_word_api.git
```

Enter on directory:

```
cd count_word_api
```

Create virtualenv:

```
python3.5 -m venv .venv
```

Activate your virtualenv:

```
source .venv/bin/activate
```

Copy localenv file example to root directory of this project:

```
cp contrib/localenv .env
```

Now configure your .env file (use your preferred text editor), then run installation:

```
make install
```

## Run project for development

```
make run
```

## More commands/target on make

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
curl -X GET -H "Authorization: Token <YOUR API KEY HERE>" \
    "http://localhost:8000/count-word?url=http://www.uol.com.br/&word=senado"
```

The response will be similar to this below:

```
{"senado": 4}
```

This response represent 4 words found on site [http://www.uol.com.br](http://www.uol.com.br). 

*IMPORTANT*: Any word or any url can be passed to url "http://www.uol.com.br" and the word "senado" are just examples of use.

## Error messages

- Message: Site informado indisponível no momento.
    - Site unavailable;
- Message: Este campo não pode ser nulo.
    - Field cannot be null;
- Message: Entrar um URL válido.
    - URL is not valid;

To translate messages to your language see Django documentation here: [https://docs.djangoproject.com/en/1.10/ref/settings/#language-code](https://docs.djangoproject.com/en/1.10/ref/settings/#language-code).

*IMPORTANT*: All error messages return HTTP status code 400.
