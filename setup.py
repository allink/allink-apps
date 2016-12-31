#! /usr/bin/env python
from setuptools import setup

import allink_apps
setup(
    name='allink_apps',
    version=allink_apps.__version__,
    description='collection of common apps',
    long_description='collection of common apps',
    author='Florian Türler, Beat Schenkel',
    author_email='itcrowd@allink.ch',
    url='http://github.com/allink/allink-core/',
    license='BSD License',
    platforms=['OS Independent'],
    packages=[
        'allink_apps',
        'allink_apps.people',
        'allink_apps.testimonials',
        'allink_apps.work',
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