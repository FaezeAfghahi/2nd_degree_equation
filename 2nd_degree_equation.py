
"""
build a 2nd degree equation from their roots


"""

x = int(input ("please enter x:"))
y = int(input ("please enter y:"))
a = 1
b = -1*(x+y)
c = x*y
print(a,"(x**2)+(",b,")x+",c,"=0")