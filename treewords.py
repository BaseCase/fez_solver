class Treewords:
    def __init__(self):
        with open('/usr/share/dict/words') as f:
            words = [w.strip().lower() for w in f.readlines()]
        self._generate_tree(words)


    def _generate_tree(self, words):
        self.tree = {}
        for word in words:
            parent = self.tree
            for letter in word + '\0':
                if letter in parent:
                    pass
                else:
                    parent[letter] = {}
                parent = parent[letter]


    def is_word(self, word):
        parent = self.tree
        for letter in word + '\0':
            if letter == '\0':
                return True
            if letter in parent:
                parent = parent[letter]
            else:
                return False


    def maybe_is_word(self, word):
        parent = self.tree
        for letter in word:
            if letter in parent:
                parent = parent[letter]
            else:
                return False
        return True

