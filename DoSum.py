num=int(input("Enter a number : "))
def DoSum(num):
    sum=0
    while num!=0:
        sum+=num % 10
        num //=10
    return sum

print("The sum of digit is :",DoSum(num))
