def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums: 
        if num == 7:
            return True
    return False

    # first we can iterate through the list 
    
    # create a conditional that if the list contains 7 it true/ if not false 

 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

any7([1, 2, 7, 4, 5])