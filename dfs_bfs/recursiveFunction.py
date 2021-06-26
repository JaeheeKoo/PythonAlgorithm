# 재귀 함수란 자기 자신을 다시 호출하는 함수를 의미
# 단순한 형태의 재귀 함수 예제
# '재귀 함수를 호출' 라는 문자열을 무한히 출력
# 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력됨

def recursive_function():
    print("재귀 함수 호출")
    recursive_function()

recursive_function()


# 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 함
def recursive_function2(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i+1, '번째 재귀함수를 호출')
    recursive_function2(i+1)
    print(i, '번째 재귀함수를 종료')

recursive_function2(1)
# 재귀 함수는 stack 프레임으로 작동!