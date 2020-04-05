#Integral and Derivatives
 1) Develop an algorithm which, for a given function f(x), interval bounds a and
b with a < b, and a prescribed number of subintervals n, applies the multiple
application trapezoidal rule to approximate the integral Z b a f(x) dx.

* Enter the desired function into the method called "Function". Enter the bound into variables a and b

2) Develop an algorithm which, for a given function f(x), interval bounds a and b
with a < b, and a prescribed number of subintervals n, approximates the integral
Z b a f(x) dx according to the following procedure: (a) If n = 1, it applies the trapezoidal rule.
(b) If n is even, it applies the multiple application Simpson’s 1/3 rule. (c) If n ≥ 3 and n is odd, it applies the multiple application Simpson’s 1/3 rule
on the first n − 3 subintervals, and applies the Simpson’s 3/8 rule on the last three subintervals. 

3) Develop an algorithm which, for a given function f(x), interval bounds a and b
with a < b, and error tolerance per subinterval tol, applies adaptive quadrature to
approximate the integral Z b a f(x) dx (based on the pseudocode that was presented 
in the recorded lectures and can be found on page 642 of the textbook).

4)  Apply the algorithms you developed in questions 1-3 above to approximate
Z 1 0 x 0.1 (1.2 − x)(1 − e 20(x−1)) dx, for varying values of n and tol. Note that this integral is not easy to evaluate
analytically! Using the true value of 0.602298, plot t as a function of n for
the algorithms you developed in questions 1 and 2, and plot t as a function of
tol for the algorithm you developed for question 3. Use your best judgement to
determine appropriate ranges of values for n and tol to be included in the plots.
