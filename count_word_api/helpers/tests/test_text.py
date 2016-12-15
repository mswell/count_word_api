from count_word_api.helpers.text import html_to_text, remove_punctuation


class TestTextHelper(object):
    def setup(self):
        self.myhtml = ("<html><head></head><body>"
                       "RAFAEL<a>TESTE</a><p>TESTE2</p><p><p>TESTE3</p></p>"
                       "</body></html>")

    def test_extract_text_from_html(self):
        expected_text = 'RAFAEL TESTE TESTE2 TESTE3'
        text = html_to_text(self.myhtml)
        assert expected_text == text

    def test_remove_punctuation(self):
        expected_text = "Rafael"
        punctuation = "!@#$%^&*()[]{}';:,./<>?\|`~-=_+\""
        for char in punctuation:
            text = "Rafael"
            text += char
            text = remove_punctuation(text)
            assert expected_text == text
