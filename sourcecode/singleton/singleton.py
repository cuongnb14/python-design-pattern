class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SlackConnection:
    __metaclass__ = Singleton


sc1 = SlackConnection()
sc2 = SlackConnection()


print(sc1)
print(sc2)