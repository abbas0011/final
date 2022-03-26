print("Halo")


def add_num(a,b):
    result = a+b
    return result

print(add_num(3,5))


sentence = "This is my company"
words = sentence.split()

#print(words)

#for word in words:
    #word.title()
#print(words)
#print([word.title() for word in words])

def harshtag(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        newword = word
        new_words.append(newword)
    joined_word = ''.join(new_words)
    return '#'+joined_word 
print(harshtag(sentence))