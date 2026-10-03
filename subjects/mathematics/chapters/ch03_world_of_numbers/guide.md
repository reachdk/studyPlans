# Chapter 3: The World of Numbers

> 👨‍🏫 **Teacher's Masterclass Overview:** Numbers form the grammar of mathematics! In earlier classes, we worked with natural numbers $\mathbb{N}$, whole numbers $\mathbb{W}$, and integers $\mathbb{Z}$. In Class 9 CBSE, we expand our mathematical universe to the complete continuum of **Real Numbers ($\mathbb{R}$)** by uniting the rational numbers ($\mathbb{Q}$) with the boundless world of irrational numbers ($\mathbb{Q}'$ or $\mathbb{I}$). In this chapter, we master decimal classification, recurring-to-fraction conversions, square root spiral constructions, rationalizing the denominator, and the generalized laws of exponents.

---

### 1. The Real Number System Hierarchy & Decimal Taxonomy

The set of **Real Numbers ($\mathbb{R}$)** represents every single point on the continuous number line. Every real number is either **rational** or **irrational**, with zero overlap ($\mathbb{Q} \cap \mathbb{Q}' = \emptyset$).

$$\mathbb{N} \subset \mathbb{W} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

#### Fundamental Decimal Taxonomy of Real Numbers

Every real number can be written as a decimal. Its decimal behavior completely determines its algebraic nature:

| Decimal Type | Defining Characteristics | Set Category | Standard Examples |
| :--- | :--- | :--- | :--- |
| **Terminating Decimal** | Digits terminate after a finite count of places. Prime factors of denominator in simplest form are strictly of form $2^m \cdot 5^n$. | **Rational ($\mathbb{Q}$)** | $\frac{3}{8} = 0.375$, $\frac{7}{25} = 0.28$, $\frac{13}{20} = 0.65$ |
| **Non-Terminating Recurring (Repeating)** | Digits never terminate, but a finite block of digits repeats infinitely with period $p$. | **Rational ($\mathbb{Q}$)** | $\frac{1}{3} = 0.\bar{3}$, $\frac{47}{99} = 0.\overline{47}$, $\frac{7}{12} = 0.58\bar{3}$ |
| **Non-Terminating Non-Recurring** | Digits continue infinitely without any periodic or repeating pattern whatsoever. | **Irrational ($\mathbb{Q}'$)** | $\sqrt{2} = 1.4142135\dots$, $\pi = 3.1415926\dots$, $0.1010010001\dots$ |

> ⚠️ **The 22/7 Examination Trap:** Students often claim "$\pi = \frac{22}{7}$, so $\pi$ is rational!"
> This is **incorrect**! $\frac{22}{7} = 3.\overline{142857}$ is a rational approximation used for school calculation. True $\pi$ is the ratio of circle circumference to diameter and is strictly **irrational** with a non-terminating, non-repeating decimal expansion.

---

### 2. Algorithmic Protocol: Expressing Recurring Decimals as $\frac{p}{q}$

Every non-terminating recurring decimal represents a rational number and can be converted into the quotient of integers $\frac{p}{q}$ ($q \neq 0$).

#### Protocol A: Pure Recurring Decimal (All digits after decimal repeat)
* **Step 1:** Let $x$ equal the recurring decimal: $x = 0.\overline{a_1 a_2 \dots a_n}$.
* **Step 2:** Let $n$ be the number of repeating digits (periodicity). Multiply both sides by $10^n$.
* **Step 3:** Subtract the original equation from the multiplied equation. The infinite repeating tails cancel out perfectly!
* **Step 4:** Solve for $x = \frac{p}{q}$ and reduce to simplest form.

#### Worked Example 1 (Express $0.\overline{47}$ in $\frac{p}{q}$ form):
1. Let $x = 0.474747\dots \quad \text{--- (Equation 1)}$
2. Since 2 digits repeat, multiply by $10^2 = 100$:
   $$100x = 47.474747\dots \quad \text{--- (Equation 2)}$$
3. Subtract Eq. 1 from Eq. 2:
   $$100x - x = (47.474747\dots) - (0.474747\dots)$$
   $$99x = 47 \implies \mathbf{x = \frac{47}{99}}$$

#### Protocol B: Mixed Recurring Decimal (Some digits before recurring block)
* **Step 1:** Let $x = 0.2\bar{3} = 0.2333\dots \quad \text{--- (Eq. 1)}$.
* **Step 2:** Multiply by $10$ to move non-repeating digits left of decimal:
   $$10x = 2.333\dots \quad \text{--- (Eq. 2)}$$
* **Step 3:** Multiply by another $10$ to shift one full repeating period:
   $$100x = 23.333\dots \quad \text{--- (Eq. 3)}$$
* **Step 4:** Subtract Eq. 2 from Eq. 3:
   $$100x - 10x = 23.333\dots - 2.333\dots \implies 90x = 21$$
   $$x = \frac{21}{90} = \mathbf{\frac{7}{30}}$$

---

### 3. Representation of Irrationals on the Number Line

By the **Dedekind-Cantor Axiom**, every real number corresponds to a unique point on the number line, and every point represents a real number.

#### The Square Root Spiral (Pythagorean Construction)
We locate square roots of non-square natural numbers ($\sqrt{2}, \sqrt{3}, \sqrt{5}$) using the **Pythagorean Theorem** on a coordinate line:
1. **Locating $\sqrt{2}$:**
   - Mark origin $O(0)$ and point $A(1)$ such that $OA = 1$ unit.
   - Construct perpendicular $AB \perp OA$ of length $1$ unit.
   - In right-angled $\Delta OAB$: $OB = \sqrt{OA^2 + AB^2} = \sqrt{1^2 + 1^2} = \sqrt{2}$.
   - With center $O$ and radius $OB$, draw an arc cutting the number line at $P$. Point $P$ represents $\mathbf{\sqrt{2}} \approx 1.414$.
2. **Locating $\sqrt{3}$:**
   - From point $B$, construct perpendicular $BC \perp OB$ of length $1$ unit.
   - In right $\Delta OBC$: $OC = \sqrt{OB^2 + BC^2} = \sqrt{(\sqrt{2})^2 + 1^2} = \sqrt{3}$.
   - Swing an arc from $O$ with radius $OC$ to mark $\mathbf{\sqrt{3}} \approx 1.732$.
3. **Locating $\sqrt{5}$ in a Single Step:**
   - Draw base $OA = 2$ units along number line.
   - Draw perpendicular $AB = 1$ unit.
   - Hypotenuse $OB = \sqrt{2^2 + 1^2} = \sqrt{4 + 1} = \mathbf{\sqrt{5}}$. Swing arc to mark $\sqrt{5} \approx 2.236$.

---

### 4. Operations on Real Numbers & Rationalization

#### Properties of Combined Operations
1. The sum, difference, product, and quotient of two **rational numbers** is always **rational** (closed under $\mathbb{Q}$).
2. The sum or difference of a **rational** and an **irrational** is always **irrational**:
   $$2 + \sqrt{3} \in \mathbb{Q}', \quad 5 - \sqrt{2} \in \mathbb{Q}'$$
3. The non-zero product or quotient of a **rational** and an **irrational** is **irrational**:
   $$3\sqrt{5} \in \mathbb{Q}', \quad \frac{\sqrt{7}}{2} \in \mathbb{Q}'$$
4. The sum, difference, product, or quotient of two **irrational numbers** may be **rational OR irrational**:
   - $(\sqrt{3}) + (-\sqrt{3}) = 0$ (Rational!)
   - $(\sqrt{2}) \times (\sqrt{8}) = \sqrt{16} = 4$ (Rational!)
   - $\sqrt{2} \times \sqrt{3} = \sqrt{6}$ (Irrational!)

#### Rationalizing the Denominator (Conjugate Multiplication)
When the denominator contains a radical term $\sqrt{a} \pm \sqrt{b}$, we multiply both numerator and denominator by its **conjugate**:
* Conjugate of $(\sqrt{a} + \sqrt{b})$ is $(\sqrt{a} - \sqrt{b})$.
* Using algebraic identity $(x+y)(x-y) = x^2 - y^2$:
  $$(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = (\sqrt{a})^2 - (\sqrt{b})^2 = a - b \quad (\text{Free of radicals!})$$

#### Worked Example 3:
Rationalize the denominator of $\frac{5}{\sqrt{7} - \sqrt{2}}$:
$$\frac{5}{\sqrt{7} - \sqrt{2}} \times \frac{\sqrt{7} + \sqrt{2}}{\sqrt{7} + \sqrt{2}} = \frac{5(\sqrt{7} + \sqrt{2})}{(\sqrt{7})^2 - (\sqrt{2})^2} = \frac{5(\sqrt{7} + \sqrt{2})}{7 - 2} = \frac{5(\sqrt{7} + \sqrt{2})}{5} = \mathbf{\sqrt{7} + \sqrt{2}}$$

---

### 5. Laws of Exponents & Examiner Pitfall Matrix

Let $a, b > 0$ be real bases and $p, q$ be rational exponents:
1. **Product Rule:** $a^p \cdot a^q = a^{p+q}$
2. **Quotient Rule:** $\frac{a^p}{a^q} = a^{p-q}$
3. **Power of Power:** $(a^p)^q = a^{p \cdot q}$
4. **Power of Product:** $a^p \cdot b^p = (ab)^p$
5. **Negative Exponent:** $a^{-p} = \frac{1}{a^p}$
6. **Fractional Exponents & Radicals:** $a^{m/n} = (\sqrt[n]{a})^m = \sqrt[n]{a^m}$, and $a^0 = 1$.

| Common Exam Trap | What the Student Wrote | Why it Loses Marks | Correct CBSE Method |
| :--- | :--- | :--- | :--- |
| **Trap 1: Distributing Square Roots** | $\sqrt{a+b} = \sqrt{a} + \sqrt{b}$. | $\sqrt{9+16} = \sqrt{25} = 5$, but $\sqrt{9}+\sqrt{16} = 3+4 = 7 \neq 5$! | Radicals do NOT distribute over addition or subtraction. |
| **Trap 2: Exponent Addition on Bases** | $2^3 \cdot 3^3 = 6^6$. | Powers only add when bases are identical: $a^p \cdot a^q = a^{p+q}$. | Same powers multiply bases: $(2 \cdot 3)^3 = \mathbf{6^3}$. |
| **Trap 3: Rationalizing Signs** | Multiplied $\frac{1}{3 - \sqrt{2}}$ by $\frac{3 - \sqrt{2}}{3 - \sqrt{2}}$. | Must multiply by the conjugate with opposite sign: $(3 + \sqrt{2})$. | $(3-\sqrt{2})(3+\sqrt{2}) = 9 - 2 = 7$. |

#### Graded HOTS Worked Example (3 Marks):
Find the value of $a$ and $b$ if:
$$\frac{3 + \sqrt{7}}{3 - \sqrt{7}} = a + b\sqrt{7}$$
* **Solution:**
  1. Rationalize LHS by multiplying by conjugate $(3 + \sqrt{7})$:
     $$\text{LHS} = \frac{(3 + \sqrt{7})(3 + \sqrt{7})}{(3 - \sqrt{7})(3 + \sqrt{7})} = \frac{(3 + \sqrt{7})^2}{3^2 - (\sqrt{7})^2}$$
  2. Expand numerator using $(x+y)^2 = x^2 + 2xy + y^2$:
     $$(3 + \sqrt{7})^2 = 3^2 + 2(3)(\sqrt{7}) + (\sqrt{7})^2 = 9 + 6\sqrt{7} + 7 = 16 + 6\sqrt{7}$$
  3. Simplify denominator: $9 - 7 = 2$.
  4. Divide:
     $$\text{LHS} = \frac{16 + 6\sqrt{7}}{2} = \frac{16}{2} + \frac{6\sqrt{7}}{2} = \mathbf{8 + 3\sqrt{7}}$$
  5. Equate with $a + b\sqrt{7}$:
     $$a + b\sqrt{7} = 8 + 3\sqrt{7} \implies \mathbf{a = 8}, \quad \mathbf{b = 3}$$

---

### 6. Historical Foundations, Brahmagupta's Laws & Proof of Irrationality of $\sqrt{2}$

*(NCERT Ganita Manjari Sections 3.1, 3.2, 3.4 & CBSE Competencies)*

#### 1. Brahmagupta's Laws of Debt and Fortune (Brahmasphutasiddhanta, 628 CE)
In the 7th century, Indian mathematician Brahmagupta established the world's first comprehensive arithmetic rules for zero ($\text{Śhūnya}$) and negative numbers using the practical concepts of **Fortunes** (positive assets) and **Debts** (negative liabilities):
1. **Addition:**
   - A fortune plus a fortune is a fortune: $(+5) + (+4) = +9$.
   - A debt plus a debt is a debt: $(-5) + (-4) = -9$.
   - The sum of zero and a debt is a debt; of zero and a fortune is a fortune.
2. **Multiplication:**
   - The product of a debt and a fortune is a debt: $(-3) \times (+4) = -12$.
   - The product of two debts is a fortune: $(-3) \times (-4) = \mathbf{+12}$.
   *(Why? Removing a debt of ₹4 three times increases your net worth by ₹12!)*

#### 2. The Density Property of Rational Numbers (NCERT Section 3.4)
* **Theorem:** The set of rational numbers $\mathbb{Q}$ is **dense**. Between any two distinct rational numbers $r_1$ and $r_2$ (with $r_1 < r_2$), there exist **infinitely many rational numbers**.
* **Constructive Proof:**
  - Let $r_1 = \frac{a}{b}$ and $r_2 = \frac{c}{d}$ where $a, b, c, d \in \mathbb{Z}, b, d > 0$ and $r_1 < r_2$.
  - Define the midpoint:
    $$r_{\text{mid}} = \frac{r_1 + r_2}{2} = \frac{\frac{a}{b} + \frac{c}{d}}{2} = \frac{ad + bc}{2bd}$$
  - Since $ad+bc \in \mathbb{Z}$ and $2bd \in \mathbb{Z}$ ($2bd \neq 0$), $r_{\text{mid}}$ is strictly a rational number.
  - Adding $r_1$ to both sides of $r_1 < r_2$ yields $2r_1 < r_1 + r_2 \implies r_1 < \frac{r_1 + r_2}{2}$.
  - Adding $r_2$ to both sides yields $r_1 + r_2 < 2r_2 \implies \frac{r_1 + r_2}{2} < r_2$.
  - Therefore: $r_1 < r_{\text{mid}} < r_2$. Repeating this process infinitely between $r_1$ and $r_{\text{mid}}$ produces infinitely many rationals.

#### 3. Formal Proof of Irrationality of $\sqrt{2}$ by Contradiction (CBSE Competency C-1.1)
* **Statement:** Prove that $\sqrt{2}$ is an irrational number.
* **Proof by Contradiction:**
  1. Assume, to the contrary, that $\sqrt{2}$ is rational. Then it can be expressed in irreducible fractional form:
     $$\sqrt{2} = \frac{p}{q}$$
     where $p, q$ are positive co-prime integers ($\gcd(p, q) = 1$) and $q \neq 0$.
  2. Squaring both sides:
     $$2 = \frac{p^2}{q^2} \implies p^2 = 2q^2 \quad \text{--- (Equation 1)}$$
  3. Since $2q^2$ is divisible by $2$, $p^2$ is an even integer. By the fundamental property of prime divisibility, if the square of an integer is even, the integer itself must be even:
     $$p = 2k \quad (\text{for some integer } k)$$
  4. Substitute $p = 2k$ into Equation 1:
     $$(2k)^2 = 2q^2 \implies 4k^2 = 2q^2 \implies q^2 = 2k^2$$
  5. This implies $q^2$ is also divisible by $2$, so $q$ must also be an even integer.
  6. **The Contradiction:** Both $p$ and $q$ are even, meaning they share $2$ as a common factor. This directly contradicts our initial premise that $\gcd(p, q) = 1$ ($p$ and $q$ are co-prime).
  7. **Conclusion:** Our assumption that $\sqrt{2}$ is rational is false. Hence, **$\sqrt{2}$ is strictly an irrational number**.

---

<div class="interactive-widget">
  <div class="widget-title">⚡ Interactive Recurring Decimal to Fraction Converter</div>
  <p style="font-size:0.88rem; color:var(--text-muted); margin-bottom:12px;">Convert pure recurring decimals into authentic $\frac{p}{q}$ fractions with full algebraic step proof:</p>
  <div class="widget-inputs">
    <label>Type: 
      <select id="dec_type" style="padding:6px 10px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" onchange="convertRecurringDecimal()">
        <option value="pure1">1-digit repeating ($0.\bar{d}$)</option>
        <option value="pure2">2-digit repeating ($0.\overline{dd}$)</option>
      </select>
    </label>
    <label>Number: <input type="number" id="dec_num" value="3" min="1" max="99" style="width:75px; padding:6px 10px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="convertRecurringDecimal()"></label>
    <button class="btn-notes-toggle" onclick="convertRecurringDecimal()" style="padding:6px 14px; font-weight:700;">Convert to Fraction</button>
  </div>
  <div id="dec-output" style="background:var(--card-bg); padding:14px 18px; border-radius:8px; border:1px solid var(--border); font-size:0.92rem; line-height:1.6; margin-top:10px;">
    <div style="font-weight:700; color:var(--primary); margin-bottom:6px;">Step-by-Step Conversion: $x = 0.\bar{3}$</div>
    <div>• Let $x = 0.333\dots$ &nbsp;<strong>--- (Equation 1)</strong></div>
    <div>• Multiply by $10$: $10x = 3.333\dots$ &nbsp;<strong>--- (Equation 2)</strong></div>
    <div>• Subtract (2) - (1): $9x = 3 \implies \mathbf{x = \frac{3}{9} = \frac{1}{3}}$</div>
  </div>
</div>
