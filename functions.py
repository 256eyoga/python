name = "Don Jojo"

#display a given letter from the string
print(f"the last letter is: {name[-1]}")
print(f"the first letter is: {name[0]}")
print(f"the last letter is: {name[7]}")

#displays number of letters from the string using len() function
print(f"The variable name has: {len(name)}")

#make characters upper case
print(f"make upper case: {name.upper()}")

#make characters lower case
print(f"make lower case: {name.lower()}")

#join len()and slice[]
first = name[:4]
number = len(name)
print(first)
print(number)
print(f"{first}{number}")