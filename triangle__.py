"""    Classify_Triangle code file      """
import datetime

A=3
B=4
C=5
ASSIGNMENT_NAME = "HW 01"
def my_brand(assignment_name):
    """
    print name, course details, assignment name, date and time.
    """
    print("=*=*=*= Sanjana =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print("=*=*=*=", assignment_name," =*=*=*=")
    print("=*=*=*=",datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),"=*=*=*=")

# In[4]:
my_brand(ASSIGNMENT_NAME)

def classify_triangle(a,b,c):
    """
    validate triangle using given input
    """
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    return False
def triangle_type(a,b,c):
    """
    type of triangle formed based on the input
    """
    if a==b and b==c:
        print('Triangle is Equilateral.')
    elif a==b or b==c or a==c:
        print('Triangle is Isosceles.')
    print('Triangle is Scalane')
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
        print('Tringle is Right angle')

if classify_triangle(A, B, C):
    triangle_type(A, B, C)
else:
    print('Triangle is not possible from given sides.')
