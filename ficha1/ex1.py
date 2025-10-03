def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False
    
print(f"Test 1: (True, True) -> {monkey_trouble(True, True)} (Expected: True)")
print(f"Test 2: (False, False) -> {monkey_trouble(False, False)} (Expected: True)")
print(f"Test 3: (True, False) -> {monkey_trouble(True, False)} (Expected: False)")
print(f"Test 4: (False, True) -> {monkey_trouble(False, True)} (Expected: False)")