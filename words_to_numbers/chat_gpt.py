def number_to_text(num):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num < 20:
        return ones[num]
    elif num < 100:
        return tens[num // 10] + " " + (ones[num % 10] if num % 10 else "")
    else:
        return number_to_text(num // 100) + " hundred" + ((" and " + number_to_text(num % 100)) if num % 100 else "")


print(number_to_text(145))