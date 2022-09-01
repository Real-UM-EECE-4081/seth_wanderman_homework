print("Question 10")
from collections import Counter
def word_count(Homework1):
    with open(Homework1) as fn:
        return Counter(fn.read().split())
print("The number of words in the file :", word_count("Homework1.txt"))