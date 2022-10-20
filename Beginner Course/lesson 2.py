
#data type

#int -> 2, 5, -7, -80, 500 : 32-bit
x = 5 #-> 155 (reference)

#float -> 3.6, 7.3, 2.0 : 64-bit
x = 3.2 #-> 48

#boolean
x = True

#String
x = "rahul"

#None Type
None

#list

x=[2, 5, 7, 9, "rahul", True] # List
y={2, 5, 7, 9, "rahul", True} # Set
z={'Name' : "Rahul", "Age": None } # Dictionary
# print(z['Age'])

a="5"
b="3"
#print(a+b) # Concatation / Addition

c=int(3.9) # float -> int :: Type Casting
# print(c)

List1 = [5] # mutable data type
List1.append(8)
List1.append(2)
List1.append(9)
List1.pop(1)
#print(List1)

#Immutable
#Tuple
x=(3,5,1,True,"rahul")

x=({2,3,4})

#nested List

x=[2,3,5, ["rahul","ram","sham",11,True], 9]

print(type(x))

x=5
print(type(x))