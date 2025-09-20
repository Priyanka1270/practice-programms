#swap two variables
a=input("Enter a variable a: ")
b=input("Enter a variable b: ")
print(f"Original variables a={a},b={b}")
#using temp variable
temp=a
a=b
b=temp
print(f"swapped values :a={a},b={b}")
