import collections
import book
import util

class FileIO:

    def load_level_vocab(self, reading_level: int):
        utils = util.Util()
        level_appropriate_words = {}

        # level-appropriate words include all levels UP to the one passed in
        for i in range(0, reading_level + 1):
            words_file = open("words_" + str(i) + ".txt")
            for line in words_file:
                if len(line) > 1 and not line.startswith("@"):
                    # skip processing empty and copyright lines
                    words_trimmed_spaces = line.replace("  ", " ")
                    words = words_trimmed_spaces.split(" ")
                
                    for word in words:
                        level_appropriate_words[utils.stem(word)] = utils.stem(word)

        return level_appropriate_words

    def load_cbt_train_data(self):
        all_books = {}
        new_book = book.Book()

        cbt_file = open("CBTest/data/cbt_train.txt")
        for line in cbt_file:
            if line.startswith("_BOOK_TITLE_"):
                # skip the very beginning of the file - no book data yet
                if len(new_book.book_title) > 0:
                    all_books[new_book.book_title] = book.Book()
                    all_books[new_book.book_title].book_title = new_book.book_title
                    all_books[new_book.book_title].book_text = new_book.book_text
                    
                # start a new book
                new_book_title = line.replace("_BOOK_TITLE_ : ", "")
                new_book.book_title = new_book_title.rstrip()
                new_book.book_text = []

            else:
                #keep appending to book
                new_book.book_text.append(line)

        return all_books
