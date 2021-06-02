#main, "driver" class
import fileIO
import util

def __init__():
    utils = util.Util()
    file_io = fileIO.FileIO()
    train_data = file_io.load_cbt_train_data()
    
    k_lvl = file_io.load_level_vocab(0)

    book_title = "Lewis_Carroll___Alice's_Adventures_Under_Ground.txt.out"
    # unaltered training text
    print("BOOK TITLE xxx'" + str(book_title) + "'xxx")
    print("BOOK TEXT " + str(train_data[book_title].book_text))
    print("Total length " + str(sum(len(word) for word in train_data[book_title].book_text)))

    # removed all words but the k-level (stemmed) and kept all the capitalized words as named entities
    leveled_book_text = []
    for sentence in train_data[book_title].book_text:
        leveled_sentence = ""
        for word in sentence.split():
            if utils.stem(word) in k_lvl or word[0].isupper():
                 leveled_sentence += word + " "
        leveled_book_text.append(leveled_sentence)

    train_data[book_title].book_text = leveled_book_text
    print("LEVELED BOOK TITLE xxx'" + str(book_title) + "'xxx")
    print("LEVELED BOOK TEXT " + str(train_data[book_title].book_text))
    print("LEVELED Total length " + str(sum(len(word) for word in train_data[book_title].book_text)))

__init__()

#k: LEVELED Total length 48372
#1: 