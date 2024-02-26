import mypackage.foo as foo
from mypackage.subpackage import subfoo


def myfunc() -> None:
    print("running foobar.py")
    print(foo.add(1, 1))
    print(subfoo.sub(5, 2))


if __name__ == "__main__":
    myfunc()
