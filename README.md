## eh?

Fez is a cool video game. It came out a couple of years ago, but I'm just now getting around to it. There are some really hard puzzles in the game. One of those puzzles gives you a clue and asks you to spell out a word using blocks. The clue is:

> My first half is what it is.
> My second half is half of what made it.
> What is my name?

To spell out the answer, you are given eight blocks, each of which has four letters printed on it. You can place the blocks in any order and orientation. This means there are a LOT of possible inputs. Way too many to just trial and error.

So, I decided to make a computer program that could generate all of the possible English language words I could make with those blocks. This cut the choice space down to just 131 words:

> albanite
> alkannin
> althaein
> anaunter
> anhaline
> annaline
> annulate
> antilens
> antliate
> arbutean
> argenton
> atabrine
> atheling
> atonable
> attacher
> attainer
> babelish
> bailment
> balanite
> banisher
> banister
> banxring
> bareboat
> bartizan
> baseborn
> bathorse
> blanking
> blankish
> bleating
> blennoma
> boatable
> bokharan
> bombable
> brineman
> buttress
> calanthe
> earthian
> embright
> eranthis
> faineant
> fennoman
> fontange
> gantline
> gauntlet
> ghostlet
> guttable
> habenula
> habutaye
> hanafite
> harbinge
> hatteria
> hearting
> hebraist
> henhussy
> hornbeam
> huntress
> hushable
> ingather
> instable
> intermat
> kashruth
> knorhaan
> latinate
> libament
> linenman
> linnaean
> marennin
> martinet
> merchant
> mobbable
> nabalite
> nebalian
> negatron
> nembutal
> neonatal
> nestling
> nobleman
> nonmetal
> numerant
> onhanger
> ornament
> rabatine
> reactant
> reattach
> reattain
> rebanish
> resnatch
> resonant
> rhaetian
> rhamnite
> rheostat
> schnabel
> sebright
> settling
> sheraton
> sinnable
> snatcher
> srikanth
> stanchel
> stancher
> sternson
> stonable
> straiten
> sunsetty
> tabulate
> tachygen
> tactable
> tangency
> tangible
> teatfish
> teatling
> tertiana
> testator
> tetragon
> tetramin
> tintless
> tormenta
> trachean
> tractate
> transect
> treating
> tristate
> turngate
> unbreast
> unfasten
> unmanner
> unmantle
> unmental
> unstable
> untangle
> yeshibah


## Result

As it turns out, the answer is not in this list, because it is a proper noun and not in my computer's dictionary. But I thought this program was interesting enough to share anyway. These words are also pretty interesting. A lot of them are new to me.


## The code

* `fez_solver.py` -- run this to actually execute the program. Each block in the game is represented by one row in the `blocks` list, and each item in each list is one face of each block.

* `treewords.py` -- Treewords is basically a spell-checker built out of the words list Unix systems have at `/usr/share/dict/words`. It generates a tree out of the list to allow fast searching and also the ability to check whether or not a given string is the first part of a word, even if it is not itself a word.

* `jumbler.py` -- Jumbler uses Treewords to check every possible path through every possible permutation of the letter blocks graph. It is fast because it short-circuits whenever it reaches a node that is not a partial word, so it doesn't have to check every single thing.

* `test_treewords.py` and `test_jumbler.py` -- unit test files

