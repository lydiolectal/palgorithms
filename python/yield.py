def fib():
	x = 0
	y = 1
	while True:
        # why does moving 'yield' to end result in error?
		x, y = y, x + y
		yield y

def addOne(x):
    while True:
        yield x
        x = x + 1

if __name__ == "__main__":
    f = fib()
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())

    # x = addOne(5)
    # print(x.__next__())
    # print(x.__next__())
