from byotest import *
coins = [100, 50, 20, 10, 5, 2, 1]
def get_change(amount):
    
      
    change =[]
    for coin in coins:
       while coin <= amount:
           amount -= coin
           change.append(coin)
    return change
    
    
tests_are_equal(get_change(0), [])
tests_are_equal(get_change(1), [1])
tests_are_equal(get_change(2), [2])
tests_are_equal(get_change(5), [5])
tests_are_equal(get_change(10), [10])
tests_are_equal(get_change(20), [20])
tests_are_equal(get_change(50), [50])
tests_are_equal(get_change(100), [100])
tests_are_equal(get_change(3), [2, 1])
tests_are_equal(get_change(7), [5, 2])
tests_are_equal(get_change(6), [5, 1])
tests_are_equal(get_change(9), [5, 2, 2])
tests_are_equal(get_change(19), [10, 5, 2, 2])


print("All tests passed!")