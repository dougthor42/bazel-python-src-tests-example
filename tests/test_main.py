import unittest

from myproject import main


class TestMain(unittest.TestCase):
    def test_add_1(self) -> None:
        assert main.add(0, 0) == 0

    def test_add_2(self) -> None:
        assert main.add(-1, 1) == 0


if __name__ == "__main__":
    unittest.main()
