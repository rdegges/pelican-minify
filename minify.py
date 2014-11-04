"""A Pelican plugin which minifies HTML pages."""


from logging import getLogger
from os import walk
from os.path import join
import sys

from htmlmin import minify as min
from pelican import signals


# We need save unicode strings to files.
try:
    from codecs import open
except ImportError:
    pass

logger = getLogger(__name__)


def minify_html(pelican):
    """Minify all HTML files.

    :param pelican: The Pelican instance.
    """
    for dirpath, _, filenames in walk(pelican.settings['OUTPUT_PATH']):
        for name in filenames:
            if name.endswith('.html') or name.endswith('.htm'):
                filepath = join(dirpath, name)
                create_minified_file(filepath)


def create_minified_file(filename):
    """Create a minified HTML file, overwriting the original.

    :param str filename: The file to minify.
    """
    uncompressed = open(filename, encoding='utf-8').read()
    with open(filename, 'w', encoding='utf-8') as f:
        try:
            logger.debug('Minifying: %s' % filename)
            compressed = min(uncompressed, remove_comments=True,
                             remove_all_empty_space=True,
                             remove_empty_space=True)
            f.write(compressed)
        except Exception as ex:
            logger.critical('HTML Minification failed: %s' % ex)
        finally:
            f.close()


def register():
    """Run the HTML minification stuff after all articles have been generated,
    at the very end of the processing loop.
    """
    signals.finalized.connect(minify_html)
