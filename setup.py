"""Setup script for ``alignparse``."""


import re
import sys

from setuptools import setup


if not (sys.version_info[0] == 3 and sys.version_info[1] >= 6):
    raise RuntimeError(
                'alignparse requires Python >=3.6.\n'
                f"You are using {sys.version_info[0]}.{sys.version_info[1]}.")

# get metadata from package `__init__.py` file as here:
# https://packaging.python.org/guides/single-sourcing-package-version/
metadata = {}
init_file = 'alignparse/__init__.py'
with open(init_file) as f:
    init_text = f.read()
for dataname in ['version', 'author', 'email', 'url']:
    matches = re.findall(
            '__' + dataname + r'__\s+=\s+[\'"]([^\'"]+)[\'"]',
            init_text)
    if len(matches) != 1:
        raise ValueError(f"found {len(matches)} matches for {dataname} "
                         f"in {init_file}")
    else:
        metadata[dataname] = matches[0]

with open('README.rst') as f:
    readme = f.read()

# main setup command
setup(
    name='alignparse',
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    download_url='https://github.com/jbloomlab/alignparse/tarball/' +
                 metadata['version'],  # tagged version on GitHub
    description='Align sequences and then parse features.',
    long_description=readme,
    license='GPLv3',
    install_requires=[
            'biopython>=1.73',
            'dna_features_viewer>=1.0.0',
            'matplotlib>=3.0.0',
            'numpy>=0.13',
            'packaging',
            'plotnine>=0.5.1',
            'pysam>=0.13',
            ],
    platforms='Linux and Mac OS X.',
    packages=['alignparse'],
    package_dir={'alignparse': 'alignparse'},
)
