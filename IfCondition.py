'''
1. Simple if

    if condition:
        statement

2. if/else

    if condition:
        statement
    else:
        statement

3. Nested If

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

4. Ladder if/else

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement        
'''

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print(a," Is Greater Value")
    else:
        print(c," Is Greater Value")
elif b>c:
    print(b," Is Greater Number")
else:
    print(c," Is Greater Value")
