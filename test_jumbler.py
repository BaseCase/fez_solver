from unittest import TestCase

from jumbler import Jumbler
from treewords import Treewords


class JumblerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.j = Jumbler(Treewords(), [])

    def test_base_case(self):
        rows = [['a', 'i', 'z']]
        self.j.groups = rows
        words = self.j.get_all_words()
        self.assertEqual(['a', 'i', 'z'], words)

    def test_permutations(self):
        rows = [
            ['c'],
            ['t'],
            ['a']
        ]
        self.j.groups = rows
        words = self.j.get_all_words()
        self.assertEqual(['act', 'cat'], words)

    def test_complicated_case(self):
        rows = [
            ['a','z','z'],
            ['z','t','s', 'a']
        ]

        self.j.groups = rows

        words = self.j.get_all_words()
        self.assertEqual(['aa', 'za', 'as', 'at', 'sa', 'ta'], words)

