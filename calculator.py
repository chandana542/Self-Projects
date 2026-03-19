
def calc(x,y,op):
    if op=='+':
        ans=x+y
    elif op=='-':
        ans=x-y
    elif op=='*':
        ans=x*y
    elif op=='/':
        if y==0:
            return 'Division with 0 is not possible'
        ans = x/y
    elif op=='%':
        ans=x%y
    elif op=='**':
        ans=x**y
    else:
        return 'Invalid Operation'
    return ans

print('Calculator Program')

while True:
    x=float(input('Enter first number: '))
    y=float(input('Enter second number: '))
    op=input('Choose an operation by entering the symbol:\n1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Modulus(%)\n6.Power(**)\n')
    print(calc(x,y,op))
    a=input('Do you want to continue (y/n)?')
    if a=='n':
        break