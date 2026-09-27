# Chapter 6: Measuring Space: Perimeter and Area

> 👨‍🏫 **Teacher's Overview:** When the height (altitude) of a triangle is unknown, the elementary formula $\text{Area} = \frac{1}{2} \times \text{base} \times \text{height}$ cannot be applied directly. Greek mathematician Hero of Alexandria derived a remarkable formula that gives the exact area of **any triangle** knowing strictly its three side lengths. In Class 9 CBSE, Heron's formula is tested through real-world applications: park fencing, flyover billboards, and dividing quadrilaterals along diagonals.

---

### 1. Perimeter and Semi-Perimeter

For a triangle with side lengths $a$, $b$, and $c$:
- **Perimeter ($2s$):** Total boundary length:
  $$\text{Perimeter} = a + b + c$$
- **Semi-Perimeter ($s$):** Half of the perimeter:
  $$\mathbf{s = \frac{a + b + c}{2}}$$

---

### 2. Heron's Formula for Area of a Triangle

$$\mathbf{\text{Area} = \sqrt{s(s - a)(s - b)(s - c)}}$$

where:
- $a, b, c$ are the lengths of the three sides.
- $s = \frac{a+b+c}{2}$ is the semi-perimeter.
- $(s - a), (s - b), (s - c)$ must each be strictly positive (since the sum of any two sides of a triangle is always greater than the third side: $a + b > c \implies s > c$).

---

### 3. Special Case: Equilateral Triangle

For an equilateral triangle where all sides are equal ($a = b = c$):
1. $s = \frac{a + a + a}{2} = \frac{3a}{2}$
2. $s - a = \frac{3a}{2} - a = \frac{a}{2}$
3. $\text{Area} = \sqrt{\frac{3a}{2} \cdot \frac{a}{2} \cdot \frac{a}{2} \cdot \frac{a}{2}} = \sqrt{\frac{3a^4}{16}} = \mathbf{\frac{\sqrt{3}}{4} a^2}$

| Triangle Type | Given Parameters | Best Formula |
| :--- | :--- | :--- |
| **Right-Angled Triangle** | Base $b$ and Altitude $h$ | $\text{Area} = \frac{1}{2} \times b \times h$ |
| **Equilateral Triangle** | Side $a$ | $\text{Area} = \frac{\sqrt{3}}{4} a^2$ |
| **Scalene / General Triangle** | Three sides $a, b, c$ | $\mathbf{\text{Area} = \sqrt{s(s - a)(s - b)(s - c)}}$ |
| **Quadrilateral** | 4 sides + 1 diagonal | Split into 2 triangles; sum their areas |

---

### 4. Prime Factorization Technique under the Radical

> 💡 **Calculation Secret:** Never multiply out huge numbers inside $\sqrt{\dots}$! It invites arithmetic errors. Instead, **break each factor into prime factors** and pull out pairs:

**Example (From School PA-2 Q27): Flyover Triangular Wall**
Sides are $a = 13\text{ m}, b = 14\text{ m}, c = 15\text{ m}$:
1. $s = \frac{13 + 14 + 15}{2} = \frac{42}{2} = 21\text{ m}$
2. $s - a = 21 - 13 = 8\text{ m}$
3. $s - b = 21 - 14 = 7\text{ m}$
4. $s - c = 21 - 15 = 6\text{ m}$
5. $\text{Area} = \sqrt{21 \times 8 \times 7 \times 6}$
   - Factorize: $21 = 7 \times 3$
   - Factorize: $8 = 2 \times 2 \times 2$
   - Factorize: $7 = 7$
   - Factorize: $6 = 2 \times 3$
6. Group pairs:
   $$\text{Area} = \sqrt{(7 \times 7) \times (3 \times 3) \times (2 \times 2 \times 2 \times 2)} = \sqrt{7^2 \times 3^2 \times 2^4}$$
   $$\text{Area} = 7 \times 3 \times 2^2 = 7 \times 3 \times 4 = \mathbf{84\text{ m}^2}$$

---

### 5. Application to Quadrilaterals (Cleanliness Campaign Problem - PA-2 Q34)

A park or field $PQRS$ has $\angle Q = 90^\circ$, $PQ = 7\text{ m}$, $QR = 24\text{ m}$, $RS = 18\text{ m}$, $SP = 13\text{ m}$ (or similar):
1. **Right-Angled Part $\Delta PQR$:**
   - By Pythagoras theorem: $PR = \sqrt{PQ^2 + QR^2} = \sqrt{7^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25\text{ m}$.
   - $\text{Area}(\Delta PQR) = \frac{1}{2} \times 7 \times 24 = 84\text{ m}^2$.
2. **General Triangle Part $\Delta PRS$:**
   - Sides are $PR = 25\text{ m}, RS, SP$. Use Heron's formula!
3. **Total Area:**
   $$\text{Total Area} = \text{Area}(\Delta PQR) + \text{Area}(\Delta PRS)$$
