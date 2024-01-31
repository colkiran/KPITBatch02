# print("hello")

heads = int(input("Enter the heads count :"))
legs = int(input("Enter the legs count :"))
heads = 33
for i in range (1 , heads+1):
    if (4*i) + (2*(heads-i)) == 108:
        print(f"number of chicken :{heads -i} and number of rabbit:{i}")