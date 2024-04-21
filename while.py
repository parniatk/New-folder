# 5.1 (Count positive and negative numbers and compute the average of numbers)
positive_num = 0
negative_num = 0
count = 0
total = 0

num = eval(input("Enter the number :"))

while num != 0 :
    num = int (input (" Enter another number :"))
    #being a positive number
    if num > 0 :
        positive_num = num +1
    else :
        negative_num = num +1
#sum
    total+=1
# count
    count+=1
#average
    average = total / count

print (f"number of positive number : {positive_num}")
print (f"number of negative number : {negative_num}")
print (f"total of numbers : {total}")
print (f"average of number : {average}")