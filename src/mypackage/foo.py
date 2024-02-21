# N.B.: It seems like gazelle doesn't really like relative imports yet.
# So don't do `from .subpackage import subfoo` or else it won't get the dep
# tree correct. Or maybe I'm doing something wrong?
from mypackage.subpackage import subfoo

import pathspec

_ = pathspec


def add(a: int, b: int) -> int:
    diff = subfoo.sub(a, b)
    print(f"diff is: {diff}")
    return a + b
