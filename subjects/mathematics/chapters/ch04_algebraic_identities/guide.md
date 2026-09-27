# Chapter 4: Exploring Algebraic Identities

> 👨‍🏫 **Teacher's Overview:** An algebraic identity is an algebraic equation that holds true for **all possible values** of its variables. Identities are the power tools of mathematics: they turn complex arithmetic into mental math, allow rapid factorization of high-degree polynomials, and appear in almost every section of the CBSE Class 9 exam.

---

### 1. The Core 8 CBSE Algebraic Identities

Master these eight formulas until they become second nature:

| No. | Identity | Form / Use Case |
| :--- | :--- | :--- |
| **I** | $(x + y)^2 = x^2 + 2xy + y^2$ | Square of a sum |
| **II** | $(x - y)^2 = x^2 - 2xy + y^2$ | Square of a difference |
| **III** | $x^2 - y^2 = (x - y)(x + y)$ | Difference of squares (fast mental math) |
| **IV** | $(x + a)(x + b) = x^2 + (a + b)x + ab$ | Product of binomials with common term |
| **V** | $(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx$ | Square of a trinomial |
| **VI** | $(x + y)^3 = x^3 + y^3 + 3xy(x + y)$ | Cube of a sum ($x^3 + 3x^2y + 3xy^2 + y^3$) |
| **VII** | $(x - y)^3 = x^3 - y^3 - 3xy(x - y)$ | Cube of a difference ($x^3 - 3x^2y + 3xy^2 - y^3$) |
| **VIII**| $x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)$ | Sum of three cubes |

---

### 2. High-Yield Derived Cubes Identities

From Identities VI and VII, we obtain the factorization formulas for the sum and difference of two cubes:

$$\mathbf{x^3 + y^3 = (x + y)(x^2 - xy + y^2)}$$
$$\mathbf{x^3 - y^3 = (x - y)(x^2 + xy + y^2)}$$

> ⚠️ **Exam Trap:** Watch the middle signs inside the quadratic bracket:
> - For $x^3 + y^3$, the middle sign is **negative**: $(x^2 - xy + y^2)$.
> - For $x^3 - y^3$, the middle sign is **positive**: $(x^2 + xy + y^2)$.

---

### 3. The Conditional Identity (CBSE Favorite!)

From Identity VIII:
$$x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)$$

$$\mathbf{\text{If } x + y + z = 0, \quad \text{then } x^3 + y^3 + z^3 = 3xyz}$$

**Example:** Evaluate $(-12)^3 + (7)^3 + (5)^3$ without calculating actual cubes:
Let $x = -12, y = 7, z = 5$.
Check the sum: $x + y + z = -12 + 7 + 5 = 0$.
Since $x + y + z = 0$:
$$(-12)^3 + 7^3 + 5^3 = 3(-12)(7)(5) = 3 \times (-12) \times 35 = -36 \times 35 = \mathbf{-1260}$$

---

### 4. Step-by-Step Evaluation Problem (From School PA-2 Q30)

**Problem:** If $2x + 3y = 13$ and $xy = 6$, find the value of $8x^3 + 27y^3$.

**Solution Method:**
1. Recognize that $8x^3 = (2x)^3$ and $27y^3 = (3y)^3$.
2. Take the cube of both sides of $2x + 3y = 13$:
   $$(2x + 3y)^3 = 13^3$$
3. Use Identity VI: $(a + b)^3 = a^3 + b^3 + 3ab(a + b)$:
   $$(2x)^3 + (3y)^3 + 3(2x)(3y)(2x + 3y) = 2197$$
4. Simplify terms:
   $$8x^3 + 27y^3 + 18(xy)(2x + 3y) = 2197$$
5. Substitute the known values $xy = 6$ and $2x + 3y = 13$:
   $$8x^3 + 27y^3 + 18(6)(13) = 2197$$
   $$8x^3 + 27y^3 + 1404 = 2197$$
6. Subtract 1404:
   $$8x^3 + 27y^3 = 2197 - 1404 = \mathbf{793}$$
