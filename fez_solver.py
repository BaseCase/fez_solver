from jumbler import Jumbler
from treewords import Treewords


blocks = [
    ['g', 'm', 's', 'a'],
    ['t', 'n', 'h', 'b'],
    ['z', 'q', 'e', 'x', 'k'], # in the Fez alphabet, 'x' and 'k' are represented by the same character
    ['m', 's', 'a', 'g'],
    ['t', 'n', 'h', 'b'],
    ['v', 'o', 'i', 'c', 'u'], # in the Fez alphabet, 'v' and 'u' are represented by the same character
    ['n', 'h', 'b', 't'],
    ['r', 'l', 'f', 'y']
]

checker = Treewords()
j = Jumbler(checker, blocks, True)

words = j.get_all_words()

for word in sorted(words):
    print word

