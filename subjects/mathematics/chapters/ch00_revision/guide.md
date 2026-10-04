# Master Revision Sheet: Formulas, Identities & Theorems
> **NCERT Ganita Manjari • CBSE Class 9 Mathematics**  
> *A high-density, formula-centric reference collating all essential identities, analytical formulas, and geometric theorems across Chapters 1, 2, 3, 4, and 6.*

---

### 1. Number Systems & Exponent Laws (Chapter 3)

#### Real Numbers Hierarchy
$$\mathbb{N} \subset \mathbb{W} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$
* **Natural Numbers ($\mathbb{N}$):** $\{1, 2, 3, \dots\}$
* **Whole Numbers ($\mathbb{W}$):** $\{0, 1, 2, 3, \dots\}$
* **Integers ($\mathbb{Z}$):** $\{\dots, -2, -1, 0, 1, 2, \dots\}$
* **Rational Numbers ($\mathbb{Q}$):** Numbers expressible as $\frac{p}{q}$, where $p, q \in \mathbb{Z}$ and $q \neq 0$.
* **Irrational Numbers ($\mathbb{I}$):** Real numbers that *cannot* be expressed as $\frac{p}{q}$ (e.g., $\sqrt{2}, \sqrt{3}, \pi$).

---

#### Decimal Expansion & Rationality Criteria

| Decimal Type | Form / Example | Classification | Rationality Rule |
| :--- | :--- | :--- | :--- |
| **Terminating** | $0.375 = \frac{3}{8}$ | **Rational** ($\mathbb{Q}$) | Denominator in lowest terms has prime factors **only of the form $2^m \times 5^n$**. |
| **Non-Terminating Recurring** | $0.\bar{3} = \frac{1}{3}, 0.2\overline{35} = \frac{233}{990}$ | **Rational** ($\mathbb{Q}$) | Denominator in lowest terms contains prime factors **other than 2 or 5**. |
| **Non-Terminating Non-Recurring** | $1.41421356\dots, 0.1010010001\dots$ | **Irrational** ($\mathbb{I}$) | Cannot be expressed as $\frac{p}{q}$. Square root of any prime $p$ ($\sqrt{p}$) is always irrational. |

##### Fast Conversion: Recurring Decimal $\to \frac{p}{q}$
* **Pure Recurring:** $0.\overline{a} = \frac{a}{9}$, $\quad 0.\overline{ab} = \frac{ab}{99}$, $\quad 0.\overline{abc} = \frac{abc}{999}$.
* **Mixed Recurring:** 
  $$0.a\bar{b} = \frac{ab - a}{90}, \quad 0.ab\bar{c} = \frac{abc - ab}{900}, \quad 0.a\overline{bc} = \frac{abc - a}{990}$$
  *(Numerator: Full digits minus non-repeating digits. Denominator: As many 9s as repeating digits, followed by as many 0s as non-repeating digits).*

---

#### Laws of Exponents & Radicals Master Table
*Let $a, b > 0$ and $m, n, p, q$ be rational numbers:*

| Law | Formula | Exam Notes / Edge Cases |
| :--- | :--- | :--- |
| **Product of Powers** | $a^m \cdot a^n = a^{m+n}$ | Add exponents when bases are identical. |
| **Quotient of Powers** | $\frac{a^m}{a^n} = a^{m-n}$ | Subtract denominator exponent from numerator. |
| **Power of a Power** | $(a^m)^n = a^{mn}$ | Multiply exponents: $((a^m)^n)^p = a^{mnp}$. |
| **Power of a Product** | $(ab)^n = a^n \cdot b^n$ | Distribute power across factors. |
| **Power of a Quotient** | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ | $b \neq 0$. |
| **Zero Exponent** | $a^0 = 1$ | Valid for any $a \neq 0$. Note: $0^0$ is indeterminate. |
| **Negative Exponent** | $a^{-n} = \frac{1}{a^n} \iff \frac{1}{a^{-n}} = a^n$ | Reciprocal inverts the sign of the power. |
| **Fractional Exponents** | $a^{p/q} = \sqrt[q]{a^p} = (\sqrt[q]{a})^p$ | In evaluations, compute the root first: $(64)^{2/3} = (4)^2 = 16$. |

---

#### Rationalization & Conjugate Pairs
* **Single Radical:** $\frac{1}{\sqrt{a}} \times \frac{\sqrt{a}}{\sqrt{a}} = \frac{\sqrt{a}}{a}$.
* **Binomial Radical:** Conjugate of $(\sqrt{a} + \sqrt{b})$ is $(\sqrt{a} - \sqrt{b})$:
  $$\frac{1}{\sqrt{a} \pm \sqrt{b}} \times \frac{\sqrt{a} \mp \sqrt{b}}{\sqrt{a} \mp \sqrt{b}} = \frac{\sqrt{a} \mp \sqrt{b}}{a - b}$$
* **Mixed Surd:** Conjugate of $(a + b\sqrt{c})$ is $(a - b\sqrt{c})$:
  $$\frac{1}{a + b\sqrt{c}} = \frac{a - b\sqrt{c}}{a^2 - b^2 c}$$

> [!TIP]
> **Brahmagupta's Laws of Sign Arithmetic & Real Density:**
> * Negative $\times$ Negative = Positive; Positive $\times$ Negative = Negative.
> * Division by zero is undefined ($\frac{a}{0}$ has no mathematical meaning).
> * **Density Property:** Between any two distinct real numbers $a < b$, there exist **infinitely many rational** and **infinitely many irrational** numbers. Arithmetic mean $\frac{a+b}{2}$ always gives a rational between two rationals.

---

### 2. Linear Polynomials & Growth/Decay (Chapter 2)

#### Polynomial Foundations
* **Definition:** An algebraic expression $p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ where exponents $n$ are **non-negative integers** ($n \in \{0, 1, 2, \dots\}$).
* **Degree:** The highest non-negative power of $x$ with a non-zero coefficient ($a_n \neq 0$).

| Polynomial Type | Standard Form | Degree | Number of Zeroes |
| :--- | :--- | :---: | :---: |
| **Zero Polynomial** | $p(x) = 0$ | **Not defined** | Infinitely many (all real numbers) |
| **Non-Zero Constant** | $p(x) = c \quad (c \neq 0)$ | **$0$** ($c = cx^0$) | No zeroes |
| **Linear Polynomial** | $p(x) = ax + b \quad (a \neq 0)$ | **$1$** | Exactly 1 zero ($x = -b/a$) |
| **Quadratic Polynomial** | $p(x) = ax^2 + bx + c \quad (a \neq 0)$ | **$2$** | At most 2 real zeroes |
| **Cubic Polynomial** | $p(x) = ax^3 + bx^2 + cx + d \quad (a \neq 0)$ | **$3$** | At most 3 real zeroes |

---

#### Linear Equations in Two Variables ($ax + by + c = 0$)
Every linear equation in two variables represents a **straight line** on the Cartesian plane with **infinitely many solutions**.

##### Key Line Forms & Formulas
* **General Form:** $Ax + By + C = 0 \implies \text{Slope } m = -\frac{A}{B}, \quad x\text{-intercept} = -\frac{C}{A}, \quad y\text{-intercept} = -\frac{C}{B}$.
* **Slope-Intercept Form:** $y = mx + c$, where $m$ is the slope and $c$ is the $y$-intercept.
* **Intercept Form:** $\frac{x}{a} + \frac{y}{b} = 1$, where $a$ is the $x$-intercept $(a, 0)$ and $b$ is the $y$-intercept $(0, b)$.
* **Horizontal Line:** $y = k$ (Slope $m = 0$, parallel to $x$-axis).
* **Vertical Line:** $x = k$ (Slope $m$ is **undefined**, parallel to $y$-axis).

---

#### Constant Rate of Change (Slope $m$)
$$\text{Slope } m = \frac{\text{Rise}}{\text{Run}} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$
* **Linear Growth ($m > 0$):** Line rises from left to right ($\Delta y > 0$). Physical models: Savings accumulation $S(n) = 150n + 500$, constant velocity $s = vt$.
* **Linear Decay ($m < 0$):** Line falls from left to right ($\Delta y < 0$). Physical models: Battery drain $B(t) = 100 - 18t$, altitude descent.
* **Parallel Lines:** $m_1 = m_2$.
* **Perpendicular Lines:** $m_1 \cdot m_2 = -1 \iff m_2 = -\frac{1}{m_1}$.

---

### 3. Algebraic Identities & Factoring Master Table (Chapter 4)

#### The 13 Core Identities

| ID # | Algebraic Identity | Primary Use / Application |
| :---: | :--- | :--- |
| **1** | $(x + a)(x + b) = x^2 + (a + b)x + ab$ | Binomial multiplication, factoring quadratics. |
| **2** | $(a + b)^2 = a^2 + 2ab + b^2$ | Square of binomial sum. |
| **3** | $(a - b)^2 = a^2 - 2ab + b^2$ | Square of binomial difference. |
| **4** | $a^2 - b^2 = (a - b)(a + b)$ | Difference of two squares (factoring). |
| **5** | $(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)$ | Trinomial square expansion. |
| **6** | $a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca)$ | Finding sum of squares from linear & pairwise sums. |
| **7** | $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 = a^3 + b^3 + 3ab(a + b)$ | Cube of a sum. |
| **8** | $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3 = a^3 - b^3 - 3ab(a - b)$ | Cube of a difference. |
| **9** | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ | Sum of two cubes (factoring). |
| **10** | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ | Difference of two cubes (factoring). |
| **11** | $a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)$ | Three-variable cubic master identity. |
| **12** | $a^3 + b^3 + c^3 - 3abc = \frac{1}{2}(a + b + c)\left[(a - b)^2 + (b - c)^2 + (c - a)^2\right]$ | Alternative SOS (sum of squares) form. |
| **13** | **Conditional Zero Rule:** If $a + b + c = 0$, then $\mathbf{a^3 + b^3 + c^3 = 3abc}$ | Rapid evaluation of cubic sums without direct cubing. |

---

#### High-Yield Reciprocal Identities (Exam Classics)
When given $x + \frac{1}{x} = k$ or $x - \frac{1}{x} = k$:
* **Square Sum:**
  $$x^2 + \frac{1}{x^2} = \left(x + \frac{1}{x}\right)^2 - 2 = k^2 - 2$$
  $$x^2 + \frac{1}{x^2} = \left(x - \frac{1}{x}\right)^2 + 2 = k^2 + 2$$
* **Cube Sum / Difference:**
  $$x^3 + \frac{1}{x^3} = \left(x + \frac{1}{x}\right)^3 - 3\left(x + \frac{1}{x}\right) = k^3 - 3k$$
  $$x^3 - \frac{1}{x^3} = \left(x - \frac{1}{x}\right)^3 + 3\left(x - \frac{1}{x}\right) = k^3 + 3k$$
* **Fourth Power:**
  $$x^4 + \frac{1}{x^4} = \left(x^2 + \frac{1}{x^2}\right)^2 - 2$$

---

#### Remainder & Factor Theorems
* **Remainder Theorem:** If a polynomial $p(x)$ is divided by $(x - a)$, the remainder is $R = p(a)$. If divided by $(ax + b)$, remainder is $R = p(-b/a)$.
* **Factor Theorem:** A linear polynomial $(x - a)$ is a factor of $p(x)$ **if and only if** $p(a) = 0$.

#### Algebra Tiles Area Representation
* $x^2$ tile: Large square of side $x$.
* $x$ tile: Rectangle of dimensions $x \times 1$.
* $1$ tile: Small unit square of side $1$.
* **Geometric Factoring:** Arranging $x^2 + (p+q)x + pq$ tiles into a large rectangle of length $(x + p)$ and breadth $(x + q)$ confirms the factors algebraically and visually.

---

### 4. Coordinate Geometry & Analytical Tools (Chapter 1)

#### Cartesian Grid & Sign Conventions

| Quadrant / Axis | Abscissa ($x$) | Ordinate ($y$) | Coordinate Form | Location on Plane |
| :---: | :---: | :---: | :---: | :--- |
| **Quadrant I** | $x > 0$ ($+$) | $y > 0$ ($+$) | $(+, +)$ | Top-Right |
| **Quadrant II** | $x < 0$ ($-$) | $y > 0$ ($+$) | $(-, +)$ | Top-Left |
| **Quadrant III** | $x < 0$ ($-$) | $y < 0$ ($-$) | $(-, -)$ | Bottom-Left |
| **Quadrant IV** | $x > 0$ ($+$) | $y < 0$ ($-$) | $(+, -)$ | Bottom-Right |
| **$x$-axis** | Any real $x$ | $y = 0$ | $(x, 0)$ | Horizontal dividing line |
| **$y$-axis** | $x = 0$ | Any real $y$ | $(0, y)$ | Vertical dividing line |
| **Origin ($O$)** | $x = 0$ | $y = 0$ | $(0, 0)$ | Intersection of coordinate axes |

---

#### Essential Coordinate Formulas

##### 1. Perpendicular Distance to Axes
* Distance of point $P(x, y)$ from the **$x$-axis** $= |y|$ (absolute ordinate).
* Distance of point $P(x, y)$ from the **$y$-axis** $= |x|$ (absolute abscissa).

##### 2. Reflections Across Axes
* **Reflection in $x$-axis:** $(x, y) \to (x, -y)$ (negate ordinate).
* **Reflection in $y$-axis:** $(x, y) \to (-x, y)$ (negate abscissa).
* **Reflection in Origin:** $(x, y) \to (-x, -y)$ (negate both).

##### 3. Baudhāyana–Pythagoras Distance Formula
$$d(P, Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
* **Distance from Origin $O(0, 0)$:** $OP = \sqrt{x^2 + y^2}$.

##### 4. Midpoint Formula & Missing Endpoints
$$M(x_M, y_M) = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$
* **Finding Missing Endpoint $B(x_B, y_B)$ given $A$ and $M$:**
  $$x_B = 2x_M - x_A, \quad y_B = 2y_M - y_A$$

##### 5. Points of Trisection ($P, Q$ dividing $AB$ into 3 equal parts)
$$\delta x = \frac{x_B - x_A}{3}, \quad \delta y = \frac{y_B - y_A}{3}$$
$$P(x_A + \delta x, y_A + \delta y), \quad Q(x_A + 2\delta x, y_A + 2\delta y)$$

##### 6. Triangle Reconstruction from Side Midpoints
*Let $D, E, F$ be the midpoints of sides $BC, CA, AB$ respectively:*
$$x_A = x_E + x_F - x_D, \quad y_A = y_E + y_F - y_D$$
$$x_B = x_D + x_F - x_E, \quad y_B = y_D + y_F - y_E$$
$$x_C = x_D + x_E - x_F, \quad y_C = y_D + y_E - y_F$$
*(Rule: Add the coordinates of the two adjacent midpoints and subtract the opposite midpoint).*

##### 7. Circle Locus Boundary Test
*Center $C(h, k)$, radius $r$. For any point $P(x, y)$, calculate $d^2 = (x - h)^2 + (y - k)^2$:*
* $d < r \implies P$ lies **strictly inside** the circle.
* $d = r \implies P$ lies **exactly on the boundary** of the circle.
* $d > r \implies P$ lies **strictly outside** the circle.

##### 8. Collinearity Criteria
Three points $A, B, C$ are collinear if and only if:
1. **Distance Method:** $AB + BC = AC$ (longest segment equals sum of shorter segments).
2. **Equal Slope Method:** $\frac{y_B - y_A}{x_B - x_A} = \frac{y_C - y_B}{x_C - x_B}$.

##### 9. Area of Triangle Formed by a Line with Axes
For $Ax + By + C = 0$:
$$\text{Area} = \frac{1}{2} \times |x\text{-intercept}| \times |y\text{-intercept}| = \frac{1}{2} \left|\frac{-C}{A}\right| \left|\frac{-C}{B}\right| = \frac{C^2}{2|AB|}$$

---

### 5. Perimeter & Area: Mensuration Formulas (Chapter 6)

#### Heron's Master Formula for Triangles
For any triangle with side lengths $a, b, c$:
$$\text{Semi-Perimeter: } s = \frac{a + b + c}{2}$$
$$\mathbf{\text{Area} = \sqrt{s(s - a)(s - b)(s - c)}}$$
* **Existence Condition:** $s > a, s > b, s > c$ (equivalent to triangle inequalities $a + b > c, b + c > a, c + a > b$).

---

#### Special Triangle Reference Card

| Triangle | Knowns | Area Formula | Altitude Formula |
| :--- | :--- | :--- | :--- |
| **Equilateral** | Side $a$ | $\text{Area} = \frac{\sqrt{3}}{4}a^2$ | $h = \frac{\sqrt{3}}{2}a$ |
| **Isosceles** | Equal legs $a$, base $b$ | $\text{Area} = \frac{b}{4}\sqrt{4a^2 - b^2}$ | $h = \sqrt{a^2 - \left(\frac{b}{2}\right)^2}$ |
| **Right-Angled** | Base $b$, perpendicular $p$ | $\text{Area} = \frac{1}{2} \times b \times p$ | Hypotenuse $c = \sqrt{b^2 + p^2}$ |
| **Any Triangle** | Base $b$, altitude $h$ | $\text{Area} = \frac{1}{2} \times b \times h$ | Altitude to side $a$: $h_a = \frac{2 \times \text{Area}}{a}$ |

---

#### Quadrilateral Area Decomposition Techniques
1. **Rhombus (Diagonals $d_1, d_2$):** $\text{Area} = \frac{1}{2} \times d_1 \times d_2$. Each side $a = \sqrt{(d_1/2)^2 + (d_2/2)^2}$.
2. **Trapezium (Parallel sides $a$ and $b$, height $h$):**
   $$\text{Area} = \frac{1}{2}(a + b)h$$
   *Decomposition method when height is not given:* Draw a line from one upper vertex parallel to the opposite oblique leg to create a **parallelogram** and a **triangle**. Use Heron's formula on the triangle to find height $h = \frac{2 \times \text{Area}}{\text{base}}$, then find trapezium area.
3. **General Quadrilateral via Diagonal:** Split into two triangles $\Delta_1$ and $\Delta_2$ along diagonal $d$. $\text{Area} = \text{Area}(\Delta_1) + \text{Area}(\Delta_2)$.

---

#### Brahmagupta's Master Formula (Cyclic Quadrilaterals)
For a quadrilateral whose four vertices lie on a circle (cyclic quadrilateral) with side lengths $a, b, c, d$:
$$\text{Semi-Perimeter: } s = \frac{a + b + c + d}{2}$$
$$\mathbf{\text{Area} = \sqrt{(s - a)(s - b)(s - c)(s - d)}}$$
> [!NOTE]
> **Reduction to Heron's Formula:**  
> When one side shrinks to a point ($d \to 0$), the cyclic quadrilateral degenerates into a triangle with sides $a, b, c$.  
> Since $(s - 0) = s$, Brahmagupta's formula reduces directly to:
> $$\text{Area} = \sqrt{s(s - a)(s - b)(s - c)} \quad \text{(Heron's Formula)}$$

---

#### Circle, Arc & Sector Formulas

| Circle Element | Formula | Notes |
| :--- | :--- | :--- |
| **Circumference** | $C = 2\pi r = \pi d$ | Ratio $\frac{C}{d} = \pi \approx \frac{22}{7} \approx 3.14159$ |
| **Circle Area** | $A = \pi r^2$ | Area of circular boundary |
| **Arc Length of Sector** | $L = \frac{\theta}{360^\circ} \times 2\pi r$ | Subtended central angle $\theta$ in degrees |
| **Sector Area** | $A_{\text{sector}} = \frac{\theta}{360^\circ} \times \pi r^2 = \frac{1}{2} L r$ | Equivalent to $(1/2) \times \text{Arc Length} \times \text{Radius}$ |
| **Sector Perimeter** | $P_{\text{sector}} = L + 2r$ | Arc length plus two radial boundary edges |
| **Minor Segment Area** | $A_{\text{segment}} = A_{\text{sector}} - \text{Area of } \Delta OAB$ | For $\theta = 90^\circ$: Sector $- \frac{1}{2}r^2$<br>For $\theta = 60^\circ$: Sector $- \frac{\sqrt{3}}{4}r^2$ |

---

#### Area Scaling Principle
If all linear dimensions (sides) of a 2D geometric figure are multiplied by a scale factor $k$:
$$\text{Perimeter Scales by } k \implies P' = k \cdot P$$
$$\mathbf{\text{Area Scales by } k^2 \implies A' = k^2 \cdot A}$$
* Example: If sides are doubled ($k = 2$), Area quadruples ($A' = 4A$), which is a **$300\%$ increase**.
* Example: If sides are tripled ($k = 3$), Area becomes $9A$, which is an **$800\%$ increase**.

---

### 6. 💡 Top 10 High-Stakes Exam Traps Checklist

1. **Negative Exponent Trap:** $a^{-n} = \frac{1}{a^n}$; it does *not* make the number negative (e.g., $2^{-3} = \frac{1}{8}$, NOT $-8$).
2. **Perpendicular Distance from Axes:** Distance from $x$-axis is $|y|$; distance from $y$-axis is $|x|$.
3. **Degree of Constant vs Zero Polynomial:** Degree of constant $c \neq 0$ is $0$; degree of zero polynomial $0$ is **undefined**.
4. **Fractional Exponents:** Simplify root before power: $81^{3/4} = (\sqrt[4]{81})^3 = 3^3 = 27$.
5. **Cubic Reciprocal Adjustments:** $(x + 1/x)^3 = x^3 + 1/x^3 + 3(x + 1/x)$. Do not forget the $+ 3(x + 1/x)$ cross term!
6. **Signs in Cubic Differences:** $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$. Notice $+3ab^2$ is positive!
7. **Triangle Semi-Perimeter:** Remember to divide perimeter by **2**, not by 3 ($s = \frac{a+b+c}{2}$).
8. **Trapezium Height Mistake:** The slant non-parallel sides are *not* the height. Decompose into parallelogram + triangle to find vertical height $h$.
9. **Sector Perimeter Edge Trap:** Perimeter of a sector is $L + 2r$, not just arc length $L$.
10. **Perpendicular Slope Rule:** $m_1 \cdot m_2 = -1 \implies m_2 = -\frac{1}{m_1}$. Remember both **negative** and **reciprocal**!
