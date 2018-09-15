def is_even(number):
    return number % 2 == 0

def number_even_numbers(numbers):
    
        
    
        
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)

assert number_even_numbers([]) == False, "No numbers"
assert number_even_numbers([2,4]) == True, "2 even numbers"
assert number_even_numbers([2]) == False, "1 even number"
assert number_even_numbers([1,3,9]) == False, "Odd numbers and no even numbers!"
assert number_even_numbers([1,2,3,5,6]) == True, "2 even numbers"

print("All tests passed!")