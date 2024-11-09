def factors(number):
    print(" The factors are ")
    for i in range(1,number+1):
        if number%i==0:
            print(i)

num=int(input(" Enter a number. "))
factors(num)
    