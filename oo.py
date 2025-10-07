

'''
text = "hello amazing world"

words = text.split()       # ['hello', 'amazing', 'world']
longest = words[0]         # 'hello'

for word in words[1:]:
    if len(word) > len(longest):
        longest = word

print(longest)   # Output: amazing
'''
'''
def prompt_and_write(filename):
    with open (filename,"w") as file:
        while True:
            line= input("Enter text(leave blank to stop):")
            if line=="":
                break
            file.write(line+"\n")
prompt_and_write("file.txt")
'''
'''
def print_names(filename):
    with open(filename,'r') as file:
        next(file)

        for line in file:
            parts=line.strip().split(",")

            if len(parts) >= 2:
                last_name= parts[0]
                first_name=parts[1]
                print(first_name,last_name)
print_names("CSV.csv")
'''
'''
def printname(filename):
    with open (filename,'r') as file:
        #next(file)

        for line in file:
            parts=line.strip().split(",")

            if len(parts)>=2:
                first=parts[0]
                second=parts[1]
                print(first,second)
    printname("CSV.csv")
'''
'''
def numbers():
    total=0
    while True:
        filename=input("enter filename:")
        if filename=="":
            break
        with open (filename,'r') as file:
            file_sum=0
            for line in file:
                file_sum+=int(line.strip())
            print("sum of numbers in",filename,":",file_sum)
            total+=file_sum
    print("Total sum of all files:",total)
numbers()
   '''
'''
try:
    x=int(input("enterx:"))
    y=int(input("enter y:"))

    print("x+y=",(x+y))
except:
    print("invalid integer(s).")
    print("try again.")      
    '''
'''
def numbers():
    total_sum = 0
    while True:
        filename = input("Enter filename: ")
        if filename == "":
            break
        try:
            with open(filename, 'r') as file:
                file_sum = 0
                for line in file:
                    try:
                        file_sum += float(line.strip())
                    except ValueError:
                        continue
            print(f"Sum of numbers in {filename}: {file_sum}")
            total_sum += file_sum
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please try again.")
    print(f"\nTotal sum across all valid files: {total_sum}")

numbers()
'''
'''
try:
    x_input=input("enter x:")
    y_input=input("enter y:")
    x=int(x_input)
    y=int(y_input)

    print("x/y=",(x/y))

except ValueError:
    print("Invalid number entered.")
except ArithmeticError:
    print("can't divide by 0.")
    '''
'''
import csv

with open("C:/Users/Amanullah K Batcha/OneDrive/Desktop/pythonfiles/students.csv") as file:
    next(file)
    for line in file:
        name, m1, m2, m3=line.strip().split(",")
        avg=(int(m1)+int(m2)+int(m3))/3
        print(name,"average:",avg)
     '''
    '''
def num():
    while True:
        name=input("enter file name:")
        if name=='':
            break
        with open(name,"r") as file:
            file_sum=0
            for line in file:
                file_sum+=int(line.strip())
            print("the sum of the numbers in the file",name,"is",file_sum)
num()
'''
def num(name):
    while True:
        name=input("enter nameof file:")
        if name=="":
            break
        with open(name,"r") as file:
            for line in file:
                m1,m2,m3,m4,m5=line.strip().split(",")
                add=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
                print("the sum of all the numbers in file",name,"is:",add)
num(name)


