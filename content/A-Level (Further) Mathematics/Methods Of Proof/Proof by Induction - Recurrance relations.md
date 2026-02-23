## The Method

This method of proof by induction is used for questions of the form:

$U_1 = x$ and $U_{n+1} = f(U_n)$  
Prove by induction that $U_n = g(n)$

There are several steps to this proof:
1. Prove $U_n = g(n)$ true for $n = 1$
2. Assume $U_k = g(k)$ (This is the same as saying '*Assume $U_n = g(n)$ is true for $n=k$*')
3. Substitute in $k+1$ ($U_{k+1} = f(U_k)$)
4. Rearrange to be in the same form as $g(n)$, except all instances of $n$ are replaced by $k+1$.
5. As this is true for $n = 1$, and true for $n = k+1$, this is true for all $n \in \mathbb{N}$.
6. You have proved the statement via induction.

## An Example
### Question
Given $u_1 = 8$ and $u_{n+1} = 4u_n - 9n$, prove $u_n = 4^n + 3n + 1$

### Step 1
$u_1 = 4^1 + 3(1) + 1$  
$u_1 = 4 + 3 + 1$  
$u_1 = 8$  
$\checkmark$ True for $n=1$

### Step 2
Assume $u_n = 4^n + 3n + 1$ true for $n=k$.  
$u_k = 4^k + 3k + 1$

### Step 3
$u_{k+1} = 4(u_k) - 9k$  
$u_{k+1} = 4(4^k + 3k + 1) - 9k$  

### Step 4
$u_{k+1} = 4^{k+1} + 12k + 4 - 9k$  
$u_{k+1} = 4^{k+1} + 3k + 4$  
$u_{k+1} = 4^{k+1} + 3(k+1) + 1$  
> In the last part of this step, $3k + 4$ is rearranged into $3(k+1) + 1$. This does not appear to be a normal thing to do, but, if guided by the question, and what it is asking you to prove, it becomes far more understandable.

### Step 5
$\checkmark$ True for $n=k+1$ if true for $n=k$.  
$\therefore$ True for all $n \in \mathbb{N}$.  

### Step 6
$\therefore$ $u_n = 4^n + 3n + 1$ must be true.