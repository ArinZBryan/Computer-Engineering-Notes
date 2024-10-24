##### Special Symbols
If a proposition is created such that it fulfils itself, ie. it defines itself to be true, then it is called a *tautology*, denoted with the symbol $\top$. Conversely, if a proposition defines itself to be false, then it is called a *contradiction*, denoted with the symbol $\bot$. Here are some examples:
- "It is what it is" (Tautology)
- "To be or not to be" ($P \vee ¬P = \top$ - Tautology)
- "My sister is jealous of me because I am an only child" (Contradiction)
It is important to note the *liar paradox* (I am a liar / this statement is false) is not a contradiction, nor is it even a proposition. This is because it is both simultaneously true and false. By the law of the excluded middle, this precludes it from being a proposition.
### Implication
Given  the statement $P \implies Q$. $P$ is the *antecedent hypothesis* and $Q$ is the *consequent*. The $\implies$ symbol means 'if ... then MUST ...', more specifically, this means that if $P$ is true, then $Q$ **must be true**; there is no other outcome for $Q$ given $P$ is true. In the event that $P$ is false, we cannot truly take conclusions about $Q$. However, as this violates the law of the excluded middle, *we define $\implies$* to be true when the first part is false.
Like other operators, implication has a truth table:

| $P$ | $Q$ | $P \implies Q$        | $Q \implies P$        |
| --- | --- | --------------------- | --------------------- |
| 1   | 1   | 1                     | 1                     |
| 1   | 0   | 0                     | 1 (ex faso quodlibet) |
| 0   | 1   | 1 (ex faso quodlibet) | 0                     |
| 0   | 0   | 1 (ex faso quodlibet) | 1 (ex faso quodlibet) |
> [!info]- Ex Faso Quodlibet
> This is a latin phrase that directly translates to "from falsehood, anything". It is means here that given that $P$ is false, it would be meaningless to draw implications from it about $Q$, as is seen in the $P \implies Q$ column in the truth table above.
##### Necessary And Sufficient
If $P$ is sufficient for $Q$, then it means that $P \implies Q$, but also that there is choice (so it's not truly implication), in that $R \implies Q$ may also be true.
If $P$ is necessary for $Q$, then it means $P \iff Q$. There is no choice. It means exactly if $P$, then $Q$, *and* if $Q$ then $P$. In other words, the $\iff$ symbol is actually the same as the identity symbol ($\equiv$) used in other parts of mathematics.
##### The other way round
Here are some ways to manipulate some proposition

|                    |                   |
| ------------------ | ----------------- |
| Original Statement | if $P$, then $Q$  |
| Contrapositive     | if $¬Q$ then $¬P$ |
| Converse           | if $Q$ then $P$   |
| Inverse            | if $¬P$ then $¬Q$ |

It is always important to note that $P \implies Q \ne Q \implies P$. Put more specifically, this is saying that a statement is not necessarily equal to its converse. (This is true when $P \iff Q$).

