def change(L):
    # 'L' is a local reference to the list passed in
    print(f"ID of list inside function: {id(L)}") 
    
    # Mutating the list in place
    L.append(5) 
    
    # The ID remains the same because the list object itself was modified
    print(f"ID of list inside function (after append): {id(L)}")


# 1. Create the original list
L1 = [1, 2, 3, 4]

# 2. Check original ID and contents
print(f"ID of original L1: {id(L1)}")
print(f"Original L1 contents: {L1}")

# 3. Pass the original list to the function
# Since lists are mutable, the function modifies the actual L1 object.
change(L1)

# 4. Uncommenting the line below passes a CLONE (a shallow copy) of L1.
# If you uncomment this, the function will modify the clone, 
# and the original L1 will remain completely safe and unchanged.
# change(L1[:]) 

# 5. Print L1 again to prove it was modified by the function call
print(f"L1 contents after function call: {L1}")

#If I passed tuple instead of list then the things could've been different, cause tuples are immutable and hence you'll not be facing any changes/challenges.