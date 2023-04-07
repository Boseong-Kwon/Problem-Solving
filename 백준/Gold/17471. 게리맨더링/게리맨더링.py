region = int(input())
people = list(map(int,input().split()))

info = []
start_list = []
answer = []

for i in range(region):
    temp = list(map(int ,input().split()))
    for j in range(len(temp)):
        if j == 0:
            continue
        temp[j] -= 1
    info.append(temp)
    start_list.append(0)

def possible(list, index):
    list1 = []
    list2 = []
    for i in range(region):
        list1.append(list[i])
        list2.append(list[i])
    list2[index] = 1
    if(index == region -1):
        team_checker(list)# 여기 부분에 잘 나뉘었는지 확인해주는 함수가 들어가야함.
    else:
        possible(list1,index+1)
        possible(list2,index+1)

def team_checker(team):
    if valid_checker(team) == 0:
        team_a = []
        team_b = []
        for i in range(len(team)):
            if team[i] == 0:
                 team_a.append(i)
            else:
                 team_b.append(i)
        visited_a = []
        visited_b = []

        if (DFS(team_a,team_a[0],visited_a) != 0 and DFS(team_b,team_b[0],visited_b) != 0):
            calc(team_a,team_b)
        
def valid_checker(list):
    counter = 0
    for i in list:
        if i == 0:
             counter += 1
        else:
             counter -= 1
    if counter == len(list) or counter == len(list) * (-1):
        return -1
    else:
        return 0
    
def DFS(team,region_number,visited):
    r_value = 0
    if region_number not in team:
        return 0
    if region_number not in visited:
        visited.append(region_number)
        if len(team) == len(visited):
            return 1
        for i in range(info[region_number][0]):
            r_value += DFS(team,info[region_number][i+1],visited)
        return r_value
    else:
        return 0

def calc(list_a, list_b):
    a_team = 0
    b_team = 0
    for i in list_a:
        a_team += people[i]
    for j in list_b:
        b_team += people[j]
    if a_team >= b_team:
        answer.append(a_team - b_team)
    else:
        answer.append(b_team - a_team)

def min_calculator(list):
    if len(list) == 0:
        return -1
    min = list[0]
    for i in list:
        if min > i:
            min = i
    return min

possible(start_list,0)
print(min_calculator(answer))