import datetime
import argparse
import string

def intChecker(a):
    num = int(a)
    if num < 8:
        raise argparse.ArgumentTypeError("Password character amount too low. The minimum is 8 characters.")
    return num

# argparse setup
parser = argparse.ArgumentParser(description = "Generates a random password")
parser.add_argument("-l", "--lower", dest = "LOWER", metavar = "LOWERCASE", choices = ["y", "n"], default = "y", help = "Choose either y or n to generate with lowercase characters. (Default: y)")
parser.add_argument("-u", "--upper", dest = "UPPER", metavar = "UPPERCASE", choices = ["y", "n"], default = "y", help = "Choose either y or n to generate with uppercase characters. (Default: y)")
parser.add_argument("-n", "--numbers", dest = "NUMBERS", metavar = "NUMBERS", choices = ["y", "n"], default = "y", help = "Choose either y or n to generate with numbers. (Default: y)")
parser.add_argument("-s", "--symbols", dest = "SYMBOLS", metavar = "SYMBOLS", choices = ["y", "n"], default = "y", help = "Choose either y or n to generate with symbols. (Default: y)")
parser.add_argument("-a", "--amount", dest = "AMOUNT", metavar = "AMOUNT", type = intChecker, default = 8, help = "Specify amount of characters the password will contain. (Minimum and default is 8)")
parser.add_argument("-o", "--output", dest = "OUTPUT", metavar = "OUTPUT", default = "", help = "Outputs to a file.")
args = parser.parse_args()

LOWER = args.LOWER
UPPER = args.UPPER
NUMBERS = args.NUMBERS
SYMBOLS = args.SYMBOLS
AMOUNT = args.AMOUNT
OUTPUT = args.OUTPUT

# generates possible types of characters for password
lowerChars = string.ascii_lowercase
upperChars = string.ascii_uppercase
numberChars = string.digits
symbolChars = string.punctuation

# generate random int between min and max (inclusive) using datetime
def randomNumber(min, max):
    current = datetime.datetime.now()
    ms = str(current.microsecond)
    algo = float(ms[::-1][:3:]) / 1000
    return round(min + algo * (max - min))

# generates the character bank according to user specifications
def charBank(LOWER, UPPER, NUMBERS, SYMBOLS):
    str = ""
    if LOWER == "y":
        str += lowerChars
    if UPPER == "y":
        str += upperChars
    if NUMBERS == "y":
        str += numberChars
    if SYMBOLS == "y":
        str += symbolChars
    return str

def main():
    while True:
        bank = charBank(LOWER, UPPER, NUMBERS, SYMBOLS)
        password = ""
        for i in range(AMOUNT): # write to password string according to specified password length
            randomChar = bank[randomNumber(0, len(bank) - 1)] # assign randomChar from a random character from the bank using random number generator
            password += randomChar
        if LOWER == "y" and (any(char in lowerChars for char in password)) == False: # if lower characters are specified but not in the generated password string, restart the while loop
            continue
        elif UPPER == "y" and (any(char in upperChars for char in password)) == False: # if upper characters are specified but not in the generated password string, restart the while loop
            continue
        elif NUMBERS == "y" and (any(char in numberChars for char in password)) == False: # if number characters are specified but not in the generated password string, restart the while loop
            continue
        elif SYMBOLS == "y" and (any(char in symbolChars for char in password)) == False: # if symbol characters are specified but not in the generated password string, restart the while loop
            continue
        elif OUTPUT != "": # if user wants to output to file
            filename = OUTPUT
            print(f"Creating: {filename}")
            with open(filename, "w") as f:
                f.write(password)
                print("Done!")
            break
        else: # if the generated password string meets all user specified requirements, output to terminal
            print(password)
            break

main()