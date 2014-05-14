from unittest import TestCase

from jumbler import Jumbler
from treewords import Treewords


class JumblerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.j = Jumbler(Treewords(), [])

    def pend_base_case(self):
        rows = [['a', 'i', 'z']]
        self.j.groups = rows
        words = self.j.get_all_words()
        self.assertEqual(['a', 'i'], words)

    def test_complicated_case(self):
        rows = [
            ['a','z','z'],
            ['z','t','s', 'a']
        ]

        self.j.groups = rows

        # ragged edge: we're getting a false positive here
        # due to a bug in Treewords

        words = self.j.get_all_words()
        self.assertEqual(['at', 'as', 'za'], words)

