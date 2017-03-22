#!/usr/bin/env python
import django
from django.conf import settings
from django.test.runner import DiscoverRunner


def main():
    settings.configure(
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'force_error'
        ],
        DATABASES={'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }}

    )
    django.setup()

    test_runner = DiscoverRunner(verbosity=1)
    test_runner.run_tests(['force_error'])

if __name__ == '__main__':
    main()
