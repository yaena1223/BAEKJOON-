n = int(input())
new_num = -1
cnt = 0
num = n


while(True):
    if(n == new_num):break
    plus = num//10 + num%10
    new_num = int(str(num%10) + str(plus%10))
    cnt = cnt+1
    num = new_num

print(cnt)
