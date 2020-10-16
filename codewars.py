############################################## KATA 1 ##############################################
from collections import Counter
import re


def number_to_string(num):
    return str(num)


print(number_to_string(5))

############################################## KATA 2 ##############################################
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


def countBits(n):
    binary = bin(n)
    oneCounter = 0
    for number in binary:
        if number == '1':
            oneCounter += 1
    return oneCounter


def countBitsWithOne(n):
    return bin(n).count('1')


print(countBits(1234))
print(countBitsWithOne(1234))


############################################## KATA 3 ##############################################
# Take a Ten Minute Walk
# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends
# you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block in a direction and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.


def is_valid_walk(walk):

    # determine if walk is valid
    numberOf_N = walk.count("n")
    numberOf_S = walk.count("s")
    if len(walk) == 10 and (numberOf_N == numberOf_S):
        numberOf_E = walk.count("e")
        numberOf_W = walk.count("w")
        if numberOf_W == numberOf_E:
            return True
        else:
            return False
    else:
        return False

    # match = re.findall("[n,s,w,e]", "".join(walk))
    # if len(match) == 10:
    #     return True


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))

# Alternativa con Counter delle Collections


def isValidWalkWithCollections(walk):
    if len(walk) == 10:
        walkmap = Counter(walk)
        print(walkmap['n'])
        return walkmap['n'] == walkmap['s'] and walkmap['e'] == walkmap['w']
    return False


print(isValidWalkWithCollections(
    ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))


############################################## KATA 4 ##############################################
# Find The Parity Outlier
# You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers or entirely
# comprised of even integers except for a single integer N. Write a method that takes
# the array as an argument and returns this "outlier" N.
def find_outlier(integers):
    oddCount = 0
    evenCount = 0
    even = None
    odd = None
    for n in integers:
        if n % 2 == 0:
            oddCount += 1
            odd = n
        else:
            evenCount += 1
            even = n
        if oddCount > evenCount and even != None:
            return even
        elif evenCount > oddCount and odd != None:
            return odd


print(find_outlier([3122704, 9797788, -8903086, -9690270, 1462276, 842346, -7736330, 900026, 728728, 9325726, -2565996, 1158718, -661588, 3733084, -8158688, 4915190, -9837902, -3163512, -
                    2321478, 7189216, -357668, -4366544, 246876, 6324516, 4288466, -9301460, -5046165, 2966028, -4338102, -2981334, -6132590, 7005978, 6438010, -4148538, -4690300, -9285126, -4300934, 2818548]))


############################################## KATA 5 ##############################################
# Split Strings
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character
# of the final pair with an underscore ('_').

def solution(s):
    out = [s[i:i + 2] for i in range(0, len(s), 2)]
    if out and len(out[-1]) == 1:
        out[-1] += "_"
    print(out)


solution("asdfadsfA")

############################################## KATA 6 ##############################################
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).


def to_camel_case(text):
    # your code here
    out = []
    for i in range(len(text)):

        if (text[i] == "-" or text[i] == "_") and text[i+1]:
            i += 1
            out += text[i].upper()
            i += 1
        else:
            out += text[i]
    return out


print(to_camel_case("pollo-tonto-bello"))


print(4/7, end="  5\n")

print('One,\'two\',\"three\",four,\\five\\\n\tonce,\'I\' caught a\
 fish\n\t\t\'//alive\\\\\'')

a = 1
b = 2
c = "pippe ar sugo"
print(c[0])
print(c[-1])
print(c[0:3])
print(c[0:])
print(c[:3])
print(c[:])

first = "          Federico        "
last = "    Monaco"
full = f"{first}  {last}"
print(full)

print(full.upper())
print(full.lower())
print(full.strip())


print(abs(-3.2))

a = len(c)
print(a)


print("bag" < "baf")

for number in range(0, 10):
    print("Pollo", number+1)


def pippo(a, b=1):
    return a+b


print(pippo(1, 2))
print(pippo(1))


# LIST
letters = ["a", "b", "c"]

matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
print(list(range(20)))
print(list("Hello World"))

letters = ["a", "b", "c", "d"]
print(letters)
print(letters[0])
print(letters[0:3])
print(letters[:3])
print(letters[:2])
print(letters[0:2])
print(letters[2:])
print(letters[::2])

numbers = list(range(20))
print(numbers[::-1])  # reverse order printing

# LIST UNPACKING
numbers = [1, 2, 3, 4]
first = numbers[0]
second = numbers[1]
third = numbers[2]

print(first)
print(second)
print(third)

# unpacking example
a, b, *other = numbers
print("unpacking example!")
print(a)
print(b)
print(other)

# Looping over list
letters = ["a", "b", "c", "d"]
for letter in letters:
    print(letter)

# Enumerate in list - crea delle tuple! Itera la lista e crea delle coppie come key,value. Praticamente scompone la lista.
for letter in enumerate(letters):
    print(letter)

for letter in enumerate(letters):
    print(letter[0], letter[1])

# con questo metodo riusciamo a farci creare separatamente la lista delle KEY e la lista dei VALUE in modo da creare due variabili separatae
for index, letter in enumerate(letters):
    print(index, letter)

# Adding items to a list
letters.append("a")
letters.insert(0, "-")

# Removing items from a list
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)

# Try to find items in a list
letters = ["a", "b", "c", "d"]
print(letters.index("a"))

if "t" in letters:
    print("TRUE")
else:
    print("FALSE")


#List Sorting
numbers = [3,51,2,8,6]
numbers.sort()
print(numbers)

#reverse sorting
numbers.sort(reverse=True)
print(numbers)

#How to do a custom sort function
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
items.sort()
print(items)

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

#Lambdas expressions/functions
items.sort(key=lambda item: item[1])
print(items)

print("pollo")