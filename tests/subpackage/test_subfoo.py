import unittest

from mypackage.subpackage import subfoo


class TestMain(unittest.TestCase):
    def test_sub_1(self) -> None:
        self.assertEqual(subfoo.sub(0, 0), 0)

    def test_sub_2(self) -> None:
        self.assertEqual(subfoo.sub(-1, 1), -2)


if __name__ == "__main__":
    unittest.main()
