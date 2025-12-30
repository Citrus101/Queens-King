
nice = 0;
n = []
def func():
    n.append(1)
    
def foo():
    # global nice
    nice = 10
    func();
    
foo()
print(n)