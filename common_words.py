def count_words_in_a_book() :
    '''Function that counts how many times a certain word appears in a book.'''

    books_to_read = ['text-files\The_Odyssey.txt', 'text-files\Don_Quixote.txt', 'text-files\The_picture_of_Dorrian_Gray.txt',
                    'text-files\Strange_case_of_Dr_jekyl.txt']

    try :
        for book in books_to_read :
            with open(book, 'r', encoding='UTF-8') as book_object :
                words = book_object.read()
                print(words.count('the'))
                

    except FileNotFoundError :
        print('The file ' + book + ' does not exist. ')
        #pass

count_words_in_a_book()