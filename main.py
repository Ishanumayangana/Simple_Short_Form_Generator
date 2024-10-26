
def generator(full_sentence):
    words = full_sentence.split()  # can get word separately
    short_form = ""
    for i in words:
        short_form = short_form + i[0].upper()

    print(short_form)


sentence = input("Enter your sentence :")
generator(sentence)



