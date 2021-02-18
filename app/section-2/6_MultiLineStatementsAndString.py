# Explicit break up statements
a = True
b = True
c = True

# using \ indentation doesn't matter
if a \
    and b\
        and c:
    print("Break up statements")


# Multi-Line String Literals
s = '''this is
multi line comment'''

d = """double quotes is valid
in multi comment
"""

# Comments in objects
a = [1, # item1
    2]

b = {
    'key1' : 1 #comment
    ,'key2' : 2 #comment
}

# comments in function
def my_func(a, #comment
            b
            ):
    print(a, b)

# comment in function call
my_func(10, #comment
        20
        )
