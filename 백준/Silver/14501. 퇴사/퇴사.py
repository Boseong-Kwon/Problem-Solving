N = int(input())
day = []
pay = []
memory = []
for i in range(N):
    temp_list = input().split()
    day.append(int(temp_list[0]))
    pay.append(int(temp_list[1]))
    memory.append(0)

memory.append(0)

for i in range(N):
    target = N - 1 - i
    if day[target] > i + 1:
        memory[target] = memory[target+1]
    else:
        if pay[target] + memory[target+day[target]] >= memory[target+1]:
            memory[target] = pay[target] + memory[target+day[target]]
        else:
            memory[target] = memory[target+1]

print(memory[0])