#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comprendre.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    IS_TESTING = 'test' in sys.argv

    # Coverage needs to start before tests running.
    if IS_TESTING:
        import coverage
        COV = coverage.coverage(source=['comprendre.users', 'comprendre.meetings'])
        COV.erase()
        COV.start()

    # Normal command execution.
    execute_from_command_line(sys.argv)

    if IS_TESTING:
        COV.stop()
        COV.save()
        if COV.report() < 100:
            # If code is not 100% covered, we should return error code.
            sys.exit(1)


if __name__ == '__main__':
    main()
