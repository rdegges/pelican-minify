# pelican-minify

An HTML minification plugin for
[Pelican](http://pelican.readthedocs.org/en/latest/), the static site generator.


## Install

To install the library, you can use
[pip](http://www.pip-installer.org/en/latest/).

```bash
$ pip install pelican-minify
```


## Usage

To use `pelican-minify`, you need to make only a single change to your
`pelicanconf.py` file (the configuration file that Pelican uses to generate
your static site.

Update your `PLUGINS` global, and append `minify` to the list, eg:

``` python
# pelicanconf.py

# ...

PLUGINS = [
    # ...
    'minify',
    # ...
]

# ...
```

The next time you build your Pelican site, `pelican-minify` will automatically
minify your Pelican pages after they've been generated.

This reduces file size and obscures the public source code, but keep in
mind--minifying your static site will increase your Pelican build times, as it
adds extra file processing for each page generated.


## Changelog

v0.1: 12-4-2012

    - First release!
