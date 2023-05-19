# Given a number, convert it into the words representing that number
# e.g. 123 > one hundred and twenty three
# The number will be any between 0 and 999

# Additional Task: Increase max to 9999
# Additional Task: Decimal numbers
# Additional Task: Negative numbers

units_dict = {
    '0': 'zero', '1': 'one', 
    '2': 'two', '3': 'three', 
    '4':'four', '5':'five', 
    '6':'six', '7':'seven', 
    '8':'eight', '9':'nine'
}

tens_dict = {
    '1': 'ten', '2': 'twenty', 
    '3': 'thirty', '4':'fourty', 
    '5':'fifty', '6':'sixty', 
    '7':'seventy', '8':'eighty', 
    '9':'ninety'
}

edge_case_dict = {
    '11': 'eleven', '12': 'twelve'
}

def assign_tens_and_units(num:int, units: str) -> str:
    """Takes the num and the already assigned units and generates one 
    str for tens and units 

    Args:
        num (int): the num inputted
        units (str): the units already assigned

    Returns:
        str: the tens and units as one string
    """
    tens_and_units = f'{tens_dict[str(num)[-2:-1]]} {units}'

    if str(num)[-2:] == '11':
        tens_and_units = edge_case_dict['11']
    if str(num)[-2:] == '12':
        tens_and_units = edge_case_dict['12']
    if units == 'zero':
        tens_and_units = tens_dict[str(num)[-2:-1]]

    return tens_and_units

def generate_decimal_words(decimal:str) -> str:
    output = ''
    for num in decimal:
        output += f'{units_dict[num]} '
    return output

def num_to_words(num:int) -> str:
    """Main function. Takes a number and returns a string which is 
    that number in words

    Args:
        num (int): inputted number

    Returns:
        str: number as words
    """
    
    # deals with decimal numbers 
    decimal = ''
    if '.' in str(num):
        decimal = 'point ' + generate_decimal_words(str(num).split('.')[1])
        num = int(str(num).split('.')[0])
        
    # edge case zero
    if num == 0:
        return f'zero {decimal}'
    
    # assign the word to the units of the number 
    units = units_dict[str(num)[-1:]]

    # returns only the units if num is smaller than 10
    if num < 10:
        return f'{units} {decimal}'

    # assigns the last two digits to tens_and_units. Changed if ends in 10, 11 or 12
    tens_and_units = assign_tens_and_units(num, units)

    # deals with remaining edge cases of 10, 11 and 12
    if num < 13:
        return f'{tens_and_units} {decimal}'
    # returns the 'teen' number if below 20 and above 12
    if num < 20:
        tens = tens_dict[str(num)[1]]
        return f"{tens[:-1]}een {decimal}"
    # returns number if less than 100
    if num < 100: 
        return f'{tens_and_units} {decimal}'

    # assigns hundreds
    hundreds = f"{units_dict[str(num)[-3:-2]]} hundred"
    # returns if number less than 1000
    if num < 1000:
        return f'{hundreds} hundred and {tens_and_units} {decimal}'
    
    # assigns hundreds
    thousands = f"{units_dict[str(num)[-4:-3]]} thousand"

    # returns if number less than 1000
    if num < 10000:
        return f'{thousands} {hundreds} and {tens_and_units} {decimal}'


print(num_to_words(0))
print(num_to_words(10))
print(num_to_words(17))
print(num_to_words(78))
print(num_to_words(456))
print(num_to_words(512))
print(num_to_words(5674.567))