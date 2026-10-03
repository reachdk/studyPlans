# Chapter 1: Orienting Yourself: The Use of Coordinates

> 👨‍🏫 **Teacher's Masterclass Overview:** Welcome to Coordinate Geometry! Invented by French mathematician René Descartes, this revolutionary branch of mathematics unites algebra and geometry, allowing us to describe geometric figures through algebraic coordinates and visualize equations as geometric curves. Under the new NCERT *Ganita Manjari* and CBSE 2026–27 curriculum, Class 9 Coordinate Geometry extends far beyond plotting points: you will master the Cartesian frame, reflections, the **Baudhāyana–Pythagoras distance formula**, the **midpoint formula**, finding **missing endpoints**, **trisection of segments**, **circle boundary tests**, **triangle reconstruction from side midpoints**, and **collinearity tests**.

---

### 1. The Cartesian Coordinate Plane & Reference Frame

To locate the position of any object or point on a two-dimensional flat plane without ambiguity, we require a fixed reference frame consisting of **two mutually perpendicular real number lines**:

1. **The $x$-axis (Horizontal Reference Axis):**
   - The horizontal number line $X'OX$.
   - Numbers to the right of origin $O$ are positive ($+x$); numbers to the left are negative ($-x$).
   - **Crucial Equation:** On the entire $x$-axis, the vertical position is zero, so the algebraic equation of the $x$-axis is $\mathbf{y = 0}$.
2. **The $y$-axis (Vertical Reference Axis):**
   - The vertical number line $Y'OY$.
   - Numbers upward from origin $O$ are positive ($+y$); numbers downward are negative ($-y$).
   - **Crucial Equation:** On the entire $y$-axis, the horizontal position is zero, so the algebraic equation of the $y$-axis is $\mathbf{x = 0}$.
3. **The Origin $O(0, 0)$:**
   - The fixed reference point where both axes intersect at right angles ($90^\circ$).
   - Coordinates are $\mathbf{(0, 0)}$. Both its abscissa and ordinate are zero.

---

### 2. Anatomy of an Ordered Pair: Abscissa vs Ordinate

Every point $P$ in the plane is represented uniquely by an **ordered pair** of real numbers: $\mathbf{P(x, y)}$.

* **Abscissa ($x$-coordinate):** The signed perpendicular distance of point $P$ from the **$y$-axis**, measured along the $x$-axis.
* **Ordinate ($y$-coordinate):** The signed perpendicular distance of point $P$ from the **$x$-axis**, measured along the $y$-axis.

#### Definitional Distinction Matrix

| Feature | Abscissa ($x$) | Ordinate ($y$) |
| :--- | :--- | :--- |
| **Distance Measured From** | Perpendicular distance from the **$y$-axis** | Perpendicular distance from the **$x$-axis** |
| **Measurement Direction** | Horizontal ($+$ right, $-$ left) | Vertical ($+$ up, $-$ down) |
| **Ordered Pair Position** | First component: $(\mathbf{x}, y)$ | Second component: $(x, \mathbf{y})$ |
| **Value on Coordinate Axes** | Constant $x = 0$ everywhere on the $y$-axis | Constant $y = 0$ everywhere on the $x$-axis |
| **Distance Formula** | Distance to $y$-axis $= |x|$ | Distance to $x$-axis $= |y|$ |

> ⚠️ **The Absolute Distance Trap:** Distance is always a non-negative scalar!
> For point $P(-5, 4)$:
> - Abscissa is $-5$, but the **distance from the $y$-axis is $|-5| = 5$ units**.
> - Ordinate is $4$, and the **distance from the $x$-axis is $|4| = 4$ units**.
> Never write a negative distance in exam answer sheets!

---

### 3. Quadrant Taxonomy & Axis Boundary Conditions

The two coordinate axes divide the infinite Euclidean plane into **four distinct infinite regions called Quadrants**, numbered counter-clockwise starting from the top right:

| Quadrant | Sign of Abscissa ($x$) | Sign of Ordinate ($y$) | Coordinate Structure | Geometric Region | Example Point |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Quadrant I** | Positive ($x > 0$) | Positive ($y > 0$) | $(+, +)$ | Top-Right | $A(4, 5)$ |
| **Quadrant II** | Negative ($x < 0$) | Positive ($y > 0$) | $(-, +)$ | Top-Left | $B(-3, 6)$ |
| **Quadrant III** | Negative ($x < 0$) | Negative ($y < 0$) | $(-, -)$ | Bottom-Left | $C(-5, -2)$ |
| **Quadrant IV** | Positive ($x > 0$) | Negative ($y < 0$) | $(+, -)$ | Bottom-Right | $D(2, -7)$ |

#### Boundary Points Lying on Coordinate Axes

Points lying directly on the axes do **NOT belong to any quadrant**:
* **Positive $x$-axis:** $(x, 0)$ where $x > 0$, e.g. $(3, 0)$.
* **Negative $x$-axis:** $(x, 0)$ where $x < 0$, e.g. $(-4, 0)$.
* **Positive $y$-axis:** $(0, y)$ where $y > 0$, e.g. $(0, 5)$.
* **Negative $y$-axis:** $(0, y)$ where $y < 0$, e.g. $(0, -6)$.
* **Origin:** $(0, 0)$ lies on both axes simultaneously.

> 💡 **Equality of Ordered Pairs:** $(a, b) = (c, d) \iff a = c \text{ and } b = d$.
> Therefore, $(3, 7) \neq (7, 3)$. The only time $(x, y) = (y, x)$ is when $x = y$ (points lying on the line $y = x$).

---

### 4. Perpendicular Projections & Reflections Across Axes & Origin

#### Perpendicular Projections
From any point $P(x_1, y_1)$:
* The foot of the perpendicular on the $x$-axis is $M(x_1, 0)$.
* The foot of the perpendicular on the $y$-axis is $N(0, y_1)$.
* The origin $O(0, 0)$, $M(x_1, 0)$, $P(x_1, y_1)$, and $N(0, y_1)$ form a **rectangle** of dimensions $|x_1|$ and $|y_1|$, with area $= |x_1| \times |y_1|$.

#### Reflections Across Axes (Mirror Points)
Reflections are frequent 1-mark and 2-mark CBSE board exam questions:
1. **Reflection in the $x$-axis:** Negate the $y$-coordinate:
   $$\text{Reflection of } (x, y) \text{ in } x\text{-axis} \implies \mathbf{(x, -y)}$$
   *Example:* Reflection of $(-3, 4)$ across the $x$-axis is $(-3, -4)$.
2. **Reflection in the $y$-axis:** Negate the $x$-coordinate:
   $$\text{Reflection of } (x, y) \text{ in } y\text{-axis} \implies \mathbf{(-x, y)}$$
   *Example:* Reflection of $(-3, 4)$ across the $y$-axis is $(3, 4)$.
3. **Reflection in the Origin:** Negate both coordinates:
   $$\text{Reflection of } (x, y) \text{ in Origin } \implies \mathbf{(-x, -y)}$$
   *Example:* Reflection of $(-3, 4)$ through $(0, 0)$ is $(3, -4)$.

---

### 5. Distance Between Two Points & The Baudhāyana–Pythagoras Theorem

*(NCERT Ganita Manjari Section 1.4)*

To determine the straight-line distance between two points $A(x_1, y_1)$ and $B(x_2, y_2)$ on the coordinate plane:

#### 1. Horizontal and Vertical Shifts
* The horizontal shift between the points is $|x_2 - x_1|$.
* The vertical shift between the points is $|y_2 - y_1|$.
* If two points share the same ordinate ($y_1 = y_2$), the segment is horizontal: $\text{Distance} = |x_2 - x_1|$.
* If two points share the same abscissa ($x_1 = x_2$), the segment is vertical: $\text{Distance} = |y_2 - y_1|$.

#### 2. The General Distance Formula
By constructing a right-angled triangle with vertex $C(x_2, y_1)$, the horizontal base is $|x_2 - x_1|$ and the vertical altitude is $|y_2 - y_1|$. Applying the Baudhāyana–Pythagoras Theorem:

$$d = AB = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

* **Distance from the Origin:** The distance of any point $P(x, y)$ from $O(0, 0)$ simplifies to:
  $$OP = \sqrt{x^2 + y^2}$$
* **Invariance Under Reflection:** Reflecting a triangle across the $x$-axis or $y$-axis preserves the lengths of all sides:
  $$\text{Length}(A'B') = \text{Length}(AB)$$

#### 3. Circles on the Coordinate Plane (NCERT Problem 12)
A circle $K$ with center $C(h, k)$ and radius $r$ is the locus of all points $P(x, y)$ such that:
$$\text{Distance}(C, P) = \sqrt{(x - h)^2 + (y - k)^2} = r$$

To test whether any given point $Q(x_q, y_q)$ lies inside, on, or outside the circle:
* Compute distance $d = \text{Distance}(C, Q)$.
* If $\mathbf{d < r} \implies$ Point lies **strictly inside** the circle.
* If $\mathbf{d = r} \implies$ Point lies **on the boundary** of the circle.
* If $\mathbf{d > r} \implies$ Point lies **strictly outside** the circle.

*Worked Example (from NCERT Problem 12):*
Points $A(1, -8), B(-4, 7), C(-7, -4)$ lie on circle $K$ with center $O(0, 0)$.
* Radius $r = OA = \sqrt{1^2 + (-8)^2} = \sqrt{1 + 64} = \sqrt{65}$ units.
* Verify $OB = \sqrt{(-4)^2 + 7^2} = \sqrt{16 + 49} = \sqrt{65}$, $OC = \sqrt{(-7)^2 + (-4)^2} = \sqrt{49 + 16} = \sqrt{65}$.
* For $D(-5, 6)$: $OD = \sqrt{(-5)^2 + 6^2} = \sqrt{25 + 36} = \sqrt{61}$. Since $\sqrt{61} < \sqrt{65}$, **$D$ lies strictly inside circle $K$**.
* For $E(0, 9)$: $OE = \sqrt{0^2 + 9^2} = 9 = \sqrt{81}$. Since $\sqrt{81} > \sqrt{65}$, **$E$ lies strictly outside circle $K$**.

---

### 6. The Midpoint Formula & Finding Missing Endpoints

*(NCERT Ganita Manjari Problems 9 & 10)*

The midpoint $M$ of a line segment connecting $A(x_1, y_1)$ and $B(x_2, y_2)$ is the point that divides $AB$ into two equal halves ($AM = MB$).

#### 1. The Midpoint Formula
The coordinates of midpoint $M(x_m, y_m)$ are the arithmetic averages of the coordinates of the endpoints:

$$M = \left(\frac{x_1 + x_2}{2}, \quad \frac{y_1 + y_2}{2}\right)$$

#### 2. Protocol: Finding an Unknown Endpoint Given the Midpoint
When you are given endpoint $A(x_1, y_1)$ and midpoint $M(x_m, y_m)$, find the other endpoint $B(x_2, y_2)$ by inverting the formula:

$$x_2 = 2x_m - x_1 \qquad \text{and} \qquad y_2 = 2y_m - y_1$$

*Worked Example (from NCERT Problem 10):*
Given that $M(-7, 1)$ is the midpoint of segment $AB$ with $A(3, -4)$, find the coordinates of $B(x, y)$:
1. Set up the abscissa equation:
   $$\frac{3 + x}{2} = -7 \implies 3 + x = -14 \implies x = -14 - 3 = \mathbf{-17}$$
2. Set up the ordinate equation:
   $$\frac{-4 + y}{2} = 1 \implies -4 + y = 2 \implies y = 2 + 4 = \mathbf{6}$$
3. Therefore, endpoint $B$ is $\mathbf{(-17, 6)}$.
*Check:* $\frac{3 + (-17)}{2} = \frac{-14}{2} = -7$; $\frac{-4 + 6}{2} = \frac{2}{2} = 1$. Correct!

---

### 7. Points of Trisection of a Line Segment

*(NCERT Ganita Manjari Problem 11)*

Points $P$ and $Q$ are called the **points of trisection** of segment $AB$ if they divide $AB$ into three equal parts:
$$AP = PQ = QB$$
Assume $P$ lies closer to $A$, and $Q$ lies closer to $B$.

#### Finding Trisection Points Using the Midpoint Formula
You do not need the advanced section formula! Notice the two key midpoint relationships:
1. $Q$ is the midpoint of segment $PB$.
2. $P$ is the midpoint of segment $AQ$.

#### Standard Step-by-Step Method:
* Let $A = (x_1, y_1)$ and $B = (x_2, y_2)$.
* The total vector displacement from $A$ to $B$ is $\Delta x = x_2 - x_1$ and $\Delta y = y_2 - y_1$.
* Each of the three equal segments has step:
  $$\delta x = \frac{x_2 - x_1}{3}, \qquad \delta y = \frac{y_2 - y_1}{3}$$
* Therefore:
  $$P = \left(x_1 + \frac{x_2 - x_1}{3}, \quad y_1 + \frac{y_2 - y_1}{3}\right) = \left(\frac{2x_1 + x_2}{3}, \quad \frac{2y_1 + y_2}{3}\right)$$
  $$Q = \left(x_1 + 2\frac{x_2 - x_1}{3}, \quad y_1 + 2\frac{y_2 - y_1}{3}\right) = \left(\frac{x_1 + 2x_2}{3}, \quad \frac{y_1 + 2y_2}{3}\right)$$
* **Verification via Midpoint:** $Q$ is strictly the midpoint of segment $PB$:
  $$\text{Midpoint of } PB = \left(\frac{x_P + x_B}{2}, \frac{y_P + y_B}{2}\right) = Q$$

*Worked Example (from NCERT Problem 11):*
Find the trisection points $P$ and $Q$ of segment $AB$ with $A(4, 7)$ and $B(16, -2)$:
1. $\Delta x = 16 - 4 = 12 \implies \delta x = \frac{12}{3} = 4$.
2. $\Delta y = -2 - 7 = -9 \implies \delta y = \frac{-9}{3} = -3$.
3. For point $P$ (1 step from $A$):
   $$x_P = 4 + 4 = \mathbf{8}, \quad y_P = 7 + (-3) = \mathbf{4} \implies \mathbf{P(8, 4)}$$
4. For point $Q$ (2 steps from $A$, or 1 step from $P$):
   $$x_Q = 8 + 4 = \mathbf{12}, \quad y_Q = 4 + (-3) = \mathbf{1} \implies \mathbf{Q(12, 1)}$$
5. *Check using Midpoint:* Is $P(8, 4)$ the midpoint of $AQ$?
   $$\frac{4 + 12}{2} = 8, \quad \frac{7 + 1}{2} = 4. \quad \text{Verified!}$$

---

### 8. Advanced Geometric Synthesis: Triangle Reconstruction & Parallelograms

#### 1. Reconstructing Triangle Vertices from Side Midpoints (NCERT Problem 13)
Let $\Delta ABC$ have unknown vertices $A(x_A, y_A)$, $B(x_B, y_B)$, and $C(x_C, y_C)$.
Suppose the midpoints of sides $AB, BC, CA$ are given as $D(x_1, y_1)$, $E(x_2, y_2)$, and $F(x_3, y_3)$ respectively.

##### The Midpoint System:
$$\frac{x_A + x_B}{2} = x_1 \implies x_A + x_B = 2x_1 \quad \text{--- (1)}$$
$$\frac{x_B + x_C}{2} = x_2 \implies x_B + x_C = 2x_2 \quad \text{--- (2)}$$
$$\frac{x_C + x_A}{2} = x_3 \implies x_C + x_A = 2x_3 \quad \text{--- (3)}$$

Adding (1), (2), and (3):
$$2(x_A + x_B + x_C) = 2(x_1 + x_2 + x_3) \implies x_A + x_B + x_C = x_1 + x_2 + x_3 \quad \text{--- (4)}$$

Now subtract each equation:
* Subtract (2) from (4): $x_A = (x_1 + x_2 + x_3) - 2x_2 \implies \mathbf{x_A = x_1 + x_3 - x_2}$
* Subtract (3) from (4): $x_B = (x_1 + x_2 + x_3) - 2x_3 \implies \mathbf{x_B = x_1 + x_2 - x_3}$
* Subtract (1) from (4): $x_C = (x_1 + x_2 + x_3) - 2x_1 \implies \mathbf{x_C = x_2 + x_3 - x_1}$

*(The exact same symmetric relations hold for all $y$-coordinates!)*

*Worked Example (from NCERT Problem 13):*
Midpoints of sides of $\Delta ABC$ are $D(5, 1)$ on $AB$, $E(6, 5)$ on $BC$, and $F(0, 3)$ on $CA$.
1. Sum of midpoint $x$-coordinates: $5 + 6 + 0 = 11$.
   - $x_A = 11 - 2(6) = 11 - 12 = \mathbf{-1}$
   - $x_B = 11 - 2(0) = 11 - 0 = \mathbf{11}$
   - $x_C = 11 - 2(5) = 11 - 10 = \mathbf{1}$
2. Sum of midpoint $y$-coordinates: $1 + 5 + 3 = 9$.
   - $y_A = 9 - 2(5) = 9 - 10 = \mathbf{-1}$
   - $y_B = 9 - 2(3) = 9 - 6 = \mathbf{3}$
   - $y_C = 9 - 2(1) = 9 - 2 = \mathbf{7}$
3. Hence, the three vertices of the triangle are:
   $$\mathbf{A(-1, -1), \quad B(11, 3), \quad C(1, 7)}$$

#### 2. The Parallelogram Diagonal Midpoint Property (CBSE Syllabus CG-9)
In any parallelogram $ABCD$, the diagonals $AC$ and $BD$ bisect each other at their **common midpoint**:
$$\text{Midpoint of } AC = \text{Midpoint of } BD$$
$$\left(\frac{x_A + x_C}{2}, \frac{y_A + y_C}{2}\right) = \left(\frac{x_B + x_D}{2}, \frac{y_B + y_D}{2}\right)$$

Therefore, given any three vertices $A, B, C$, the fourth vertex $D(x_D, y_D)$ is:
$$\mathbf{x_D = x_A + x_C - x_B} \qquad \text{and} \qquad \mathbf{y_D = y_A + y_C - y_B}$$

---

### 9. Collinearity Verification: Distance vs Slope Methods

*(NCERT Ganita Manjari Problems 6 & 7)*

Three points $A, B, C$ are called **collinear** if they all lie on the same straight line. In CBSE exams, you may be asked to test collinearity without plotting:

#### Method 1: The Distance Sum Criterion (Baudhāyana–Pythagoras)
Points $A, B, C$ are collinear if and only if the sum of the lengths of the two smaller segments equals the length of the largest segment:
$$AB + BC = AC \quad (\text{if } B \text{ lies between } A \text{ and } C)$$
*(If $AB + BC > AC$, the three points form a triangle and are non-collinear).*

#### Method 2: The Slope / Rise-over-Run Criterion
The steepness (rate of vertical rise per horizontal shift) between points must be identical:
$$\text{Slope}(AB) = \frac{y_2 - y_1}{x_2 - x_1} = \frac{y_3 - y_2}{x_3 - x_2} = \text{Slope}(BC)$$
Since point $B$ is common to both segments, they must lie on the same continuous line.

*Worked Example (from NCERT Problem 6):*
Are the points $M(-3, -4), A(0, 0), G(6, 8)$ on the same straight line?
* Using Slope:
  - $\text{Slope}(MA) = \frac{0 - (-4)}{0 - (-3)} = \frac{4}{3}$
  - $\text{Slope}(AG) = \frac{8 - 0}{6 - 0} = \frac{8}{6} = \frac{4}{3}$
  - Since $\text{Slope}(MA) = \text{Slope}(AG)$ and $A$ is common, **$M, A, G$ are collinear!**

---

### 10. Examiner's Pitfall Matrix & Graded Solved Examples

| Common Exam Error | What the Student Wrote | Why it Loses Marks | Correct CBSE Method |
| :--- | :--- | :--- | :--- |
| **Trap 1: Axis vs Coordinate** | "Distance of $(-4, 7)$ from $y$-axis is $7$." | Confusing $x$ and $y$. Distance to $y$-axis is the horizontal distance (abscissa). | Distance is $|-4| = \mathbf{4\text{ units}}$. |
| **Trap 2: Negative Distance** | "Distance from $x$-axis is $-5$." | Distance is physical length and can never be negative. | Take absolute value: $|-5| = \mathbf{5\text{ units}}$. |
| **Trap 3: Points on Axes** | "Point $(0, -3)$ lies in Quadrant IV." | Points with $x=0$ or $y=0$ do not belong to any quadrant. | Point lies on the **negative $y$-axis**. |
| **Trap 4: Midpoint Subtraction** | Used $\frac{x_2 - x_1}{2}$ for midpoint. | Subtraction gives half-distance, not the coordinate position! | Midpoint is the average: $\mathbf{\frac{x_1 + x_2}{2}}$. |
| **Trap 5: Missing Endpoint Sign** | Forgot to multiply midpoint by 2. | $x_2 = 2x_m - x_1$, not $x_m - x_1$. | Multiply midpoint coordinate by 2 before subtracting endpoint. |

#### Tiered Solved Example (HOTS / 4 Marks):
Show that the points $P(2, 1), Q(-1, 2), R(-2, -1),$ and $S(1, -2)$ form a square $PQRS$, and calculate its area and the coordinates of the intersection of its diagonals.
* **Solution:**
  1. **Calculate side lengths using Distance Formula:**
     - $PQ = \sqrt{(-1 - 2)^2 + (2 - 1)^2} = \sqrt{(-3)^2 + 1^2} = \sqrt{9 + 1} = \sqrt{10}$ units.
     - $QR = \sqrt{(-2 - (-1))^2 + (-1 - 2)^2} = \sqrt{(-1)^2 + (-3)^2} = \sqrt{1 + 9} = \sqrt{10}$ units.
     - $RS = \sqrt{(1 - (-2))^2 + (-2 - (-1))^2} = \sqrt{3^2 + (-1)^2} = \sqrt{9 + 1} = \sqrt{10}$ units.
     - $SP = \sqrt{(2 - 1)^2 + (1 - (-2))^2} = \sqrt{1^2 + 3^2} = \sqrt{1 + 9} = \sqrt{10}$ units.
     - All four sides are equal ($PQ = QR = RS = SP = \sqrt{10}$). [1.5 marks]
  2. **Calculate diagonal lengths:**
     - Diagonal $PR = \sqrt{(-2 - 2)^2 + (-1 - 1)^2} = \sqrt{(-4)^2 + (-2)^2} = \sqrt{16 + 4} = \sqrt{20}$ units.
     - Diagonal $QS = \sqrt{(1 - (-1))^2 + (-2 - 2)^2} = \sqrt{2^2 + (-4)^2} = \sqrt{4 + 16} = \sqrt{20}$ units.
     - Since all 4 sides are equal AND both diagonals are equal ($PR = QS = \sqrt{20}$), **$PQRS$ is a Square**. [1.5 marks]
  3. **Area of Square:** $\text{Area} = \text{side}^2 = (\sqrt{10})^2 = \mathbf{10\text{ sq units}}$. [0.5 mark]
  4. **Diagonal Intersection (Midpoint of $PR$):**
     $$M = \left(\frac{2 + (-2)}{2}, \frac{1 + (-1)}{2}\right) = \left(\frac{0}{2}, \frac{0}{2}\right) = \mathbf{(0, 0)}$$
     The diagonals intersect exactly at the **Origin $O(0, 0)$**. [0.5 mark]

---

<div class="interactive-widget">
  <div class="widget-title">⚡ Interactive Dual-Point Coordinate, Distance & Midpoint Calculator</div>
  <p style="font-size:0.88rem; color:var(--text-muted); margin-bottom:12px;">Enter coordinates for points $A(x_1, y_1)$ and $B(x_2, y_2)$ to calculate distance, midpoint, quadrant analysis, and collinearity:</p>
  <div class="widget-inputs" style="display:flex; flex-wrap:wrap; gap:10px; align-items:center;">
    <label>Point A: $x_1$ <input type="number" id="pt_x1" value="-3" step="1" style="width:65px; padding:6px 8px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="calcDualPoints()"></label>
    <label>$y_1$ <input type="number" id="pt_y1" value="4" step="1" style="width:65px; padding:6px 8px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="calcDualPoints()"></label>
    <span style="font-weight:700; color:var(--primary); margin:0 4px;">|</span>
    <label>Point B: $x_2$ <input type="number" id="pt_x2" value="5" step="1" style="width:65px; padding:6px 8px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="calcDualPoints()"></label>
    <label>$y_2$ <input type="number" id="pt_y2" value="-2" step="1" style="width:65px; padding:6px 8px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="calcDualPoints()"></label>
    <button class="btn-notes-toggle" onclick="calcDualPoints()" style="padding:6px 14px; font-weight:700;">Calculate</button>
  </div>
  <div id="dual-coord-output" style="background:var(--card-bg); padding:14px 18px; border-radius:8px; border:1px solid var(--border); font-size:0.92rem; line-height:1.6; margin-top:10px;">
    <div style="font-weight:700; color:var(--primary); margin-bottom:6px;">Calculated Properties: Segment AB</div>
    <div>• <strong>Point A:</strong> $(-3, 4)$ [Quadrant II] &nbsp;|&nbsp; <strong>Point B:</strong> $(5, -2)$ [Quadrant IV]</div>
    <div>• <strong>Midpoint M:</strong> $\left(\frac{-3 + 5}{2}, \frac{4 + (-2)}{2}\right) = \mathbf{(1, 1)}$ [Quadrant I]</div>
    <div>• <strong>Horizontal Shift $|x_2 - x_1|$:</strong> $|5 - (-3)| = 8$ units</div>
    <div>• <strong>Vertical Shift $|y_2 - y_1|$:</strong> $|-2 - 4| = 6$ units</div>
    <div>• <strong>Straight-Line Distance $AB$:</strong> $\sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = \mathbf{10\text{ units}}$</div>
  </div>
</div>
