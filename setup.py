#!/usr/bin/env python3

from setuptools import setup


setup(
    name='passpy',
    version='0.9',
    description='ZX2C4\'s pass compatible Python library and cli',
    url='https://github.com/bfrascher/passpy',
    author='Benedikt Rascher-Friesenhausen',
    author_email='benediktrascherfriesenhausen+passpy@gmail.com',
    license='GPLv3+',
    packages=['passpy'],
    install_requires=[
        'python-gnupg>=0.3.8',
        'GitPython>=1.0.1',
        'pyperclip>=1.5',
        'click>=2.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: GPLv3+',
        'Programming Language :: Python :: 3.5',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ],
    entry_points='''
        [console_scripts]
        passpy=passpy.__main__:cli
    ''',
)
