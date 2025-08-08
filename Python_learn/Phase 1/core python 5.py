
def count_words(sentence):
    text = sentence.split()
    print("number of words =", len(text))

def get_vowel_count(sentence):
    vowels = 0
    for letter in sentence:
        if letter.lower() in "aeiou":
            vowels = vowels + 1
    print(vowels)

def reverse_letters(sentence):
     print(sentence[::-1])

def reverse_words(sentence):
    text = sentence.split() 
    print(" ".join(text[::-1]))

def longest_word(sentence):
     text = sentence.split()
     print(max(text, key=len))


sentence = input("enter sentence")
count_words(sentence)
get_vowel_count(sentence)
reverse_letters(sentence)
reverse_words(sentence)
longest_word(sentence)
