class MyHashSet:

    def __init__(self):
        self.container = []

    def add(self, key: int) -> None:
        self.container.append(key)

    def remove(self, key: int) -> None:
        while key in self.container:
            self.container.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.container


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)