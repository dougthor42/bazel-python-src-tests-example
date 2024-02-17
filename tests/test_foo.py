import unittest

from mypackage import foo


class TestMain(unittest.TestCase):
    def test_add_1(self) -> None:
        self.assertEqual(foo.add(0, 0), 0)

    def test_add_2(self) -> None:
        self.assertEqual(foo.add(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
