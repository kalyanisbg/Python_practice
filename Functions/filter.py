'''
We were given a list of lists, where each sublist holds the title of a famous 
book that has a year as its title and the last name of the author that wrote 
the book. Unfortunately, when this list was made, each of the books was 
accidentally entered twice—once with the title as a numeric value and once 
with the title as a string. Use the filter() function to deduplicate the list 
and keep only the sublists that have the book title stored as a string:
books = [["Burgess", 1985],
 ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
   ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
     ["Murakami", 1985]]
'''

books = [["Burgess", 1985],
 ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
   ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
     ["Murakami", 1985]]


def title_as_string(entry):
    return type(entry[1]) is str


string_titles = filter(title_as_string, books)
string_titles_list = list(string_titles)
print(string_titles_list)