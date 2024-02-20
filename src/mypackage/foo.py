from .subpackage import subfoo


def add(a: int, b: int) -> int:
    diff = subfoo.sub(a, b)
    print(f"diff is: {diff}")
    return a + b
