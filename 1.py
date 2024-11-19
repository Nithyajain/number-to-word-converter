def number_to_words(n):
    if n == 0:
        return "zero"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def words(num):
        if num < 10:
            return units[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ("-" + units[num % 10] if num % 10 != 0 else "")
        elif num < 1000:
            return units[num // 100] + " hundred" + (" and " + words(num % 100) if num % 100 != 0 else "")
        else:
            for i, unit in enumerate(thousands):
                if num < 1000 ** (i + 1):
                    return words(num // (1000 ** i)) + " " + unit + (" " + words(num % (1000 ** i)) if num % (1000 ** i) != 0 else "")

    return words(n)

# Taking input from the user
try:
    number = int(input("Enter a number to convert to words: "))
    if number < 0:
        print("Please enter a non-negative number.")
    else:
        print(f"The number {number} in words is: {number_to_words(number)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
