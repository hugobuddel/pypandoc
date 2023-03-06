#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pypandoc
import io
from setuptools import setup

with io.open('README.md', encoding="utf-8") as f:
    long_description = f.read()

module = pypandoc
setup(
    name='pypandoc',
    version=module.__version__,
    url=module.__url__,
    license=module.__license__,
    description=module.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=module.__author__.encode('utf8'),
    author_email=module.__author_email__,
    packages=['pypandoc'],
    python_requires=module.__python_requires__,
    setup_requires=module.__setup_requires__,
    classifiers=module.__classifiers__,
    test_suite='tests',
)
