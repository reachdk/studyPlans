# Chapter 2: Introduction to Linear Polynomials

> 👨‍🏫 **Teacher's Overview:** A polynomial is an algebraic expression built from variables, constants, and the fundamental operations of addition, subtraction, and multiplication. The golden rule in Class 9: **The exponent of the variable must strictly be a whole number (0, 1, 2, 3...)!** In this chapter, we master degrees, coefficients, evaluating polynomials at given points, and finding the zeroes of linear polynomials algebraically and geometrically.

---

### 1. What is a Polynomial?

An expression of the form:
$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$$
where $a_n, a_{n-1}, \dots, a_0$ are real numbers (called **coefficients**), $a_n \neq 0$, and the powers $n, n-1, \dots$ are **non-negative integers (whole numbers)**.

| Expression | Is it a Polynomial? | Reason |
| :--- | :--- | :--- |
| $2x^3 - 5x + 7$ | **Yes** | Exponents of $x$ are 3, 1, 0 (all whole numbers). |
| $\sqrt{x} + 3$ | **No** | Power of $x$ is $1/2$ (a fraction, not a whole number). |
| $x + \frac{1}{x}$ | **No** | $1/x = x^{-1}$; power is $-1$ (negative integer). |
| $\sqrt{5}x^2 - 3x$ | **Yes** | The coefficient is irrational ($\sqrt{5}$), but power of $x$ is 2 (whole number). |
| $7$ | **Yes** | Constant polynomial: $7 = 7x^0$ (degree is 0). |

> ⚠️ **Exam Trap:** Coefficients can be square roots, fractions, or negative numbers (e.g. $\sqrt{3}x + \frac{2}{5}$ is valid). It is **only the exponent of the variable** that must never be a fraction, decimal, or negative!

---

### 2. Degree of a Polynomial

The **degree** of a non-zero polynomial is the **highest power of the variable** appearing in any term with a non-zero coefficient.

| Classification | Degree | Standard Form | Example |
| :--- | :--- | :--- | :--- |
| **Zero Polynomial** | **Undefined** | $0$ | $0$ (has no non-zero terms) |
| **Constant Polynomial** | **0** | $c \quad (c \neq 0)$ | $p(x) = -8 = -8x^0$ |
| **Linear Polynomial** | **1** | $ax + b \quad (a \neq 0)$ | $p(x) = 3x - 5$ |
| **Quadratic Polynomial** | **2** | $ax^2 + bx + c \quad (a \neq 0)$ | $p(x) = x^2 - 4x + 3$ |
| **Cubic Polynomial** | **3** | $ax^3 + bx^2 + cx + d \quad (a \neq 0)$ | $p(x) = 2x^3 - x^2 + 1$ |

---

### 3. Value of a Polynomial at $x = k$

If $P(x)$ is a polynomial in $x$ and $k$ is any real number, then the value obtained by substituting $x = k$ into $P(x)$ is denoted by $P(k)$.

**Example (from School PA-2 Exam):**
Evaluate $P(x) = x^3 - 10x^2 + 3x - 4$ at $x = -1$:
$$P(-1) = (-1)^3 - 10(-1)^2 + 3(-1) - 4$$
$$P(-1) = -1 - 10(1) - 3 - 4 = -1 - 10 - 3 - 4 = \mathbf{-18}$$

---

### 4. Zero of a Polynomial

A real number $k$ is called a **zero of a polynomial $P(x)$** if:
$$P(k) = 0$$

#### Key Rules for Zeroes:
1. A zero of a polynomial need not be the number 0. (For example, $P(x) = x - 2$ has zero $x = 2$).
2. 0 can be a zero of a polynomial. (For example, $P(x) = x^2$ has zero $x = 0$).
3. **Every linear polynomial has one and only one zero:**
   $$ax + b = 0 \implies x = -\frac{b}{a}$$
4. A polynomial of degree $n$ can have at most $n$ real zeroes.
5. **Geometrical meaning:** The zeroes of $P(x)$ are the $x$-coordinates of the points where the graph of $y = P(x)$ intersects the $x$-axis!

> 💡 **Simplifying Before Finding Zeroes:** To find zeroes of $p(x) = (x-2)^2 - (x+2)^2$, expand first:
> $$p(x) = [x^2 - 4x + 4] - [x^2 + 4x + 4] = -8x$$
> Set $-8x = 0 \implies x = 0$. Hence, the only zero is $x = 0$.
