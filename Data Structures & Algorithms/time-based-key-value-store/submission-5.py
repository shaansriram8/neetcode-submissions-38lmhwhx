class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        final_time = 0
        final_value = ""
        if key in self.store:
            for pair in self.store[key]:
                if pair[0] <= timestamp:
                    final_time = pair[0]
                    final_value = pair[1]
            return final_value
        return ""


