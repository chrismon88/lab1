# create variables for name and birthday input
name = input("What is your name?")
birth_month = input("what month were you born in?")
#print greeting concatinate name
print("Hello, " + name + "!")

if birth_month == "December":
    print("Happy birthday month!")

print(f"There are {len(name)} letters in your name!")