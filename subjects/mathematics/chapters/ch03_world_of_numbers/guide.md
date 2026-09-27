# Chapter 3: The World of Numbers

> 👨‍🏫 **Teacher's Overview:** The real number system is the foundation of all mathematics. In Class 9 CBSE, we explore the boundary between rational and irrational numbers through their decimal expansions, learn the indispensable technique of **rationalizing the denominator**, and master the **laws of exponents** with fractional powers.

---

### 1. Classification of Real Numbers ($\mathbb{R}$)

The collection of all Real Numbers consists of **Rational Numbers ($\mathbb{Q}$)** and **Irrational Numbers**:

```
                       Real Numbers (R)
                       /              \
             Rational (Q)           Irrational
             /          \           (√2, √3, π, e)
       Integers (Z)    Fractions (3/4, -2/5)
       /          \
Whole (W: 0,1,2..) Negative Integers (-1, -2..)
    |
Natural (N: 1,2,3..)
```

- **Rational Numbers ($\mathbb{Q}$):** Can be expressed as $\frac{p}{q}$, where $p, q \in \mathbb{Z}, q \neq 0$, and $\gcd(p, q) = 1$.
- **Irrational Numbers:** Cannot be written in the form $\frac{p}{q}$.

---

### 2. Decimal Expansions: The Definitive Test

| Type of Number | Nature of Decimal Expansion | Examples |
| :--- | :--- | :--- |
| **Rational Number** | **Terminating** | $\frac{1}{2} = 0.5$, $\frac{7}{8} = 0.875$ (Denominator has prime factors $2^m 5^n$) |
| **Rational Number** | **Non-terminating Recurring (Repeating)** | $\frac{1}{3} = 0.\overline{3}$, $\frac{1}{7} = 0.\overline{142857}$ |
| **Irrational Number** | **Non-terminating Non-recurring** | $\sqrt{2} = 1.41421356\dots$, $\pi = 3.14159265\dots$, $0.1010010001\dots$ |

> ⚠️ **Exam Trap:** $\pi$ is **irrational**! The fraction $\frac{22}{7}$ and decimal $3.14$ are only convenient rational approximations used for calculations, but the true value of $\pi$ has a non-terminating, non-recurring decimal expansion.

---

### 3. Converting Recurring Decimals to $p/q$ Form

**Standard Method:**
To express $x = 0.\overline{6} = 0.6666\dots$ in $p/q$ form:
1. Let $x = 0.6666\dots$  --- (1)
2. Multiply by $10$ (since 1 digit repeats):
   $$10x = 6.6666\dots$$ --- (2)
3. Subtract (1) from (2):
   $$10x - x = 6.6666\dots - 0.6666\dots \implies 9x = 6 \implies x = \frac{6}{9} = \mathbf{\frac{2}{3}}$$

**Predicting Multiples (from School PA-2 Q38):**
Given $\frac{1}{7} = 0.\overline{142857}$, find $\frac{6}{7}$:
$$\frac{6}{7} = 6 \times \frac{1}{7} = 6 \times 0.\overline{142857} = \mathbf{0.\overline{857142}}$$
*(Notice the cyclical permutation of the digits: 1-4-2-8-5-7).*

---

### 4. Operations on Real Numbers & Rationalizing the Denominator

- **Sum/Difference:** Rational $\pm$ Irrational = **Irrational** (e.g., $3 + \sqrt{2}$ is irrational).
- **Product/Quotient:** Non-zero Rational $\times$ Irrational = **Irrational** (e.g., $2\sqrt{3}$ is irrational).
- **Product of two irrationals:** Can be rational or irrational ($\sqrt{2} \times \sqrt{2} = 2$ [rational], but $\sqrt{2} \times \sqrt{3} = \sqrt{6}$ [irrational]).

#### Rationalizing the Denominator:
When an expression has an irrational radical in the denominator, multiply numerator and denominator by its **rationalizing factor (conjugate)**:
$$\frac{1}{\sqrt{a} + \sqrt{b}} \times \frac{\sqrt{a} - \sqrt{b}}{\sqrt{a} - \sqrt{b}} = \frac{\sqrt{a} - \sqrt{b}}{a - b}$$

**Example:** Rationalize $\frac{1}{3 + \sqrt{2}}$:
$$\frac{1}{3 + \sqrt{2}} \times \frac{3 - \sqrt{2}}{3 - \sqrt{2}} = \frac{3 - \sqrt{2}}{3^2 - (\sqrt{2})^2} = \frac{3 - \sqrt{2}}{9 - 2} = \mathbf{\frac{3 - \sqrt{2}}{7}}$$

---

### 5. Laws of Exponents for Real Numbers

Let $a > 0$ be a real number and $p, q$ be rational numbers:

1. $a^p \cdot a^q = a^{p+q}$
2. $(a^p)^q = a^{pq}$
3. $\frac{a^p}{a^q} = a^{p-q}$
4. $a^p \cdot b^p = (ab)^p$
5. $a^0 = 1 \quad (a \neq 0)$
6. $a^{-p} = \frac{1}{a^p} \implies \left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n$
7. $a^{1/n} = \sqrt[n]{a}$ and $a^{m/n} = (\sqrt[n]{a})^m = \sqrt[n]{a^m}$

**Examples from PA-2 Exam:**
- Simplify $\left(\frac{3}{8}\right)^{-2}$:
  $$\left(\frac{3}{8}\right)^{-2} = \left(\frac{8}{3}\right)^2 = \mathbf{\frac{64}{9}}$$
- Simplify $\left(\frac{1}{3}\right)^{1/5} \div \left(\frac{1}{3}\right)^{1/3}$:
  $$\left(\frac{1}{3}\right)^{\frac{1}{5} - \frac{1}{3}} = \left(\frac{1}{3}\right)^{\frac{3 - 5}{15}} = \left(\frac{1}{3}\right)^{-\frac{2}{15}} = \mathbf{3^{2/15} \text{ or } \left(\frac{1}{3}\right)^{-2/15}}$$
