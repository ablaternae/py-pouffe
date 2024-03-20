# =============================================================================
#
# =============================================================================


from ..options import hash, tripcode

import sortedcontainers

Containers = sortedcontainers
Collection = sortedcontainers.SortedDict


try:
    from setuptools.extern.jaraco.text import WordSet

    def make_snake_case(s):
        return WordSet.parse(s).lowered().underscore_separated()

    def make_camel_case(s):
        return WordSet.parse(s).camel_case()  # headless_camel_case()

except ImportError:
    from peewee import make_snake_case

    def make_camel_case(s):
        import re

        return re.sub(r"\w+", lambda m: m.group(0).capitalize(), s)


__all__ = ("hash", "tripcode", "make_snake_case", "make_camel_case")
