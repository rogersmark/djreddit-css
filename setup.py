import os
from setuptools import setup, find_packages

setup(
    name = "djreddit_css",
    version = "0.1",
    author = "Mark Rogers",
    author_email = "f4nt@f4ntasmic.com",
    url = "http://www.f4ntasmic.com",

    packages = find_packages('.'),
    package_dir = {'':'.'},
    data_files=[('.', ['README.rst','MANIFEST.in']),],
    package_data = {
        'djreddit_css':
        ['templates/*.html',
        'templates/djreddit_css/*.html'
        ],
    },
    include_package_data=True,

    keywords = "django reddit css",
    description = "Populates CSS for SubReddits that use Custom CSS",
    install_requires=[
    ],
    classifiers = [
        "Intended Audience :: Developers",
        'Programming Language :: Python',
    ]
)
