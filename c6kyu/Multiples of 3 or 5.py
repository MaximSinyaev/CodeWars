def solution(number):
    sum = 0
    max_3 = (number - 1) // 3
    max_5 = (number - 1) // 5
    for i in range(1, max_3 + 1):
      sum += i * 3
    for i in range(1, max_5 + 1):
      if i % 3 != 0:
          sum += i * 5
    return sum

print(solution(10))