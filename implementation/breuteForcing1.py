# 완전 탐색
# 가능한 경우의 수를 모두 검사해보는 탐색 방법

# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
# 00시 00분 03초, 00시 13분 30초 ...

# 난이도 1, 풀이시간 15분, 시간제한 2초, 메모리 제한 128MB
# 입력 조건 : 첫째 줄에 정수 N이 입력 (0 <= N <= 23)
# 출력 조건 : 3이 하나라도 포함되는 모든 경우의 수를 출력


N = int(input("입력 : "))

for i in range(0, N + 1):
    for j in range(60):
        for k in range(60):
            hour = str(i).zfill(2)
            minute = str(j).zfill(2) 
            second = str(k).zfill(2)
            S =  hour + minute + second 
            if "3" in S:
                print("{}시 {}분 {}초".format(hour, minute, second))

