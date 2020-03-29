# shortest-path-triangle

Minimum-sum descent Some positive integers are arranged in an equilateral triangle with n numbers in its base like the one shown in the figure below for n = 4. The problem is to find the smallest sum in a descent from the triangle apex to its base through a sequence of adjacent numbers (shown in the figure by the circles). Design a dynamic programming algorithm for this problem and indicate its time efficiency.

<p align="center">
  <img src="https://github.com/ThapaRahul/shortest-path-triangle/blob/master/tree.png">
</p>

Empirical Investigation of Three Algorithms for the Minimum-Sum Descent Problem

As most algorithmic problems, it can be solved by different algorithms, including:
- Brute force
- Dynamic Programming
- Dijkstra’s shortest path algorithm 

**Note 1**: You can do any or all parts of this project.  An extra credit will be given independently for each of the three parts of it.

**Note 2**: You can use any code you may find on the Internet for your programs.  But you must clearly indicate its source in your submission. 

The input to each of these algorithms will be a positive integer n specified from the keyboard.  The n(n+1)/2 numbers composing an input triangle are to be generated randomly in the range [1, n<sup>2</sup>] top-down left-to-right. The output will be a list of n numbers composing a shortest path from the triangle’s apex to it its bottom row. 

**Part I** 

-	Write a program implementing a brute-force (exhaustive search) algorithm for this problem.

-	Indicate the order of your algorithm’s time efficiency based on the theoretical grounds.  Justify your answer.

-	Run your algorithm on a sequence of n’s values to obtain a scatterplot. Discuss whether your empirical data agree with your theoretical answer given above.

-	Experiment with your program to find the largest value of n for which it can solve the problem in 1 minute on your computer.

-	Estimate the largest value of n for which it will be able to solve the problem in 24 hours and in one year.  Justify your answers. 


**Part II** 

-	Write a program for solving this problem by dynamic programming.

Answer questions (b)-(e) about this algorithm. 


**Part III**

-	Write a program for solving this problem by applying Dijkstra’s shortest path algorithm. (You’ll have to transform the problem first to make it possible.)

Answer questions (b)-(e) about this algorithm. 
