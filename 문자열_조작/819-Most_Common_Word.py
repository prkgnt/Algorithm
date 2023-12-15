from typing import List
from collections import defaultdict
import re
class Solution(object):
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        li = []
        # 정규문자를 제외한 나머지를 공백으로 치환하는 방법
        # re.sub("[^\w]"," ", paragraph).lower().split()
        for word in re.split("[!?',;.]", paragraph):
            li.extend(word.split())
        cnt = defaultdict(int)
        for word in li:
            w = word.lower()
            if w not in banned:
                cnt[w] += 1
        return max(cnt, key=cnt.get)

