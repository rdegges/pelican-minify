# pelican-minify

[![PyPI Version](https://img.shields.io/pypi/v/pelican-minify.svg)](https://pypi.python.org/pypi/pelican-minify)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pelican-minify.svg)](https://pypi.python.org/pypi/pelican-minify)
[![Build Status](https://secure.travis-ci.org/rdegges/pelican-minify.png?branch=master)](https://travis-ci.org/rdegges/pelican-minify)

An HTML minification plugin for
[Pelican](http://pelican.readthedocs.org/en/latest/), the static site generator.

![Pelican Logo](https://github.com/rdegges/pelican-minify/raw/master/pelican.png)


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

`pelican-minify` can also be configured by setting `MINIFY` to a hash containing
[parameters to htmlmin](https://htmlmin.readthedocs.org/en/latest/reference.html#htmlmin.minify), eg:

``` python
# pelicanconf.py

# ...

MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

# ...
```

This reduces file size and obscures the public source code, but keep in
mind--minifying your static site will increase your Pelican build times, as it
adds extra file processing for each page generated.

**NOTE**: You should probably include the `minify` plugin at the very bottom of
your `PLUGINS` array.  This will ensure it is the last thing to run, and
doesn't prematurely gzip any files.


## Changelog

v0.1: 12-4-2012

    - First release!

v0.2: 2-12-2013

    - Fixing issue with unicode characters.
    - Upgrading django-htmlmin dependency.

v0.3: 2-12-2013

    - Fixing tests.

v0.4: 2-15-2013

    - Upgrading django-htmlmin.

v0.5: 8-28-2014

    - Python 3 compatibility (thanks @AlexJF!).

v0.6: 9-9-2014

    - Fixing unicode bug (thanks @kura!).

v0.7: 11-4-2014

    - Making minification work on .htm files (thanks @Undeterminant!).

v0.8: 5-12-2015

    - No longer removing optional quotes from HTML elements. This provides
      better compatibility across browsers / etc.

v0.9: 11-25-2015

    - Making minify library configurable.
    - Removing aggressive whitespace removal (*avoids issues*).
