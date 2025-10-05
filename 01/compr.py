#Comprehensions
temp = [35,40,28,32,30]
farhen = [item*(9/5)+32 for item in temp]
print(farhen)

unique_initials = {item[0].lower() for item in ["Alice", "Bob", "hijbullah"] }
print(unique_initials)

square_map = {x: x**2 for x in range(5)}
print(f"Squred Map{square_map}")