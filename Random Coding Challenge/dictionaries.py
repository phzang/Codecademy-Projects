"""Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and
values, as a parameter. This function should return the sum of the values of all even keys."""

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

"""Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter.
The function should add 10 to every value in my_dictionary and return my_dictionary"""

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary:
    my_dictionary[key] += 10
    
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

"""Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter.
This function should return a list of all values in the dictionary that are also keys."""

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  v_list = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      v_list.append(value)
  
  return v_list
    
  
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The
function should return the key associated with the largest value in the dictionary."""

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = ""
  largest_value = float("-inf")
  
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_key = key
      largest_value = value
      
  return largest_key
  
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

"""Write a function named word_length_dictionary that takes a list of strings named words as a
parameter. The function should return a dictionary of key/value pairs where every key is a word in words
and every value is the length of that word. """

# Write your word_length_dictionary function here:

def word_length_dictionary(words):
  tmp_dict = {}
  for word in words:
    tmp_dict[word] = len(word)
  
  return tmp_dict

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

"""Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
The function should return a dictionary containing the frequency of each element in words."""

# Write your frequency_dictionary function here:

def frequency_dictionary(words):
  tmp_dict = {}
  for word in words:
    if word not in tmp_dict:
      tmp_dict[word] = 1
    else:
      tmp_dict[word] += 1
      
  return tmp_dict
      

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

"""Create a function named unique_values that takes a dictionary named my_dictionary as a parameter.
The function should return the number of unique values in the dictionary."""

# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
      
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


"""Create a function named count_first_letter that takes a dictionary
named names as a parameter. names should be a dictionary where the key
is a last name and the value is a list of first names.

The function should return a new dictionary where each key is the first
letter of a last name, and the value is the number of people whose last name
begins with that letter."""

# Write your count_first_letter function here:
def count_first_letter(names):
    letters = {}
      
    for key in names.keys():
        if key[0] not in letters:
            letters[key[0]] = len(names[key])
        else:
            letters[key[0]] += len(names[key])

    return letters                                      
      

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
