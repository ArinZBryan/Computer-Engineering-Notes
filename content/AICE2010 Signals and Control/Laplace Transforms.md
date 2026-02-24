#maths/pure-maths/calculus/differential-equations
### Motivation
This motivation is broadly adapted from the motivation outlined [here](https://scholarship.claremont.edu/cgi/viewcontent.cgi?article=1009&context=codee)

When dealing with ODEs, it is often complex to solve them using the tools for dealing with derivatives and integrals. It would be convenient if we had some transform that we could put differential equations through that would transform taking derivatives into something easier, like multiplication. This is where the Laplace transform comes in, it happens to be such a transform.
##### Integral Transforms
An integral transform is a general way of transforming some function into another, that relies on the idea that [functions](../AICE1004%20Maths%20for%20AICE%20(1)/Foundation%20of%20Maths/Set%20Theory/Functions) can be considered vectors of infinite length, where the input to the function is simply and index into that vector. It uses integration of a function and a _kernel_ to produce a new function which we say has been transformed by an integral transform with the kernel.
$$F(s) = T(f) = \langle k(s) ,f\rangle=\int^{x=b}_{x=a}k(s, x)f(x)dx$$
We can the define a specific transform based on this by choosing a specific bounds of integration and kernel.

> [!note] Naming Conventions
> By convention, transformed functions are named as capitalised versions of the lower-case untransformed function

While it is not immediately obvious how this is useful, or that this has a well-defined inverse that we can use on the answer to our transformed problem, for the right bounds and kernel, it absolutely can.
##### Constructing the Laplace transform
To get a transform that does what we want, we set our goal to be that
$$T\left(\frac{d}{dx}f\right)=s\cdot T(f)$$
where $T$ is our transformation and $s$ is some arbitrary constant term.
Since, in general, we care about problems that are causal (IVPs), we can also add that we don't care about the value of $f$ before $t < 0$. 

Because of this choice of bounds, we can see that if we use an integral transform to produce our desired transformation, we will have to use an [improper integral](../A-Level%20(Further)%20Mathematics/Pure/Calculus/Integration/Improper%20Integrals) (from zero to infinity). Thus, to prevent having an infinite result, we can also surmise that the kernel times the function must decay to zero.
$$\lim_{t\to\infty}(k(s,t)f(t))=0$$
> [!note] Linear Combinations
> Due to properties of linear combinations, if any two functions satisfy the conditions above, any linear combination of the two will also satisfy the conditions.

Using the integral transform we defined earlier, we have that
$$\int^{t=\infty}_{t=0}k(s,t)\left(\frac{df}{dt}\right)dt=s\cdot\int^{t=\infty}_{t=0}k(s,t)(f)dt = \int^{t=\infty}_{t=0}s\cdot k(s,t)(f)dt$$
We can then perform [integration by parts](./../A-Level%20(Further)%20Mathematics/Pure/Calculus/Integration/Integration%20by%20Parts) on the left-most integral:
$$\int^{t=\infty}_{t=0}k(s,t)\left(\frac{df}{dt}\right)dt=[k(s,t)f(t)]^{t=\infty}_{t=0}-\int^{t=\infty}_{t=0}\left(\frac{\partial}{\partial t}k(s,t)\right)(f)dt$$
Since $\lim_{t\to\infty}k(s,t)f(t) = 0$, we can simplify to:
$$\int^{t=\infty}_{t=0}k(s,t)\left(\frac{df}{dt}\right)dt=-k(s,0)f(0)+\int^{t=\infty}_{t=0}-\left(\frac{\partial}{\partial t}k(s,t)\right)(f)dt$$
##### Finding the kernel
Ignoring the $k(s,0)f(0)$ term for the moment, we can see that for our transform to work, we must have that:
$$\int^{t=\infty}_{t=0}s\cdot k(s,t)(f)dt=\int^{t=\infty}_{t=0}-\left(\frac{\partial}{\partial t}k(s,t)\right)(f)dt$$
We can then easily simplify this
$$s\cdot k(s,t)(f)-\left(\frac{\partial}{\partial t}k(s,t)\right)(f)=0$$
$$s\cdot k(s,t)=-\left(\frac{\partial}{\partial t}k(s,t)\right)$$
$$\frac{\partial}{\partial t}k(s,t) = -s\cdot k(s,t)$$
Because $s$ is actually just a constant, this final equation is actually just a regular first ODE that we can solve analytically! Any solution to this equation will then be the kernel function that allows us to perform our desired transform.

>[!proof]- Solving the first order ODE
>$$\frac{\partial}{\partial t}k(s,t) = -s\cdot k(s,t)$$
>$$\partial k(s,t)=-s\cdot k(s,t)\partial t$$
>$$\frac{\partial k(s,t)}{k(s,t)}=-s\partial t$$
>$$\int \frac{1}{k(s,t)}dk(s,t)=\int-sdt$$
>$$\ln(k(s,t))=C-st\implies k(s,t)=e^{C-st}=e^C+e^{-st}$$
>In this case, we can disregard the constant term, so the solution is $e^{-st}$
##### Defining the Laplace Transform
Once the ODE is solved, we find that $k(s,t) = e^{-st}$. Thus, we can define the Laplace transform as the following:
$$F(s)=\mathscr{L}(f)=\int^{t=\infty}_{t=0}e^{-st}f(t)dt$$
Going back to the $k(s,0)f(0)$ term we ignored earlier, we can see that if we plug in our new kernel, we find the following property of the Laplace transform:
$$\mathscr{L}\left(\frac{d}{dt}f\right)=s\mathscr{L}(f)-f(0)$$
### Using the Laplace transform

https://tutorial.math.lamar.edu/Classes/DE/LaplaceIntro.aspx
https://tutorial.math.lamar.edu/Classes/DE/IVPWithLaplace.aspxhttps://tutorial.math.lamar.edu/Classes/DE/Laplace_Table.aspx
