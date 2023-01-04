import time
start_time = time.time()
end_time = time.time()




score = 90, 85, 77, 65, 97
ch = {2,4}

for i in range(5):
    if i+1 in ch:
        continue
    if score[i] >= 80:
        print(i+1, "합격")












print("소요 시간 : ", end_time - start_time)