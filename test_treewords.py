from unittest import TestCase

from treewords import Treewords


class TreewordsTest(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.t = Treewords()

	def test_it_loads_words_into_a_tree(self):
		self.assertTrue(self.t.tree['c'])
		self.assertTrue(self.t.tree['c']['a'])
		self.assertTrue(self.t.tree['c']['a']['t'])
		self.assertTrue('\0' in self.t.tree['c']['a']['t'])

	def test_it_loads_the_whole_damn_dictionary(self):
		self.assertTrue('\0' in self.t.tree['z']['y']['g']['o']['t']['e'])

	def test_fake_words_dont_have_the_terminal_key(self):
		self.assertFalse('\0' in self.t.tree['m']['a']['r']['b']['l'])

	def test_it_can_tell_you_if_a_string_is_a_word(self):
		word = "tree"
		self.assertTrue(self.t.is_word(word))

	def test_it_short_circuits_as_soon_as_it_knows_it_isnt_a_word(self):
		fake_word = "abzq"
		self.assertFalse(self.t.is_word(fake_word))

	def test_it_can_tell_you_if_youre_maybe_a_word(self):
		maybe_word = "tre"
		self.assertTrue(self.t.maybe_is_word(maybe_word))

	def test_it_can_tell_you_if_you_fail_the_maybe_test(self):
		maybe_word = "trez"
		self.assertFalse(self.t.maybe_is_word(maybe_word))
