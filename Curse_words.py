from csv import reader
import string

def func(msg):
    sentence = msg.split(" ")

    if msg == None:
        return False

    with open('curse_words.csv', 'r') as read:
        next_word = False
        csv_reader = reader(read)
        for items in csv_reader:
            for true_word in sentence:
                for item in items:
                    word = ''
                    next_word = False
                    bad_word = str(item.lower()[1:])
                    true_word = true_word.lower()
                    word = true_word
                    previous_letter_index = 0

                    for j in range(len(bad_word)):
                        if true_word.find(bad_word[j]) == -1:
                            next_word = True

                        if true_word.count(bad_word[j]) < bad_word.count(bad_word[j]):
                            next_word = True

                        if previous_letter_index > true_word.find(bad_word[j]):
                            next_word = True

                        previous_letter_index =  true_word.find(bad_word[j])

                    if next_word == False:
                        for k in string.punctuation:
                            word = word.replace(k, '')

                        for i in range(len(bad_word)):
                            bad_word_letter_index = word.find(bad_word[i])    

                            if bad_word_letter_index != -1:
                                word = word.replace(word[bad_word_letter_index],'')

                            if bad_word[i] != '':   
                                if word == '':
                                    return True
                                    

print(func(""))