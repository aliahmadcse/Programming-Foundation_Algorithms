# use recursion to implement a count down


def countDown(x):
    if x == 0:
        print("Done")
        return
    print(x, "...")
    countDown(x-1)
    print("foo")


countDown(5)
