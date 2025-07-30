# air-convert

![PyPI version](https://img.shields.io/pypi/v/air-convert.svg)

Utility for converting HTML to Air Tags

* PyPI package: https://pypi.org/project/air-convert/
* Free software: MIT License
* Documentation: https://github.com/feldroy/air_convert

## Installation

Pip:

```sh
pip install air-covert
```

UV:

```sh
uv add air-covert
```


## Usage from the command line

```sh
air-convert local/path/to/my/page.html
```

When combined with curl or wget:

```sh
curl -o page.html https://example.com && air-convert page.html
```

```sh
wget -O page.html https://example.com && air-convert page.html
```



## Programmatic usage


```python
from air_convert import html_to_airtags
html_to_airtags("""
<main>
    <article class="prose">
        <h1>Hello, world</h1>
        <p>Let's soar into the air!</p>
    </article>
</main>
""")
```

Generates:

```python
air.Main(
    air.Article(
        air.H1("Hello, world"),
        air.P("Let\'s soar into the air!"),
        class_="prose"
    )
)
```

## Credits

- This package was created with the awesome [Cookiecutter](https://github.com/audreyfeldroy/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
- Uses the elegant Typer framework to provide a CLI interface
- Relies on BeautifulSoup4 for parsing of HTML
- Formatting of generated code provided by Ruff

