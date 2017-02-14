import urllib

def read_txt():
    # since "open returns an object of the file type"
    # then quotes is an instance/object of File class (built into base python lib since didn't import anything)
    # quotes = open(r"/Users/jasonsimpson/Dropbox/Dev/python_intro_course/movie_quotes/movie_quotes.txt")
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    print ("")
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
        print ("This document has no curse words!")
    else:
        print ("Could not scan the document properly")

read_txt()