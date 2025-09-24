'''
NAME: Wasilah Amanullah
ID NUMBER: 748006541
SECTION 604
'''
#the code using function to check what type of triangle it is
'''
To check if a triangle is equilateral,isoceles or scalene with its sides:
'''
def triangle(a,b,c): #function is being called
    '''
    sides are a,b and c
    '''
    if a==b and b==c and a==c:#to check if all sides are the same
        return "equilateral"
    elif a==b or b==c or c==a:# to check if any two sides are same
        return "isoceles"
    else:# if none of the sides are equal then its scalene
        return "Scalene"
def main():
    #to call the previous function
    a=int(input("Enter side a:"))
    b=int(input("Enter side b:"))
    c=int(input("Enter side c:"))
    output=triangle(a,b,c)
    print('the triangle is',output)
main() 

 



    


        
 