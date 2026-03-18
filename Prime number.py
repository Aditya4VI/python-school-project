num = int(input("Enter your number: "))

if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")
