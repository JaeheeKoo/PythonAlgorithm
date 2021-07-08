# 체스판 8 x 8 좌표 평면. 나이트가 있습니다.
# 나이트가 움직이는 경우
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동

# 8 x 8 좌표에서 나이트의 위치가 주어졌을 때
# 나이트가 이동할 수 있는 경우의 수를 출력하세요.
# 행 위치는 1~8로 표현하며, 열 위치는 a~h로 표현합니다.

# 난이도 1, 풀이 시간 20분, 시간 제한 1초, 메모리 제한 128MB
# 입력 조건 : 첫째 줄에 현재 나이트가 위차한 곳의 좌표를 나타내는 두 문자로 구성된 문자 열이 입력
#            입력 문자는 a1처럼 열과 행으로 이뤄짐
# 출력 조건 : 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력

place = input("입력 :")
row = int(place[1])
col = ord(place[0]) - ord('a') + 1

dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2,-2, 2, -1, 1, -1, 1, -1, 1]

count = 0

for i in range(len(dx)):
    nx = row + dy[i]
    ny = col + dx[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count, "개") 


# 해답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1<= next_column <= 8:
        result += 1
print(result)