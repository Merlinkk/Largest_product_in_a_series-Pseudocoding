num = 2709360626                                        #series in variable num
k = 3                                                   # k is contiguous digits
largest = 0                                             # initiliazing value of largest so we can compare
while num> 0:  # // 10 ** (k - 1)                       # using while loop here 
    digits = num % 10 ** k                              # this gives us % of num with 10 to the power k >> here it gives 626
    product = 1                                         # initializing product to multiply later
    while digits > 0:                                   #using nested while loop here till digit drops to 0
        product = product * (digits % 10)               
        if product == 0:
            break
        digits //= 10                                   #flooring the value of num one digit at a time 
    print(largest, product)                             #Purely for reference 
    largest = max(largest, product)                     # using max() function to get maximum value in largest variable
    num //= 10                                          #flooring the value of num, eliminating/deleting digits one at a time>> LOOP to 7

print(largest)

