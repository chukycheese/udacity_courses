def read_text():
    quotes = open(r'C:\Dev\udacity\programming_foundations_with_python\5_use_classes_profanity_editor\movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

    check_profanity(contents_of_file)

# In Python 3, urllib is sperated into three parts; request, parse, and error
from urllib.request import urlopen
from urllib.parse import quote          # converts regular strings into bytes

def check_profanity(text_to_check):
    converted = quote(text_to_check)
    connection = urlopen("http://www.wdylike.appspot.com/?q=" + converted)
    output = connection.read()
    print(output)
    connection.close()

read_text()
