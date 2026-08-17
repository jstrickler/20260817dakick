import sillymod

def doit(greeting="greetings"):
    print(f"{greeting} out there!")
    return 42

result = doit("hello")
print(f"{result = }")

doit("goodbye")
doit()
# doit("hello", 'goodbye')

def read_files(color, *file_paths):
    print(f"{color = }")
    for file_path in file_paths:
        print(file_path)

read_files('red', 'mary.txt')
read_files('blue', 'lemur.txt', 'bushbaby.txt', 'potto.txt')
read_files('green')

x = {'foo'}

sillymod.silly()