class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Creating objects
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)   # Output: True
print(id(obj1))
print(id(obj2))