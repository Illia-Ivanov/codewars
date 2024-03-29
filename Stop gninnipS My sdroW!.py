def spin_words(sentence):
    sen = sentence.split()
    for i, word in enumerate(sen):
        if len(word) >= 5:
            sen[i] = word[::-1]
        else:
            sen[i] = word[:]
    res = " ".join(sen)
    return res


result = spin_words("Hey Billiger jonny")
print(result)