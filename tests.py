from contextlib import contextmanager
from shutil import rmtree
from tempfile import mkdtemp, mkstemp
from unittest import TestCase, main

from minify import create_minified_file


@contextmanager
def temporary_folder():
    """Creates a temporary folder, return it and delete it afterwards.

    This allows to do something like this in tests:

        >>> with temporary_folder() as d:
            # do whatever you want
    """
    tempdir = mkdtemp()
    try:
        yield tempdir
    finally:
        rmtree(tempdir)


class TestMinify(TestCase):

    def test_create_minified_file(self):
        """Test that a file matching the input filename is compressed."""
        with temporary_folder() as tempdir:
            (_, a_html_filename) = mkstemp(suffix='.html', dir=tempdir)
            f = open(a_html_filename, 'w')
            f.write('   <html>   <head></head>  <body>hi</body>   </html>        ')
            f.close()
            create_minified_file(a_html_filename, {'remove_all_empty_space': True})
            self.assertEqual(open(a_html_filename).read(), '<html><head></head><body>hi</body></html>')


if __name__ == '__main__':
    main()
