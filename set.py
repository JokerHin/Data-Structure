sets={1,2,3}
sets.add(4)
sets.discard(5)
sets.discard(2)
print(5 in sets)
print(sets)

def count_unique_word(text):
    words = text.split()
    unique_word = set(words)
    return len(unique_word)

text_input = ("Python is a high-level programming language. "
              "Python's simplicity and flexibility make it a popular programming language. "
              "Learning Python is essential for mastering web development, data science, and automation tasks.")

print("Number of unique words:", count_unique_word(text_input))
