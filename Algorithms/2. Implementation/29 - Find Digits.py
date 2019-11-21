def findDigits(n):
    return sum(n % int(digit) == 0 and int(digit) != 0 for digit in str(n))