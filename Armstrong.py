num=int(input("Enter a number to be checked : "))
def checkArmstrong(num):
    orginal=num
    sum=0
    while num>0:
        digit =num%10
        sum = sum + (digit ** 3)
        num//=10
    if sum == orginal:
        print("Armstrong number ")
    else:
        print("Not an Armstrong number ")

checkArmstrong(num)
