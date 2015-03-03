http://en.wikipedia.org/wiki/Blotto_games

To be played at the MathSpace event on 6th March, https://wiki.london.hackspace.org.uk/view/Group:MathSpace

Download the code and start writing your own strategy or additions to the codebase.
Please push anything you work on! Post on the mailing list (https://groups.google.com/forum/#!forum/lhs-mathspace) with any questions.

To get started, copy SimpleStrategy and rename it to your own strategy name in the same directory.
The basic task is to implement soldiers_request which is where you decide your move on each turn.
Simple examples to look at:
 - StaticStrategy
 - CopierStrategy

On the night we will start by battling 100 soldiers, across 8 fields, and 10,000 runs.
The winner will be the one that wins the most games over all 10,000 runs, i.e. a max score of 10,000.
People might mess around with other setups afterwards. Suggestions of weighted field values or more/less soldiers/fields

Uses:

 - python2.7
 
 Optional:
 - matplotlib (sudo apt-get install python-matplotlib on linux or equivalent elsewhere)
 - numpy (sudo apt-get install python-numpy on linux or equivalent elsewhere)
 - progressbar (sudo pip install progressbar on linux or equivalent elsewhere)
