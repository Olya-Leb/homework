import inspect

def introspection_info(obj):
    info = {
        "type" : type(obj),
        "attributes" : [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        "methods" : [method for method in dir(obj) if callable(getattr(obj, method))],
        "module" : inspect.getmodule(obj)
    }
    return info

class SomeClass:

    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        return self.attribute_1

def main():

    some_object = SomeClass()

    number_info1 = introspection_info(42)
    print(number_info1)

    number_info2 = introspection_info(some_object)
    print(number_info2)

if __name__ == "__main__":
    main()