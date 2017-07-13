def read_text():
    quotes = open(r'C:\Dev\udacity\programming_foundations_with_python\5_use_classes_profanity_editor\movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
