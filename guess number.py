import random 
num=random.randint(1,20)
i=0
while i<5:
    ans=int(input("請輸入數字:"))
    if ans == num: 
           print("恭喜答對") 
           break
    else:
        print("錯了ㄏ 錯了") 
        
        if ans>num:
            print("大一點") 
        if ans<num: 
            print("小一點")
    i=i+1
        