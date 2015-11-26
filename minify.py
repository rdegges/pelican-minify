"""A Pelican plugin which minifies HTML pages."""


from logging import getLogger
from os import walk
from os.path import join

from htmlmin import minify
from pelican import signals
from joblib import Parallel, delayed

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
    options = pelican.settings.get('MINIFY', {})
    files_to_minify = []

    for dirpath, _, filenames in walk(pelican.settings['OUTPUT_PATH']):
        files_to_minify += [join(dirpath, name) for name in filenames if name.endswith('.html') or name.endswith('.htm')]

    Parallel(n_jobs=-1)(delayed(create_minified_file)(filepath, options) for filepath in files_to_minify)


def create_minified_file(filename, options):
    """Create a minified HTML file, overwriting the original.

    :param str filename: The file to minify.
    """
    uncompressed = open(filename, encoding='utf-8').read()

    with open(filename, 'w', encoding='utf-8') as f:
        try:
            logger.debug('Minifying: %s' % filename)
            compressed = minify(uncompressed, **options)
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
