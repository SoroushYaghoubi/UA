UA
===

# v.2:
## Intro
There is a quite new field in mathematics called Tropical Geometry. There are several ways you could define or explain what it is. But since we are already in the context of p-adics let's start building the idea from bottom up together in a way that would make sense rather than taking a formal defintion out of thin air.

Before we continue I assume you are familiar with some properties and tools used in the p-adic world. But let's do a half intuitive half mathematical recap what these tools are.

First of all there are several ways you could visualize a mathematical object. The type of visualization that would benefit us in this specific topic would be this one: imagine a Matrioshka-like structure where there are infinite spheres fractally nested inside of each other.

A certain operation that we like to be able to do on this object is "peeling" each ball. This peeling would first of all take us one level deeper into this infinite layers starting from 0. Second of all it reveals to us all the numbers that are divisable by p to the power of the layer we just revealed. For example opening the 0-th ball would show us every number that is divisable by $p^0$ and opening the 3d layer would show us all the numbers divisable by $p^3$. It is important to mention that each layer also contains all the possible residues of the division by that power of p. For example the 3d layer not only contains all of numbers that are multiplies of $p^3$ but also all the possible numbers that would have a residue in their division by $p^3$.

The usual visualization of the p-adics is like this image below where each sphere contains p spheres inside of it where each sphere represents a different residue in their division by p. To emphasize again on this property: out of one of these p spheres, there is always one of them that contains all the numbers divisable by a power of p, i.e. residue 0. 

But one piece of information that is lost in this sort of visualization is that going into this single sphere, would also mean going one layer deeper in the p-adic ladder.

![](https://md.fachschaften.org/uploads/1dc57b06-6cf8-415b-bfc3-75535efc3265.png)

In fact this operation of peeling aka going one layer deeper into this sphere is so important that there is a function defined just for that called the valuation function. This valuation function that is noted as $v_p$ is in essence counting how many times you have to "peel" before you can find your current number.

As an example take number 36 in the 3-adics. The "valuation" of this number is $v_3(36)=v_3(3^{\boxed{2}} \times 4)=2$ because the highest power of 3 that divides 36 is 2. More intuitively speaking this means that number 36 is not findable in the 0th layer and not in the 1st layer but after we open 2 balls.

Before we continue we have to also mention some small details. The valuation of number 0 is by convention infinity and for us that means we can only find 0 in by peeling infinite times. 
Also the valuation function is extended and defined on all rational numbers with the same idea and also it ignores the sign of the number. For example number $-\frac{15}{36}$ would have the valuation $\frac{3^1 \times 5}{3^2 \times 4} = 3^{\boxed{-1}} \times \frac{5}{4}=-1$. What this topologically means is beyong this introduction but think if it as doing the opposite of peeling.

## Tropical Geometry
Now as the next step we will play around with some properties of the valuation mechanically. In simplest terms what happens when we try to find the valuation of two numbers multiplied or added together? 

Let's take two numbers x and y. Per definition we can write them as $\boxed{x=p^{v_p(x)} \times a}$ and $\boxed{y=p^{v_p(y)} \times b}$. We will also use these short notations: $m:=\min(v_p(x), v_p(y))$ and $M:=\max(v_p(x), v_p(y))$. Also we sometimes use capital letters for the valuation of a variable for example $X := v_p(x)$ and 

Take a look at these two properties:
$\qquad v_p(x \times y) \qquad = \qquad v_p(p^{\boxed{v_p(x) + v_p(y)}} \times ab) \qquad = \qquad v_p(x)+v_p(y)$
$\qquad v_p(x+y) \qquad = \qquad v_p(p^{v_p(x)}a + p^{v_p(y)}b) \qquad \qquad \; = \qquad \qquad ??$

It is not hard to see why the first property holds and the least we can say is that it is pretty nice. 
But the second property looks a bit trickier. However if we were lucky and the valuations where not the same then we get exactly the $\min$imum of the two valuations. If we are unlucky and they are the same then the factors could possibly add up to make a larger valuation.
case $v_p(x) \neq v_p(y) \qquad \longrightarrow$ $$v_p(\;\; p^{m} (\boxed{p^{M-m}a + b}) \;\;)= \qquad m$$
case $v_p(x) = v_p(y) \qquad \longrightarrow$ $$v_p(\;\; p^{m} (\boxed{a + b})\;\;) \qquad \;\,\geq \qquad m$$

### *a revealing example*
Knowing all this we will now look at what happens if we apply the valuation function to this equation: $$x^2+3y=0$$
By taking the valuation of both sides we get $$v_3(x^2 + 3y)=v_3(0)=\infty$$

Let's take a step back and think what this means. This equation is asking us when exactly can the valuation of the sum of the individual terms be as big as possible. Well from what we have seen so far we know for sure that this is possible if and only if the valuation of the individual terms is equal. Otherwise the answer will stay finite. 
More concretely we first find the valuation of each term: $$v_3(x^2)=v_3(x \times x)=X+X=2X$$ $$v_3(3y)=v_3(3) + Y = 1+Y$$
A trick that mathematicians use here is that they draw $\min(2X, 1+Y)$. The folded line is exactly the solution space for when the valuations are the same (this is also why it is irrelevant if you use $\max$ or $\min$). **This is very useful because we reduced the space of all solutions from 2d to 1d and from a nonlinear one to a linear one.**

![](https://md.fachschaften.org/uploads/d8aebb23-6f02-4f22-ad21-93146652b528.png)
![](https://md.fachschaften.org/uploads/a3e00fe8-91c8-4959-9b31-27ffefc7f53a.png)

### *quick usecase*
A usecase for this is the Bézout's Theorem in Tropical Algebraic Geometry which says that the number of intersections between two tropical shapes is proportionate to the number of solutions to the initial system of equations. This is nice because not only our problem is changed completely from a nonlinear one to a combinatorics one.

- intersection of tropical polygons: ![](https://md.fachschaften.org/uploads/127988d5-3276-4ed5-b653-497833505914.png)

### *an overview*
In fact this technique of linearization is so powerful that it has a name: Tropicalization. The type of polynomials that are generated here always look like the minimum of several linear polynomials which are studied in the field of Tropical Algebra. The shapes created by them are also usually several lines connected with each other making tripod shapes which are studied in the Tropical Geometry which if not founded but formalized by a Brazilian mathematician called Imre Simon who named the field jokingly after his tropical ethnicity. :smiley: 

- usual shape of tropical polygons: ![](https://md.fachschaften.org/uploads/fce458ac-e06d-4f07-bf2f-7e495342468a.png)

Before we continue I would like to point out that what we did here had little to do with p-adics themselves but rather with two properties of the valuation function in p-adics. That is why tropicalization is a technique that is done in any mathematical space has such a valuation function with these two mentioned properties.

## ReLU: a tropical example
Another interesting field that could use Tropical Geometry is Neural Networks. In particular it is not always obvious what it means for a model to "learn" something. Formalizing such a field is hard and most of the work done is a kind of blackbox testing.

Let's do a quick recap on what a neural network is: imagine having an image. A neural network would read the pixels as the first or the input layer nodes and is expected to "learn" how to spit out the correct output. In the middle, there are commonly more layers, called hidden layers. Transfering data from a layer of nodes to the next is mostly a linear transformation. In fact a single transfer can be completely modelled as a matrix multiplication.
The problem is, if all each layer does it a linear transformation, then by the nature of linear systems, we can reduce the whole network into a single linear transformation with only an input and an output layer. This is obviously not what we are looking for because the distinction that needs to be done between different types of information is not as simple as a linear one. That is why after each linear transformation of a layer, we use a function that we call the "activation function", because it decides if or how much a neuron should be activated based on the previous nodes.

- ![](https://md.fachschaften.org/uploads/6a6f88af-03f6-4642-805e-3fcb993a24a0.png)
- ![](https://md.fachschaften.org/uploads/a4aef060-45a5-4e7f-b22d-11ba372e168d.png)

A widely used but oddly powerful activation function is in fact of tropical nature and it is called ReLU. ReLU is simply defined as $ReLU(x)=\max(0, x)$ and its main advantage is that it introduces nonlinearity, which enables complex learning patterns in the network. But unlike other activation functions it is a very well studied function thanks to tropical geometry.

![](https://md.fachschaften.org/uploads/650adbfa-0c00-44b7-81bf-43a38005cf10.png)

## Gaussians: a quick review
Even though the field of Tropical Geometry is quite a well studied field, it is in fact a new one and in order to make a stronger framework out of it especially in a way that can help analyse machine learning it needs to be extended further. And as we all know, machine learning is standing on the shoulders of statistics. It is only natural to study statistical phenomena under the lens of tropicalization. 

If we had to name one single most import tool of statistics, it would be the Gaussian distribution. It has many useful properties but three important properties of a Gaussian distribution would be:
1. Symmetrie and Invariance: this means geometrically that rotations don't change the distribution!
2. Independence: coordinates of a Gaussian event can be chosen independent and identically distributed.
3. Stability under linear transformations (like addition): Adding two normally distributed variables makes another normal distribution.

This third property is arguably the most important one of all, since it also yields the Central Limit Theorem. That is to say, if you do a statistical experiment many times, it acts asymptotically like a Gaussian!

## A Procedural Approach for Creating Tropical $p$-adic Gaussians
There seems to be no way to create a distribution such that all the three nice properties of the Gaussians hold. But if we compromise a bit there is a nice way in which the p-adic valuation can yield a distribution that has the third property: stability under linear transformations.

This is the research done by a statistician Steven N. Evans. He describes a procedure from which a distribution with this property is made.

He first takes a random variable $X$. Then he p-adically tropicalizes it. We have seen of course that this is not more than taking the valuation of the random variable $v_p(X)$. He then tries to find the probability of this value being a certain number s: $$\mathbb{P}(\;\;v_p(X)=s\;\;) \qquad = \qquad ?$$

But now we know how to interpret this: what is the probability of a number being found after peeling exactly s number of spheres? As we talked about earler we can only go one layer deeper if we open the sphere of the numbers divisable by the power of p. This means in each step out of the p spheres in front of us we can only open one of them. The probability of this is of course $1/p$. We then have to do this step s times which gives us $1/p^s$. After that we have to make sure that we don't end up going any deeper. This means choosing any sphere other than the one with numbers divisable by the power of p which is there is only one of them. This has of course the probabiliy $(1-1/p)$.

This overal probability is a geometric one which is studied well in statistics and is indeed closed under addition and scalar multiplication. $$(1/p^s)(1-1/p)$$

## Summary
we defined what tropicalization means in the context of p-adics. But we also showed that it is not specific to p-adics but rather makes sense for all non-Archimedean spaces with a valuation function with almost linear properties.
But we showed that by specifically using the p-adic interpretation of that valuation we can create a geometric distribution which has some properties that we like.
We can then for example go on and use this as a tool for creating random input for a neural network that uses ReLU without ever needing to exit the tropical context.

## Open Directions in Research


## References

