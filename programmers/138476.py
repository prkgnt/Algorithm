def solution(k, tangerine):
    sum = 0
    dict = {}
    answer = 0
    for i in range(0, len(tangerine)):
        if tangerine[i] in dict:
            dict[tangerine[i]] += 1
        else:
            dict[tangerine[i]] = 1

    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    #print(sorted_dict)
    for i in sorted_dict:
        sum += i[1]
        answer += 1
        if sum >= k:
            break
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))