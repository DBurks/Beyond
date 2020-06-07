import pytest
import io
from html_pages import HtmlPagesConverter

@pytest.fixture
def quote_file():
    return io.StringIO("quote: ' ")

@pytest.fixture
def multi_page_file():
    return io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")

## These operations require looking through files
## We don't want to do that to test our functionality
## so we use fakes.
## Fakes are classes that implement the same interface
## but here are in memory. 
## Imagine you were testing actual files and file servers failed, etc. 
## That means your tests fail.
def test_convert_quotes(quote_file):
    converter = HtmlPagesConverter(open_file=quote_file)
    converted_text = converter.get_html_page(0)
    assert converted_text == "quote: &#x27;<br />"

def test_access_second_page(multi_page_file):
    converter = HtmlPagesConverter(open_file=multi_page_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "page two<br />"