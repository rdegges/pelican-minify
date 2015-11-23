from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'pelican-minify',
    version = '0.9',
    py_modules = ('minify',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['htmlmin>=0.1.5', 'pelican>=3.1.1', 'joblib>=0.9'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/pelican-minify',
    keywords = 'pelican blog static minify html minification',
    description = ('An HTML minification plugin for Pelican, the static '
            'site generator.'),
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
