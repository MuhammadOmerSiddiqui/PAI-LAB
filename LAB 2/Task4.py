data = (10, -3, 7, 4, -8, 2, -5)
pair = []
pair_list = []
min_sum = float('inf')
for i in range(0,len(data)-1):
    for j in range(i+1,len(data)):
        sum = data[i] + data[j]
        if(sum<0):
            sum *= -1
        if(sum<min_sum):
            min_sum = sum
            pair_list = [[data[i],data[j]]]
        elif(sum==min_sum):
            pair_list.append([data[i],data[j]])
print(pair_list)