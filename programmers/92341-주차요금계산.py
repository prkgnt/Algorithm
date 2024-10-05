import math


def solution(fees, records):
    answer = []
    fee = {}
    time_table = {}
    for i in range(0, len(records)):
        time, num, p_type = records[i].split()
        if p_type == 'IN':
            time_table[num] = time
        else:
            o_time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
            i_time = int(time_table[num].split(":")[0]) * 60 + int(time_table[num].split(":")[1])
            if num in fee:
                fee[num] += o_time - i_time
            else:
                fee[num] = o_time - i_time
            time_table[num] = 0

    for key in time_table:
        if time_table[key] != 0:
            if key in fee:
                fee[key] += 1439 - (int(time_table[key].split(":")[0]) * 60 + int(time_table[key].split(":")[1]))
            else:
                fee[key] = 1439 - (int(time_table[key].split(":")[0]) * 60 + int(time_table[key].split(":")[1]))

    sorted_values = [fee[key] for key in sorted(fee)]

    for v in sorted_values:
        x = fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3]
        if x <= fees[1]:
            answer.append(fees[1])
        else:
            answer.append(x)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))