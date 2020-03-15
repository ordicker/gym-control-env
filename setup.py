import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="gym-control-env",
    version="0.1.0",
    url="git@github.com:ordicker/gym-control-env.git",
    license='MIT',

    author="Or Dicker",
    author_email="or.dicker@gmail.com",

    description="Extension for OpenAI Gym environments and benchmarks",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        'gym>=0.10,<1'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
