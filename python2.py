#LIST 
fruits=["appple","banana","cherry","date","elderberry"]
print("First fruit:",fruits[0])
print("last fruit:",fruits[-5])
fruits.append("fig")
print("updated list:",fruits)
fruits.pop(0)
print("List after removal:",fruits)
#list operation
numbers=[2,4,6,8,10]
total_sum=sum(numbers)
print("sum of numbers:",total_sum)
new_numbers=[num*2 for num in numbers]
print("numbers multiplied by 2:",new_numbers)
#slicing
number=[1,2,3,4,5,6,7,8,9,10]
print("First 3 elements:",number[ :3])
print("Last 3 elements:",number[-3: ])
print("Elements form indext 2 to 6;",number [2:7]) 
#sorting
numb=[4, 1, 7,3, 9]
numb.sort()
print("Ascending:",numb)
numb.sort(reverse=True)
print("Deceding:",numb)
#List comprehension
squares=[x**2 for x in range(1,11)]
print("squares:",squares)
#matrix
matrix=[[1,2],[3,4],[5,6]]
print("second row:",matrix[1][1])
print("element at [2][1]:",matrix[2][1])