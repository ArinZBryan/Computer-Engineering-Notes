### Equivalence
To prove that $P \implies Q \iff (Q' \implies P')$, you must prove exhaustively that all cases of the first statement result in the value from the second statement. 
> [!info] The Contrapositive
> The contrapositive, shown above on the right hand side of the equation, can be proved to identically equal to the original statement, shown on the left hand side of the equation. Thus, for any statement, if we can prove the contrapositive, we also prove the original statement. This is most commonly done when using proof by contradiction.
##### De Morgan's Law
$¬(A\wedge B) = ¬A \vee ¬B$
$¬(A\vee B) = ¬A \wedge ¬B$

### Predicates
A predicate is to a proposition as a function is to an equation, ie. it is missing information before it can be evaluated. For example, "$x$ is even" is a predicate: we cannot say if this is true or false if we do not know $x$. Thus, we notate this like a function: $P(x) = x \text{ is even}$. To turn this into a proposition, we must specify $x$. For example, $P(12)$, *is* a proposition, as we have given a value to test to the predicate.
##### Turning into propositions
It is possible to take an arbitrary predicate and turn it into a proposition by using one of two quantification methods:
- For all ($\forall x$) - This means that 'for all $x$, evaluate the predicate to the right'. For example: $P = \forall xA(x) \implies B(x)$ translates to the proposition "For all values of $x$, $A(x)$ implies $B(x)$"
- For some ($\exists x$) - This means that 'for some $x$, evaluate the predicate to the right'. For example: $Q = \exists xC(x)$ - This means that 'there exists some value of x, such that $C(x)$ is true'.
> It is important to note that $¬\forall = \exists$

### Sequent (Optional)
A *valid argument* consists of a finite set of propositions ($P_1, P_2, \dots, P_n$) that are called premises, together with a further proposition $C$, the conclusion, such that $P_1 \wedge P_2 \wedge \dots \wedge P_n \implies C$ is true (is a tautology). If an argument is not valid, then we say it is an *invalid argument*.
There are a few ways of properly notating this: 
- Linear Notation: $P_1, P_2, \dots, P_n \vdash C$
	E.g. $A, A\implies B \vdash B$
- Gentzen System: $\frac{P_1 \space P_2 \space \dots \space P_n}{C}$
	E.g. $\frac{A\space\space\space A\implies B} {B}$
- Fitch System: We don't care about this one.
To prove any given argument, we must show that it is a tautology. To do this, we must prove that all the propositions and'ed together implies the conclusion results in a tautology.
For example