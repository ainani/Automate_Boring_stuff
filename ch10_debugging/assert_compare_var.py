#!/usr/bin/python


def compare_var(var1, var2):
    assert var1.lower() == var2.lower(), "Both variables are having different strings"
    print "Both strings are equal in cases: ", var1, var2

if __name__ == "__main__":
    compare_var('test', 'TEST')
    compare_var('teSt', 'TesT')
    compare_var('TEst', 'test')

    compare_var('T Est', 'test')       ### Assertion starts from here
    compare_var('TEst ', 'test')
    compare_var('TEst1', 'test')
