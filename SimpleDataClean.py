#Program: SimpleDataClean
#Written by: Lee Friend
#Date: 06/10/2020

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]


def strip_characters(string1):
    for char in bad_chars:
        string1 = string1.replace(char,"")
    return string1

stripped_test_data = []

for datestring in test_data:
    newstring = strip_characters(datestring)
    stripped_test_data.append(newstring)

print (stripped_test_data)