import unittest

from mypackage import foobar


class TestMain(unittest.TestCase):
    def test_foobar_myfunc(self) -> None:
        self.assertIsNone(foobar.myfunc())


if __name__ == "__main__":
    unittest.main()
