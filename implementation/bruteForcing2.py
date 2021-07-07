# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면
# ABCKK13을 출력합니다.

# 난이도 1, 풀이시간 20분, 시간 제한 1초
# 입력 조건 : 첫째 줄에 하나의 문자열 S가 주어집니다.
# 출력 조건 : 첫째 줄에 문제에서 요구하는 정답을 출력합니다.


data = input("입력 : ")
alphaList = []
value = 0

for i in data:
    if ord(i) in range(ord('A'), ord('Z') + 1):
        alphaList.append(i)
    else:
        value += int(i)

alphaList.sort()

if value != 0:
    alphaList.append(str(value))
    
print(''.join(alphaList))
