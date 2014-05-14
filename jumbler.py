from itertools import permutations

import math


class Jumbler:
    def __init__(self, spell_checker, groups, logging=False):
        self.logging = logging
        self.spell_checker = spell_checker
        self.groups = groups

    def get_all_words(self):
        total_perms = math.factorial(len(self.groups))
        current_perm = 1
        words = []

        for ordering in permutations(self.groups):
            if self.logging: print "finding words for ordering {0} out of {1}".format(current_perm, total_perms)
            current_perm += 1
            words += self.look_for_words(ordering)
        return list(set(words))

    def look_for_words(self, groups):
        self.found_words = []
        self.dsf(groups[0], groups[1:], "")
        return self.found_words


    def dsf(self, head, tail, word_so_far):
        if not tail: # base case. we're on the bottom row
            for letter in head:
                if self.is_word(word_so_far + letter):
                    self.found_words.append(word_so_far + letter)
        else: # non-base case. short-circuit if maybe word check fails
            for letter in head:
                if not self.maybe_is_word(word_so_far + letter):
                    continue
                else:
                    self.dsf(tail[0], tail[1:], word_so_far + letter)


    def is_word(self, candidate):
        return self.spell_checker.is_word(candidate)


    def maybe_is_word(self, candidate):
        return self.spell_checker.maybe_is_word(candidate)

