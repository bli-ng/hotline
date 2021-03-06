# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hotline',
    version='0.1.0',

    description='Session Manager',
    long_description=long_description,

    url='https://github.com/bli-ng/hotline',

    author='bli-ng',
    #author_email='',

    license='ISC',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='session manager',

    packages=find_packages(),

    install_requires=[],
)
