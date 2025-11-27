#Types and Iterals
#Python can understand data types
#Python has built in Data Structures
x = 42
print(type(x))
y = 3.14
print(type(y))
z = "hello" # (String): A sequence of characters
print(type(z))
t = True
print(type(t))
lst = [1,5,3] #(List): List is a sequential data structure
print(type(lst))
print(f"List before mutation: {lst}")
lst.append(22)
print(f"List after mutation: {lst}")
list_in_list = [1,5,3, ["Hijbullah", "Rahul", "Arfi", 3.5, 3*4], "hi"]
print(f"List under list: {list_in_list}")
tpl = (1,3,1)
print(type(tpl)) #Immutable
#The main difference between a tuple and a list in Python is that a **list is mutable** (its elements can be changed), while a **tuple is immutable** (its elements cannot be changed after creation).
Dict = {"a": 1, "b": 2} #Dictionar will gain the first one if there is duplicate value for one key
print(type(Dict))
Set = {1,2,2,3} #Do not allow duplicate value
print(type(Set))

#python is all about class and object