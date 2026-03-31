# मान लीजिए हमारे पास दो अलग-अलग लिस्ट हैं जिनमें एक जैसा डेटा है
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 अब वही ऑब्जेक्ट है जो list1 है

print("\n--- Identity Operators ---")

# 1. 'is' Operator (क्या ये एक ही ऑब्जेक्ट हैं?)
print("list1 is list3:", list1 is list3)  # True (क्योंकि list3 = list1 किया गया है)
print("list1 is list2:", list1 is list2)  # False (डेटा सेम है, पर मेमोरी में अलग जगह हैं)

# 2. 'is not' Operator (क्या ये अलग-अलग ऑब्जेक्ट हैं?)
print("list1 is not list2:", list1 is not list2) # True (हाँ, ये अलग-अलग हैं)

# 3. Comparison vs Identity (== vs is)
print("\n--- Difference: == vs is ---")
print("list1 == list2:", list1 == list2) # True (क्योंकि डेटा/वैल्यू बराबर है)
print("list1 is list2:", list1 is list2) # False (क्योंकि ऑब्जेक्ट/मेमोरी एड्रेस अलग है)