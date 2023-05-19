# Given a number, convert it into the words representing that number
# e.g. 123 > one hundred and twenty three
# The number will be any between 0 and 999

# Additional Task: Increase max to 9999
# Additional Task: Decimal numbers
# Additional Task: Negative numbers

# SO BAD MAKE BETTER

unit_to_word_dict = {'1': 'one', '2': 'two', '3': 'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

tens_to_word_dict = {'1': 'ten', '2': 'twenty', '3': 'thirty', '4':'fourty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

edge_case_to_word_dict = {'11': 'eleven', '12': 'twelve'}


def num_to_words(num:int) -> str:
  if num == 0:
    return 'zero'
    
  if num == 11:
    return edge_case_to_word_dict['11']
  if num == 12:
    return edge_case_to_word_dict['12']
  if num == 10:
    return tens_to_word_dict['1']
    
  if len(str(num)) == 3:
    hundreds = unit_to_word_dict[str(num)[0]]
    if str(num)[-2:] == '11':
      tens = edge_case_to_word_dict['11']
      return f"{hundreds} hundred and {tens}"
    if str(num)[-2:] == '12':
      tens = edge_case_to_word_dict['12']
      return f"{hundreds} hundred and {tens}"
    if str(num)[-2:] == '10':
      tens = tens_to_word_dict['1']
      return f"{hundreds} hundred and {tens}"
    
    else:  
      tens = tens_to_word_dict[str(num)[1]]
    if str(num)[2] == '0':
      return f"{hundreds} hundred and {tens}"
    units = unit_to_word_dict[str(num)[2]]
    return f"{hundreds} hundred and {tens} {units}"

  if len(str(num)) == 2:
    if str(num)[0] != '1':
      tens = tens_to_word_dict[str(num)[0]]
      if str(num)[1] == '0':
        return f"{tens}"
      units = unit_to_word_dict[str(num)[1]]
      return f"{tens} {units}"

    if num > 12:
      tens = tens_to_word_dict[str(num)[1]]
      return f"{tens[:-1]}een"

  if len(str(num)) == 1:
    return unit_to_word_dict[str(num)]
    



print(num_to_words(0)) # return 'zero'
print(num_to_words(3)) # return 'three'
print(num_to_words(7)) # return 'seven'
print(num_to_words(12)) # return 'twelve'
print(num_to_words(13)) # return 'thirteen'
print(num_to_words(17)) # return 'seventeen'
print(num_to_words(34)) # return 'thirty four'
print(num_to_words(78)) # return 'seventy eight'
print(num_to_words(60)) # return 'sixty'
print(num_to_words(456)) # return 'four hundred and fifty six'
print(num_to_words(560)) # return 'five hundred and sixty'
print(num_to_words(612)) # return 'six hundred and twelve'
print(num_to_words(611)) # return 'six hundred and eleven'
print(num_to_words(610)) # return 'six hundred and ten'
print(num_to_words(10)) # return 'ten'
