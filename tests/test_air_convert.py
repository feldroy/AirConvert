from pathlib import Path

from air_convert import html_to_airtags


def test_html_to_tags():
    sample = """
    <html>
        <body>
            <main>
                <h1 class="header">Hello, World</h1>
            </main>
        </body>
    </html>"""
    assert "air.H1" in html_to_airtags(sample)
    assert "H1" in html_to_airtags(sample)

    # Now test with no prefix
    assert "air.H1" not in html_to_airtags(sample, air_prefix=False)
    assert "H1" in html_to_airtags(sample, air_prefix=False)


def test_html_to_tags_multi_attrs():
    sample = """
    <form action="." method="post" class="searcho">
        <label for="search">
        Search:
        <input type="search" name="search" />
        </label>
    </form>
"""
    tags = html_to_airtags(sample)

    assert (
        tags
        == """air.Form(\n    air.Label("Search:", air.Input(type="search", name="search"), for_="search"),\n    action=".",\n    method="post",\n    class_="searcho",\n)\n"""
    )


def test_doesnt_include_html_from_page():
    """HTML files starting with <!doctype html> can throw this off.

    This page was fetched with:
        curl -o page.html https://example.com && air-convert page.html
    """
    path = Path("tests/test_page.html")
    tags = html_to_airtags(path.read_text())
    assert not tags.startswith('"html"')
