#!/usr/bin/python


def spam(n):
    assert n >= 10, "Given number is less than 10"
    print "Given number is : ", n


if __name__ == "__main__":
    spam(30)
    spam(10)
    spam(6)
    spam(40)
