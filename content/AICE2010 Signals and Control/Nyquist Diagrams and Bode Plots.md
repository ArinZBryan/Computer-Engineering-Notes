Throughout the development of filters, controllers and systems, it is often useful to be able to represent systems graphically. There are generally two ways in which this is done - Nyquist Diagrams and Bode Plots. These two methods show broadly similar information, but are used in different scenarios.

### Nyquist Diagrams
Consider a stable system $g(t)$ with [transfer function](./Transfer%20Functions.md) $G(s)$. If we pass the input $x(t) = M\sin(\omega t + \phi)$, then the output function $f(t)$ would be as follows:
$$y(t) = M|G(j\omega)|\sin(\omega t + \phi + \angle G(j\omega))$$
Where $G(j\omega)$ is the [frequency response](./Fourier%20Transforms.md#Using%20the%20Fourier%20Transform%20on%20LTI%20Systems) of the system $g$. Note that in this case, it is valid to reduce our remit down to the frequency response only from the transfer function because:
- We know the system is stable, so its transient response must decay to zero and we make the assumption that we are already at steady-state.
- We are driving the system with a sinusoid
This means that the transfer function naturally reduces to the frequency response.

For a given angular frequency $\omega$, $G(j\omega) = a(\omega) + jb(\omega)$. We can then plot the locus of $G(j\omega)$ with $\omega \in (-\infty, \infty)$ onto an argand diagram, since $a(\omega)$ and $b(\omega)$ are real polynomials in $\omega$. The locus of the point $a(\omega) + jb(\omega)$ can provide useful information about the system being plotted.
##### Sketching Nyquist Diagrams
===TODO===

> [!example] Nyquist Diagram of $G(s) = \frac{1}{s+1}$
> ![](images/Nyquist%20Plot%201%20div%20(s+1)(s+2).png)

### Bode Plots
Bode plots represent the frequency response of a system using two plots, one for gain and one for phase. 

Specifically, the plots are of:
- Gain
	- X axis: Angular Frequency ($\omega$)
	- Y axis: Logarithm of Gain ($20\log_{10}\left(|G(j\omega)|\right)$)
- Phase
	- X axis: Angular Frequency ($\omega$)
	- Y axis: Phase Shift ($\angle G(j\omega)$)
##### Plotting Bode Plots
Plotting and sketching bode plots use pretty much the same method - brute force tabulation. That is, you algebraically simplify the logarithmic gain and phase shift formulas, then plug in values of $\omega$ to get points on the respective plots. From this, you then join them up. 

> [!example] Bode Plot of $G(s) = \frac{1}{(s+1)(s+2)}$
> ![](images/Bode%20Plot%201%20div%20s+1.png)