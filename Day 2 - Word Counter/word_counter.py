sentence = input(f"\nEnter sentence: ")

def count_words(sentence):
    sentence = sentence.count(' ')
    return sentence

word_count = (count_words(sentence) + 1)

print(f"Word Count: {word_count}")