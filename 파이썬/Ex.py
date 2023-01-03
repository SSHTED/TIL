import time
start_time = time.time()
end_time = time.time()



n = int(input("거스를 금액 :"))
count = 0

c_type = [500, 100, 50, 10]

for coin in c_type:
    count += n // coin
    n %= coin
    print(n)

print(count)



print("소요 시간 : ", end_time - start_time)