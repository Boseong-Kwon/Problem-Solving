place = input()
test = input().split()
list = input().split()
B = int(list[0])
C = int(list[1])

answer = int(place)

for i in test:
    if int(i) <= B:
        continue
    else:
        answer = answer + ((int(i)-B) // C)
        if ((int(i)-B) % C) != 0:
            answer += 1

print(int(answer))