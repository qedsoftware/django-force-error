# Django force error

1. Add `force_error` to your `INSTALLED_APPS`.
2. Add this to your `urls.py`.

    url(r'^force_error/', include('force_error.urls')),

3. Go to `/force_error/error/` for a generic uncaught exception or to
   `/force_error/permission_denied/`.
