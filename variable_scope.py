X = 5  # global var

def spam(ham):
    y = 100  # local var

def eggs(ham):
    y = "yellow" # local to eggs

def foo():
    name = "Fred"  # local to foo(), nonlocal to bar()
    def bar():
        print(name)

colors = list()
print(list(colors))

# print(x)   local -> nonlocal -> global -> builtin

# list = []   BAD IDEA!



