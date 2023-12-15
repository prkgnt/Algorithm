class Solution(object):
    def reorderLogFiles(self, logs):
        letter_logs = []
        num_logs = []
        for log in logs:
            l = log.split()
            if not l[1].isdigit():
                letter_logs.append(log)
            else:
                num_logs.append(log)
        letter_logs = sorted(letter_logs, key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + num_logs

