# 1    Given a list of numbers, create a new list containing only even numbers.

# numbers=[1,2,3,4,5,6,7,8,9]
# even_numbers=[]
# for i in numbers:
#     if i%2==0:
#         even_numbers.append(i)
# print(even_numbers)

# With List Comprehension

# numbers=[1,2,3,4,5,6,7,8,9]
# even_numbers=[i for i in numbers if i%2==0]
# print(even_numbers)

#____________________________________________________________________________________________________

# 2    Given a list of numbers, create a list containing the square of each number.

# numbers=[1,2,3,4,5,6,7,8,9]
# squares=[]
# for i in numbers:
#     squares.append(i*i)
# print(squares)

# With List Comprehension

# numbers=[1,2,3,4,5,6,7,8,9]
# squr=[i*i for i in numbers]
# print(squr)


#____________________________________________________________________________________________________


# 3    Given a list of numbers, create a list of numbers that are greater than 10.

# numbers=[12,423,54,64,3,5,67,9,65,2]
# new_list=[]
# for i in numbers:
#     if i > 10:
#         new_list.append(i)
# print(new_list)

# With List Comprehension

# numbers=[12,423,54,64,3,5,67,9,65,2]
# new_list=[i for i in numbers if i>10]
# print(new_list)



#______________________________________________________________________________________________________

# 4   Given a list of integers, create a new list where:

# If number is even → keep it

# If number is odd → replace it with 0



# numbers=[1,2,4,3,6,12,77,30,12]
# new_list=[]
# for i in numbers:
#     if i%2==0:
#         new_list.append(i)
#     else:
#         i=0
#         new_list.append(i)
# print(new_list)


# With List Comprehension

# numbers=[1,2,4,3,6,12,77,30,12]
# new_list=[i if i%2==0 else 0 for i in numbers]
# print(new_list)

#____________________________________________________________________________________________________

# 5   Given a list of numbers, create a list of numbers that are divisible by 3 and 5.

# numbers=[3,5,15,20,30]
# new_list=[]
# for i in numbers:
#     if i%3==0 and i%5==0:
#         new_list.append(i)
# print(new_list)

# With List Comprehension 

# numbers=[3,5,15,20,30,55]
# new_list=[i for i in numbers if i%3==0 and i%5==0]
# print(new_list)


#_______________________________________________________________________________________________________

# 6   Given a list of words, create a list containing words whose length is greater than 4.

# names=["Omar","Ali","Akbar","Ahmad","Hani","Ghazanfar"]
# new_names=[]
# for i in names:
#     if len(i)>4:
#         new_names.append(i)
# print(new_names)

# With List Comprehension 

# names=["Omar","Ali","Akbar","Ahmad","Hani","Ghazanfar"]
# new_names=[i for i in names if len(i)>4]
# print(new_names)


#______________________________________________________________________________________________________


# 7   Given a list of numbers, create a list of negative numbers only.

# numbers=[1,-3,4,-10,22,3,43,-100]
# negative_list=[]
# for i in numbers:
#     if i < 0:
#         negative_list.append(i)
# print(negative_list)



# With List Comprehension 

# numbers=[1,-3,4,-10,22,3,43,-100]
# negative_list=[i for i in numbers if i<0]
# print(negative_list)


#______________________________________________________________________________________________________

# 8   Given a list of numbers, create a new list where:

# If number is positive → keep it

# If number is negative → convert it to positive

# numbers=[3,-2,5,-7]
# new_list=[]
# for i in numbers:
#     if i>=0:
#         new_list.append(i)
#     else:
#         new_list.append(-i)
# print(new_list)



# With List Comprehension
# numbers=[3,-2,5,-7]
# new_list=[i if i>=0 else -i  for i in numbers]
# print(new_list)



#_______________________________________________________________________________________________________________

# 9   Given a list of numbers, create a list containing only numbers at even index positions.

# numbers=[10,20,30,40,50,60]
# new_list=[]
# # print(numbers[0::2])   
# for i in range(len(numbers)):
#     if i%2==0:
#         new_list.append(numbers[i])
# print(new_list)

# With List Comprehension 
# numbers=[10,20,30,40,50,60]
# even_list=[numbers[i] for i in range(len(numbers)) if i%2==0]
# print(even_list)

#____________________________________________________________________________________________________________

# 10   Given a list of numbers, create a new list where:

# If number is greater than 50 → replace with "High"

# Otherwise → replace with "Low"


# numbers=[20,75,40,90,50]
# new_list=[]
# for i in numbers:
#     if i > 50 :
#         i="High"
#         new_list.append(i)
#     else:
#         i="Low"
#         new_list.append(i)
# print(new_list)


# With List Comprehension 
# numbers=[20,75,40,90,50]
# new_list=["High" if i>50 else "low" for i in numbers] 
# print(new_list)




#___________________________________________________________________________________________________________


# This is the assignment by using Loops + List + List comprehension ........................