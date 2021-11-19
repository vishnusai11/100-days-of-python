# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_name=name1+name2
total_name_1=total_name.lower()
count1=0
count2=0
count1=total_name_1.count('t')+total_name_1.count('r')+total_name_1.count('u')+total_name_1.count('e')
count2=total_name_1.count('l')+total_name_1.count('o')+total_name_1.count('v')+total_name_1.count('e')
count1_1=str(count1)
count2_1=str(count2)
count=count1_1+count2_1
final_count=int(count)
if final_count<10 or final_count>90:
  print(f"Your score is {final_count}, you go together like coke and mentos.")
elif final_count>=40 and final_count>=50:
  print(f"Your score is {final_count}, you are alright together.")
else:
  print(f"Your score is {final_count}.")