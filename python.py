#1
list1=[1,2,3,4,5]
for i in list1:
    print("element:,i")
    print(list1[0])

#2
for i in range(0,999):
    print(i)

#3
list2=["a","b",1,"de"]
for i in list2:
        print(i)

#4
for i in "BTuPo":
     print(i)

 #5
list1.append(9)
print(list1)          


#esep1
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
 
total_product = 1
for num in range(A, B + 1):
    total_product *= num
 
print(f"The product of integers from {A} to {B} inclusive is: {total_product}")

#esep2

N = int(input("Enter a positive integer N: "))
 
sum_result = sum(1 / i for i in range(1, N + 1))
 
print(f"The sum 1 + 1/2 + 1/3 + ... + 1/{N} is: {sum_result:.6f}")