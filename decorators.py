def deco(fx):
    def inner():   
        print("Good Morning")
    fx()
    print("This is my first decorators")
    return inner

@deco
def hello():
    print("Hello coder")   

hello()