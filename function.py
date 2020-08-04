def outer():
    print("it is outer function")
    def inner():
        print("inner function")
    inner()
outer()
