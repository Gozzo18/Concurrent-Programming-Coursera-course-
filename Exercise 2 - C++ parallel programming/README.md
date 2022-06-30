# Introduction to Parallel Programming with C and Python Module
One of this module's assignment will assess the student's ability to implement a simple parallel programming algorithm.

The goal of this assignment is for the student to create a C++-based implementation of the ticketing parallel programming algorithm. Students will be furnished with a base assignment.cpp and assignment.h, which will hold the scaffolding for implementing a ticketing algorithm with the C++ standard library's thread library. There is code within the base .cpp file that outputs logging of thread activity to a text file, it must be executed before and after each thread has executed, ensuring that all threads complete their participation in the ticketing system, in a parallel manner.

## Assignment Instructions
1. Write C++ code in assignment.cpp and assignment.h to implement a simple ticketing system.  Ensure that the variable USERNAME should be your username.
2. Update .user to include only one line with the username from above.
3. Install all required packages by running ```make clean build```.
4. Execute the code via ```sh run.sh -n num_threads -u username uSrKD```.