# 파이썬의 제어문에 대해 공부해봅시다.
# 조건문 if
# cookie = int(input("정수 입력: "))
# # print(cookie)

# if cookie < 0 :
#     print(f"{cookie}는 음수입니다.")
#     cookie *= -1
# else :
#     print(f"{cookie}는 양수입니다.")

# print(cookie)


# 반복문 while, for

# for 
for i in [1, 2, 3] :
    print(i)

print("-" * 50)

for i in range(1, 11) :
    print(i)

# 1 부터 100까지 더한 결과를 출력해보세요.
sum = 0
for i in range(1, 101):
    sum += i

print(f"합은 {sum}입니다.")