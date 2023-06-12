def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce #to add decorator
def hello():
    print("Hello, World")

hello()