import ex25 #imports all methods written in this file
from ex25 import break_words #imports specific method from this file
from ex25 import * #imports all functions from the method

sentence = "All good things come to those who wait"
words = break_words(sentence)  #refers to method within the file
print words

sorted_words = ex25.sort_words(words)
print sorted_words

ex25.print_first_word(words)

ex25.print_last_word(words)

print words #after words have been popped off the array they are no longer there

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)
