"""Program to find the GCD """
def returnGCD(a, b):
    if(b==0):
        return a
    return returnGCD(b, a%b)

a = (int)( input('Enter first number >> ') )
b = (int)( input('Enter second number >> ') )
print("The GCD of ",a,' and ',b,' is: ', returnGCD(a,b))
