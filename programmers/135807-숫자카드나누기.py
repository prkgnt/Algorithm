#
# def getNumA(arrayA, arrayB):
#     dp = [0] * max(len(arrayA), len(arrayB))
#     # 배열의 가장 작은 수만큼 하나씩 비교
#     for i in range(arrayA[0], 1, -1):
#         f = 0
#         # A배열의 모든 원소를 탐색
#         for e in arrayA:
#             # 하나라도 나누어지지 않으면 break
#             if e % i != 0:
#                 f = 1
#                 break
#             else:
#                 dp[i] = 1
#         # 모든 원소가 i로 나누어질 경우
#         if f == 0:
#             # B배열의 모든 원소가 i로 나누어지지 않는지 검사
#             for j in range(0, len(arrayB)):
#                 # 하나라도 나누어지면 break
#                 if arrayB[j] % i == 0:
#                     f = 1
#                     break
#                 else:
#                     dp[i] = 1
#         # 모든 원소가 나누어지지 않을 경우 i 리턴
#         if f == 0:
#             return i
#
#     # for i in range(0, len(arrA)):
#     #     f = 0
#     #     for j in range(0, len(arrayB)):
#     #         if arrayB[j] % arrA[i] == 0:
#     #             f = 1
#     #             break
#     #     if f == 0:
#     #         return arrA[i]
#     return 0
# def solution(arrayA, arrayB):
#     arrayA.sort()
#     arrayB.sort()
#     res = getNumA(arrayA, arrayB)
#     if res >= min(arrayB):
#         return res
#     else:
#         resB = getNumA(arrayB,arrayA)
#     return max(res, resB)

def sol(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort(reverse=True)
    dp = [0] * max(min(arrayA) + 1, min(arrayB) + 1)
    res = 0
    # 배열의 가장 작은 수만큼 하나씩 비교
    for i in range(arrayA[0], 1, -1):
        f = 0
        # A배열의 모든 원소를 탐색
        for e in arrayA:
            # 하나라도 나누어지지 않으면 break
            if e % i != 0:
                f = 1
                break
            else:
                dp[i] = 1
        # 모든 원소가 i로 나누어질 경우
        if f == 0:
            # B배열의 모든 원소가 i로 나누어지지 않는지 검사
            for e in arrayB:
                if e % i == 0:
                    f = 1
                    break
                else:
                    dp[i] = 1
        # 모든 원소가 나누어지지 않을 경우 i 리턴
        if f == 0:
            res = i
            break
    if res >= arrayB[0]:
        return res

    arrayA.reverse()
    arrayB.reverse()

    for i in range(arrayB[0], 1, -1):
        if dp[i] == 1:
            continue
        f = 0
        # A배열의 모든 원소를 탐색
        for e in arrayB:
            # 하나라도 나누어지지 않으면 break
            if e % i != 0:
                f = 1
                break
        # 모든 원소가 i로 나누어질 경우
        if f == 0:
            # B배열의 모든 원소가 i로 나누어지지 않는지 검사
            for j in range(0, len(arrayA)):
                # 하나라도 나누어지면 break
                if arrayA[j] % i == 0:
                    f = 1
                    break
        # 모든 원소가 나누어지지 않을 경우 i 리턴
        if f == 0:
            if i >= res:
                return i
            else:
                return res
    return res

print(sol([10, 20], [5,17]))
print(sol([14, 35, 119], [18, 30, 102]))
