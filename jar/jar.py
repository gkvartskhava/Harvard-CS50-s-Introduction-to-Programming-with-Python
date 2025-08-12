
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if (n > self.capacity) or ((n + self.size) > self.capacity):
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    num = int(input('enter number: '))
    cookie = Jar()
    cookie.deposit(num)
    print(cookie._size)

if __name__ == "__main__":
    main()


