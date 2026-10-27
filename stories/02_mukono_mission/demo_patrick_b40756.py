# Import the TripPurse class from the story .py file
from story import TripPurse
# Test 1: Normal positive top-up
purse_one = TripPurse(1000)
result_one = purse_one.top_up(500)
print("Expected Return: True")
print("Actual Return:", result_one)
print("Expected Balance: 1500")
print("Actual Balance:", purse_one.balance)



#Text 2: Refused negative top-up
purse_two = TripPurse(2000)
result_two = purse_one.top_up(-500)
print("Expected Return: False")
print("Actual Return:", result_one)
print("Expected Balance: 2000")
print("Actual Balance:", purse_two.balance)


