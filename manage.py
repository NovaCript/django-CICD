#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from typing import List

def main() -> None:
    """Run administrative tasks.

    This function sets the DJANGO_SETTINGS_MODULE environment variable,
    imports Django's core management module, and executes the command
    specified in the command line.

    Raises:
        ImportError: If Django is not installed or available on the
            PYTHONPATH environment variable.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
