fruits = "apple","banana","mango","oromge"
for fruits in fruits:
    print(fruits)
for ran in range(2,6):
    print(f"ranges: {ran}")

for simad in range(1,8):
    print(f"xarumaha simad: {simad}")


for nadaara_age in range(1,20,5):
    print(f"Nadaara ages are: {nadaara_age}")

count = 1
while count<=5:
    print(f"Count: {count}")
    count+=1

print("Done!")

numbers = 1,2,3,4,5,6,7,8,8,9,10
for numbers in numbers:
    print(f"Numbers are: {numbers}")
print("Done!")

count =0
while count<=10:
    count+=1
    print(f"Counts are: {count}")
print("Done!")


for i in range(1,10):
    if i ==5:
        break
    print(i)



for i in range(1,10):
    if i == 5:
        continue
    print(i)
count = 1
while count<=10:
    if count==5 or count== 7:
        count+=1
        continue
    print(count)
    count +=1