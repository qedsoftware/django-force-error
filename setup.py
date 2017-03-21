#!/usr/bin/env python
from distutils.core import setup


setup(
    name='django-force-error',
    version='1.0.0b1',
    description=(
        'Ready to use Django views that produce errors for testing your error'
        ' reporting.'
    ),
    author='Quantitative Engineering Design Inc.',
    author_email='info@qed.ai',
    url='https://qed.ai/',
    packages=['force_error'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
    install_requires=[
        "django"
    ]
)
