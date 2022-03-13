import unittest

class failTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_failing(self):
        self.assertTrue(True)