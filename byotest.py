def number_of_evens(numbers):
    return 0
def equal_num(x, y):
    if x != y:
        return x
        
    else:
        return y
        
def check_for_item(collection, element):
     if element in collection:
         return collection
     else:
         return None

def check_not_in(collection, element):
     if element not in collection:
         return collection
     else:
         return None
    
def check_if_between(a, b, c):
      if c >= a and c <= b:
          return c
      else:
          return None
        
     
    


def tests_are_equal(actual, expected):
    assert expected == actual, "Expected {0} but got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}!".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} contains {1} error!".format(collection, item)

def test_between(x, z, t):
    assert t >= x and t <= z, " {0} is not within {1} and {2} inclusive".format(t, x, z)



test_between(5, 8, check_if_between(6, 11, 7))  
