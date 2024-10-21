The *cardinality* of a set, denoted by $|X|$ or $\text{card } X$, is the length of the set. However, sets have no guarantee of being finite, so there are also some extra possible values.
##### Special Values
If a set has a cardinality of 1, we call it a *singleton*. 
If a set has the same cardinality as $\mathbb{N}$, then we say it's cardinality is *countably infinite*, which we denote using the symbol $\aleph_0$.
If a set has the same cardinality as $\mathbb{R}$ in the range $[0,1]$, then we say its cardinality is *uncountably infinite*, which we denote using the symbol $\aleph_1$.

Despite the fact that $\aleph_0$ and $\aleph_1$ are both types of infinity, we can always say that $\aleph_1 \gt \aleph_0$. There are more real numbers between 1 and 0 inclusive than there are positive integers full stop.

> [!example]- Examples of cardinality
> $A = \{\}$, then $|A| = 0$
> $A = \{\varnothing\}$, then $|A| = 1$
> $A = \{1\}$, then $|A| = 1$
> $A = \{1, \{2, 3\}\}$, then $|A| = 2$
> $A = \{1, \varnothing\}$, then $|A| = 2$
> $A = \{1, 1, 1\}$, then $|A| = 1$
> $A = \{1, 2, 3\}$, then $|A| = 3$
> $A = \{1, \{2,3\}, \{2,2,3\}\}$, then $|A| = 2$

If there exists a [bijective function](./Functions.md#Types%20of%20Function) between to sets $A$ and $B$, we say that $|A| = |B|$. This follows naturally from the definition of bijective, in that every element in $B$ must be mapped to by something, and every element in $A$ must map to a unique element in $B$. Thus, the cardinality of $A$ and $B$ must be equal for a bijective function mapping $A$ to $B$ to exist.
##### More Dimensions
Though unintuitive, it is possible to prove that $|\mathbb{N}| = |\mathbb{N}\times\mathbb{N}|$. To do this, we can use *Cantor's Diagonal Argument*. By using a single space-filling line, we can concatenate all the ordered pairs in the 2D plane into a single line. Thus, we have found a bijection between $\mathbb{N}$ and $\mathbb{N}\times\mathbb{N}$.
![Cantor's Diagonal Argument](images/Cantor's%20Diagonal%20Argument.png)
It is also possible to use a Peano curve to achieve the same end.
Furthering this technique, it is possible to extend it to all dimensions. That is $|\mathbb{N}| = |\mathbb{N}\times\mathbb{N}\times\mathbb{N}|$ and $|\mathbb{N}| = |\mathbb{N}\times\mathbb{N}\times\mathbb{N}\times\dots|$
### Cantor's Diagonal Argument
Cantor's diagonal argument is a proof that $|\mathbb{N}| < |[0,1]|$. That is, there are more real numbers between 0 and 1 inclusive than there are natural numbers. The proof is as follows.

For the sake of [contradiction](./Proof.md#Proof%20By%20Contradiction), construct a table where each row contains the infinite number of digits representing the decimal expansion of each real value between 0 and 1 inclusive. (This means a number like 0.1 is represented as 0.10000000...)
![Example Table](Pasted%20image%2020241021152555.png)