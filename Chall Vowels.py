#start function
def only_vowels(string):
   my_vowels = ['a','e','i','o','u']
#transform string no.1 into a list
  string_one = list(string)
  new_list = [e for e in string_one if e in my_vowels]
#change new_list into tuple
  changed_list = tuple(new_list)
#function OrderedDict.from keys() should be used to remove duplicates
  remove_duplicates = ''.join(OrderedDict.fromkeys(new_list))
  generate_vowels = (remove_duplicates,)
#quantify duplicates in the original string
  quantified_duplicates = [letter for letter in string if string.count(letter) > 1]
  new_vowel_e = ''.join(OrderedDict.fromkeys(quantified_duplicates))
  generate_tuple_for_duplicates = tuple(new_vowel_e)
  quantified_duplicates_in_generated_tuple = len(generate_tuple_for_duplicates)
  last_quantity = (quantified_duplicates_in_generated_tuple,)
  last_tuple_generated = generate_vowels + last_quantity
  print(last_tuple_generated)