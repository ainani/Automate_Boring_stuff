You see, the proper use of assertions is to inform developers about
unrecoverable errors in a program. Assertions are not intended to
signal expected error conditions, like a File-Not-Found error, where
a user can take corrective actions or just try again.
Assertions are meant to be internal self-checks for your program. They
work by declaring some conditions as impossible in your code. If one
of these conditions doesn’t hold, that means there’s a bug in the program.
If your program is bug-free, these conditions will never occur. But if
they do occur, the program will crash with an assertion error telling
you exactly which “impossible” condition was triggered. This makes
it much easier to track down and fix bugs in your programs. And I like
anything that makes life easier—don’t you?
For now, keep in mind that Python’s assert statement is a debugging
aid, not a mechanism for handling run-time errors. The goal of using
assertions is to let developers find the likely root cause of a bug more
quickly. An assertion error should never be raised unless there’s a bug
in your program.



Assertion checking can be stopped by using -O option in command line
 - Means assertion will be compiled but not evaluated


1. Assertion should not be used for data validation
  - Because if assertion is disabled during execution it will be a security threat in few cases. like : checking for admin user or checking if a product really exist in list before deleting it
2. Assert syntax, 
   assert(1==2, 'This will never fail') 

   This assert will never fails as it will not evaluate to False any time.
   In Python any non-empty tuple is considered as True only. So above assert will never fails



 - Python’s assert statement is a debugging aid that tests a condition as an internal self-check in your program.
 - Asserts should only be used to help developers identify bugs. They’re not a mechanism for handling run-time errors.
 - Asserts can be globally disabled with an interpreter setting
