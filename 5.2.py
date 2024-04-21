import random
import time 

correct_Count = 0
start_time = time.time()

for _ in range(10) :
    a = random.randint (1 , 15)
    b = random.randint (1 , 15)
#question
    question = f"what is {a}+{b} ?" 
    answer = a + b
    print(question)
#get the answer from the user
    user_answer = eval(input())
    if user_answer == answer:
        correct_Count += 1
        print("The answer is true ")
    else:
        print(f"The answer is wrong :Right answer is {answer}")

#time spent
end_time = time.time()
time_Spande = end_time - start_time

# Results
print(f"\n you have{correct_Count} answered the correct questions.")
print(f"time spent is :{time_Spande :.2f} sanie.")
