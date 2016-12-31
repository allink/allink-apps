#! /usr/bin/env python
from setuptools import setup
from . import __version__ as version

VERSION = (0, 0, 1)
__version__ = '.'.join(map(str, VERSION))


setup(
    name='allink_apps',
    version=version,
    description='collection of common apps',
    long_description='collection of common apps',
    author='Florian Türler, Beat Schenkel',
    author_email='itcrowd@allink.ch',
    url='http://github.com/allink/allink-core/',
    license='BSD License',
    platforms=['OS Independent'],
    packages=[
        'people',
        'testimonials',
        'work',
    ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Communications :: Email',
    ],
    requires=[
    ],
    include_package_data=True,
)