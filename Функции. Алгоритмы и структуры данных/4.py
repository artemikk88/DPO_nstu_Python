class Point:
    def __init__(self, data):
        self.data = data
        self.next = None


class Spisok:
    def __init__(self):
        self.size = 0
        self.head = None

    def insert(self, data, index):
        if index < 0 or index > self.size:
            return "Индекс вне диапазона"
        node = Point(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            previous = self.head
            for i in range(index - 1):
                previous = previous.next
            node.next = previous.next
            previous.next = node
        self.size += 1

    def get_data(self, index):
        if index < 0 or index >= self.size:
            return "Индекс вне диапазона"
        now = self.head
        for i in range(index):
            now = now.next
        return now.data

    def get_point(self, index):
        if index < 0 or index >= self.size:
            return "Индекс вне диапазона"
        now = self.head
        for i in range(index):
            now = now.next
        return now

    def delete(self, index):
        if index < 0 or index >= self.size:
            return "Индекс вне диапазона"
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            node = prev.next
            prev.next = node.next
        self.size -= 1

    def count(self):
        return self.size


def remove_duplic(lst):
    if lst.head is None:
        return 0
    count_removed = 0
    node = lst.head
    while node.next != None:
        if node.data == node.next.data:
            node.next = node.next.next
            lst.size -= 1
            count_removed += 1
        else:
            node = node.next
    return count_removed


list_1 = Spisok()
for i in range(5):
    list_1.insert(i+1, i)
list_1.insert(5, 5)
print(list_1.get_data(3))
print(list_1.get_point(3))
print(list_1.count())
list_1.delete(2)
print(list_1.count())
print(remove_duplic(list_1), list_1.count())
