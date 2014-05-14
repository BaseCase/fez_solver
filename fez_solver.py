from jumbler import Jumbler
from treewords import Treewords


blocks = [
    ['g', 'm', 's', 'a'],
    ['t', 'n', 'h', 'b'],
    ['z', 'q', 'e', 'x', 'k'],
    ['m', 's', 'a', 'g'],
    ['t', 'n', 'h', 'b'],
    ['v', 'o', 'i', 'c', 'u'],
    ['n', 'h', 'b', 't'],
    ['r', 'l', 'f', 'y']
]

checker = Treewords()
j = Jumbler(checker, blocks, True)

words = j.get_all_words()

for word in sorted(words):
    print word

