class TimeMap:

    def __init__(self):
        self.people = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.people:
            self.people[key].append([timestamp, value])
        else:
            self.people[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.people:
            return ""
        ss = self.people[key]
        l, r = 0, len(ss) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if ss[mid][0] == timestamp:
                return ss[mid][1]
            elif timestamp < ss[mid][0]:
                r = mid - 1
            else:
                res = ss[mid][1]
                l = mid + 1
        return res