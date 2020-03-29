# shortest-path-triangle

Minimum-sum descent Some positive integers are arranged in an equilateral triangle with n numbers in its base like the one shown in the figure below for n = 4. The problem is to find the smallest sum in a descent from the triangle apex to its base through a sequence of adjacent numbers (shown in the figure by the circles). Design a dynamic programming algorithm for this problem and indicate its time efficiency.

Empirical Investigation of Three Algorithms for the Minimum-Sum Descent Problem

The problem in question is stated in Exercises 8.1 of the textbook.  As most algorithmic problems, it can be solved by different algorithms, including:
•	Brute force
•	Dynamic Programming
•	Dijkstra’s shortest path algorithm 

Note 1: You can do any or all parts of this project.  An extra credit will be given independently for each of the three parts of it.

Note 2: You can use any code you may find on the Internet for your programs.  But you must clearly indicate its source in your submission. 

The input to each of these algorithms will be a positive integer n specified from the keyboard.  The n(n+1)/2 numbers composing an input triangle are to be generated randomly in the range [1, n2] top-down left-to-right. The output will be a list of n numbers composing a shortest path from the triangle’s apex to it its bottom row. 

Part I  
(a)	Write a program implementing a brute-force (exhaustive search) algorithm for this problem.

(b)	Indicate the order of your algorithm’s time efficiency based on the theoretical grounds.  Justify your answer.

(c)	Run your algorithm on a sequence of n’s values to obtain a scatterplot like those in Section 2.6 of the textbook.  Discuss whether your empirical data agree with your theoretical answer given above.

(d)	Experiment with your program to find the largest value of n for which it can solve the problem in 1 minute on your computer.

(e)	Estimate the largest value of n for which it will be able to solve the problem in 24 hours and in one year.  Justify your answers. 


Part II 
(a)	Write a program for solving this problem by dynamic programming.

Answer questions (b)-(e) about this algorithm. 


Part III
(a)	Write a program for solving this problem by applying Dijkstra’s shortest path algorithm. (You’ll have to transform the problem first to make it possible.)

Answer questions (b)-(e) about this algorithm. 

Note 1: You can do any or all three parts of this project.  An extra credit will be given independently for each of the three parts of it.

Note 2: You can use any code you may find on the Internet in your programs with no detriment to your extra points.  But you must clearly indicate its source in your submission.

Note 3: You must work by yourself.  (It is not a group project.)

Note 4: Each of the three parts, if done perfectly, will add 4 points to your final grade.

You will email me the following:
. Your source and executable files with clear directives how your programs are supposed to be executed.   (Keep electronic copies of your files until I grade your projects and inform you about the extra points assigned.)
. A description of the way you’ve tested your programs including specific inputs and corresponding outputs.  (Test your programs thoroughly, including “special” and “extreme” inputs.)
. Your answers to the questions posed above with appropriate justifications and explanations.

