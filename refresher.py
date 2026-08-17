x = 5  #    x = int(5)
colors = list()
names = []   # same as above
name = 'John', 'Smith'
y = 22

result = x + y

#  "name" -> OBJ(type, value)

# static typing
#  int x;
#  String s;

# dynamic typing
ham = 0
print(ham)
print(f"{type(ham) = }")


ham = "eggs"
print(ham)

print(f"{type(ham) = }")

s = "Knolls Bettis"
print(f"{s[0] = }")
print(f"{s[7] = }")

colors = ['pink', 'orange', 'scarlet']
print(f"{colors[0] = }")
print(f"{len(colors) = }")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0:3] = }")
print(f"{fruits[:3] = }")
print(f"{fruits[4:9] = }")

print(f"{fruits[-1] = }")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
print(f"{airports['OAK'] = }")
print(f"{airports['MCO'] = }")

colors = {'red', 'purple', 'green'}
colors.add('red')
colors.add('red')
colors.add('red')
print(f"{colors = }")

other_colors = {'green', 'orange', 'pink'}
print(f"{colors & other_colors = }")


x = 5
y = 10
z = 15
print(x)     #    print(str(x) + '\n')
print(x, y, z, sep='/')

poem = "Every\nline\nis\ngood"
print(poem)
print(repr(poem))
# str() 'useful' representation
# repr() 'how to reproduce'
print("x = ", x)
print(f"{x = }")
print(f"{x = }")
print(f"{poem = }")
print(f"{poem = !s}")

FILE_PATH = 'DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n')
        print(line)

#file_name = input("Open which file? ")
# process file_name
# use float() or int()

value = 56

if value > 75:
    print("koala")
    print("kookaburra")
elif value > 50:
    print("kangaroo")
    print("wallaby")
else:
    print("cane toad")

print("All done")

# 0 None False
# len(obj) == 0  (collections)

x = 5
if x:
    print("wahooooooo")
   
print(f"{bool("") = }")
print(f"{bool([]) = }")
print(f"{bool("0") = }")
print(f"{bool([None]) = }")


fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon']

for fruit in fruits:
    print(fruit)

while True:
    name = input("What is your name? ")
    if name == 'q':
        break  # exit loop
    print(f"Hello, {name}")
