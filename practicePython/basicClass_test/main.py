item1 = {"note", "notebook", "sketch"}
item2 = {"note", "aaa", "bbb"}
item = item2 ^ item1
print(item)

temp = [v for v in range(10)]
print(temp)

increment = lambda num: num + 1;
print(increment(2))

nums = ["one", "two", "three"]
filtered = filter(lambda x: len(x) == 3, nums)
print(tuple(filtered))

class User:
    def __init__(self, name: str, id: int) -> None:
        """
        Test code

        :param name: user name
        :param id: user id
        """
        self.name: str = name
        self.id: int = id

    def change_id(self, id: int) -> None:
        """
        Change user id

        :param id: user id
        """
        self.id = id

    def change_name(self, name: str) -> None:
        """
        Change user name

        :param name: user name
        :return:
        """

if __name__ == '__main__':
    u: User = User("temp", 5)
    u.change_id(1)
    print(type(u.name))
    print(u.name)
