# You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 
n = 2
cnt = 0
for i in range(11):
    multiple = n * cnt
    cnt = cnt + 1
    print(multiple)