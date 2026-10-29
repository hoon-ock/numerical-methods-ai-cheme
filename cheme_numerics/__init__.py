"""Shared helpers for the course book.

Chapters import from here instead of re-defining plotting styles, constants, or
small utilities in every notebook. Keeping them in one installed package means a
change propagates to every chapter on the next build.
"""

from .plotting import use_course_style, COLORS

__all__ = ["use_course_style", "COLORS"]
__version__ = "0.1.0"
