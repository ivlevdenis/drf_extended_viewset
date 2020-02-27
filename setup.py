#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['djangorestframework>=3.10']

setup_requirements = ['pytest-runner',]

test_requirements = ['pytest>=3', 'djangorestframework>=3.10']

setup(
    author="Denis Ivlev",
    author_email='me@dierz.pro',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Django Rest Framework extension for implement by action serializers, permissions & /etc",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='drf_extended_viewset',
    name='drf_extended_viewset',
    packages=find_packages(include=['drf_extended_viewset', 'drf_extended_viewset.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivlevdenis/drf_extended_viewset',
    version='0.1.1',
    zip_safe=False,
)
