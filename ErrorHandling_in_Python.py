str_to_float = ['2.1', '2.3', '7,5', '$12.12', '8.9', '5%', '33.1', '33#1']
floats = []
for s in str_to_float:
    try:
      floats.append(float(s))        
    except:
      floats.append(None)
      print('exception')


print (floats)



def adder(x, y):
    try:
      z = x+y
    except TypeError as target:
      return ('cannot add these types together')
    else:
      return ('result is:', z)


print (adder(5,7))
print (adder(5,"7"))

def no_four(number):
    if number == 4:
      raise ValueError('No fours allowed!!')
    else:
      print('Number:', number)

no_four(2)
print ("===========Knowledge Check===========")


def compare(a, b):
    try:
        a_greater = (a > b)
    except:
        a_greater = None
        b_greater = None
    else:
        b_greater = (b > a)
    finally:
        print(a_greater, b_greater)

compare(10,11)

print ("===========Knowledge Check===========")


def positive_only(a, b):
    output = a + b
    if output >= 0:
        return output
    else:
        # Your code here. to throw an valueError
        raise ValueError

#positive_only(10,-25)


print ("===========Knowledge Check===========")

def int_checker(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            print('both integers')
        else:
            raise ValueError
    except:
        print('error occurred')
    else:
        print('no error occurred!')
    finally:
        print('function completed')

int_checker(5,6)  
int_checker('5',6)


print ("===========Knowledge Check===========")

def divider(a, b):
  try:
    c = a/b
 # else:
  #  print('divided:', c)
      
  except:
    print('could not divide numbers')

divider(10, 2)
