# Chapter 4: Exploring Algebraic Identities

> 👨‍🏫 **Teacher's Masterclass Overview:** Algebraic identities are the power tools of high school algebra! An identity is an equality that holds true for **all possible values** of the variables involved. Unlike ordinary linear equations which are satisfied by single numbers, identities provide universal shortcuts for polynomial multiplication, factoring complex algebraic expressions, mental arithmetic, and geometry proofs. In Class 9 CBSE, you will master the 8 foundational identities, the middle-term splitting technique, and the famous conditional identity where $a + b + c = 0$.

---

### 1. The Compendium of 8 Standard Algebraic Identities

Every Class 9 student must have absolute, instant recall of these 8 identities:

| No. | Identity Name | Algebraic Identity Formula | Primary Utility in Exams |
| :--- | :--- | :--- | :--- |
| **I** | **Square of a Sum** | $(x + y)^2 = x^2 + 2xy + y^2$ | Expanding sums; calculating $(105)^2 = (100+5)^2$. |
| **II** | **Square of a Difference** | $(x - y)^2 = x^2 - 2xy + y^2$ | Expanding differences; calculating $(97)^2 = (100-3)^2$. |
| **III** | **Difference of Two Squares** | $x^2 - y^2 = (x - y)(x + y)$ | Factoring differences; evaluating $104 \times 96 = (100+4)(100-4)$. |
| **IV** | **Product of Linear Binomials** | $(x + a)(x + b) = x^2 + (a + b)x + ab$ | Rapid expansion without FOIL; mental products $103 \times 107$. |
| **V** | **Square of a Trinomial** | $(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx$ | Expanding 3-variable terms; watch for negative signs! |
| **VI** | **Cube of a Sum** | $(x + y)^3 = x^3 + y^3 + 3xy(x + y) = x^3 + 3x^2y + 3xy^2 + y^3$ | Cubic expansion and factoring sum of cubes. |
| **VII** | **Cube of a Difference** | $(x - y)^3 = x^3 - y^3 - 3xy(x - y) = x^3 - 3x^2y + 3xy^2 - y^3$ | Cubic difference expansion; note signs: $+ - + -$. |
| **VIII**| **Sum of Three Cubes Identity** | $x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)$ | Deep algebraic factoring and the conditional shortcut. |

---

### 2. The Conditional Identity: When $x + y + z = 0$

Identity VIII yields the single most tested HOTS theorem in CBSE Class 9 examinations:

$$\text{If } \mathbf{x + y + z = 0}, \quad \text{then} \quad \mathbf{x^3 + y^3 + z^3 = 3xyz}$$

#### Proof:
From Identity VIII:
$$x^3 + y^3 + z^3 - 3xyz = (x + y + z)(x^2 + y^2 + z^2 - xy - yz - zx)$$
If $x + y + z = 0$:
$$x^3 + y^3 + z^3 - 3xyz = (0) \times (x^2 + y^2 + z^2 - xy - yz - zx) = 0$$
$$\implies \mathbf{x^3 + y^3 + z^3 = 3xyz}$$

#### Worked Example 1 (Direct Calculation without Cubing):
Evaluate $(-12)^3 + (7)^3 + (5)^3$ without actual cubing:
* Let $x = -12$, $y = 7$, $z = 5$.
* Check sum: $x + y + z = (-12) + 7 + 5 = -12 + 12 = 0$.
* Since $x + y + z = 0$, apply the conditional identity:
  $$(-12)^3 + 7^3 + 5^3 = 3xyz = 3(-12)(7)(5)$$
  $$= 3(-12)(35) = -36 \times 35 = \mathbf{-1260}$$

---

### 3. Factoring Quadratics by Splitting the Middle Term

To factorize a quadratic trinomial of the form $\mathbf{ax^2 + bx + c}$:

#### The 4-Step Algorithmic Protocol:
1. **Find Product $ac$:** Multiply the leading coefficient $a$ by constant term $c$.
2. **Find Pair $(p, q)$:** Find two real numbers $p$ and $q$ such that:
   - Their sum equals the middle coefficient: $\mathbf{p + q = b}$
   - Their product equals $ac$: $\mathbf{p \cdot q = a \cdot c}$
3. **Split the Middle Term:** Rewrite $bx$ as $px + qx$:
   $$ax^2 + bx + c = ax^2 + px + qx + c$$
4. **Factor by Grouping:** Group in pairs to extract common binomial factors.

#### Worked Example 2:
Factorize $6x^2 + 17x + 5$:
* Step 1: Product $a \cdot c = 6 \times 5 = 30$. Middle coefficient $b = 17$.
* Step 2: Factors of $30$ summing to $17$ are $15$ and $2$ ($15 \times 2 = 30$, $15 + 2 = 17$).
* Step 3: Split $17x$ into $15x + 2x$:
  $$6x^2 + 15x + 2x + 5$$
* Step 4: Group:
  $$3x(2x + 5) + 1(2x + 5) = \mathbf{(2x + 5)(3x + 1)}$$

---

### 4. Expansion of Trinomial Squares & Sign Inversion Protocol

When expanding $(x + y + z)^2 = x^2 + y^2 + z^2 + 2xy + 2yz + 2zx$ with negative terms, always rewrite with explicit addition of negative terms in parentheses:

$$\text{To expand } (2a - 3b - c)^2, \quad \text{write as } [2a + (-3b) + (-c)]^2$$

$$= (2a)^2 + (-3b)^2 + (-c)^2 + 2(2a)(-3b) + 2(-3b)(-c) + 2(-c)(2a)$$
$$= 4a^2 + 9b^2 + c^2 - 12ab + 6bc - 4ca$$

> ⚠️ **The Squared Sign Law:** Squared terms are **ALWAYS positive**!
> In $(-3b)^2$, the result is $+9b^2$, never $-9b^2$! Negative signs appear ONLY in the cross-product terms ($2xy, 2yz, 2zx$).

---

### 5. Examiner's Pitfall Matrix & Graded Solved Examples

| Common Exam Error | What the Student Wrote | Why it Loses Marks | Correct CBSE Method |
| :--- | :--- | :--- | :--- |
| **Trap 1: Dropping Middle Term** | $(x+y)^2 = x^2 + y^2$. | Omitting $2xy$ violates the fundamental expansion identity. | $(x+y)^2 = \mathbf{x^2 + 2xy + y^2}$. |
| **Trap 2: Minus in Cubes** | $(x-y)^3 = x^3 - y^3 - 3x^2y - 3xy^2$. | Last term has double negative: $-3x(-y)^2 = +3xy^2$. | $(x-y)^3 = \mathbf{x^3 - 3x^2y + 3xy^2 - y^3}$. |
| **Trap 3: Evaluated Cubes Directly** | Computed $(-12)^3 = -1728$ directly when asked to use identity. | Instruction explicitly states "without actually calculating the cubes". | Check $x+y+z=0$ and use $3xyz$. |

#### Graded HOTS Solved Example (3 Marks):
If $x + y = 12$ and $xy = 27$, find the numerical value of $x^3 + y^3$.
* **Solution:**
  1. Recall the cubic expansion identity:
     $$(x + y)^3 = x^3 + y^3 + 3xy(x + y)$$
  2. Rearrange to isolate $x^3 + y^3$:
     $$x^3 + y^3 = (x + y)^3 - 3xy(x + y)$$
  3. Substitute given values $x + y = 12$ and $xy = 27$:
     $$x^3 + y^3 = (12)^3 - 3(27)(12)$$
     $$x^3 + y^3 = 1728 - 81(12) = 1728 - 972 = \mathbf{756}$$

---

<div class="interactive-widget">
  <div class="widget-title">⚡ Interactive Algebraic Identity Expander</div>
  <p style="font-size:0.88rem; color:var(--text-muted); margin-bottom:12px;">Select an algebraic identity type and enter coefficients to compute full step-by-step polynomial expansion:</p>
  <div class="widget-inputs">
    <label>Identity:
      <select id="ident_type" style="padding:6px 10px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" onchange="expandIdentity()">
        <option value="sq_plus">Square of Sum: $(ax + b)^2$</option>
        <option value="diff_sq">Difference of Squares: $(ax - b)(ax + b)$</option>
        <option value="lin_prod">Linear Product: $(x + a)(x + b)$</option>
      </select>
    </label>
    <label>$a$: <input type="number" id="ident_a" value="2" style="width:65px; padding:6px 10px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="expandIdentity()"></label>
    <label>$b$: <input type="number" id="ident_b" value="3" style="width:65px; padding:6px 10px; border-radius:6px; border:1px solid var(--border); background:var(--bg); color:var(--text);" oninput="expandIdentity()"></label>
    <button class="btn-notes-toggle" onclick="expandIdentity()" style="padding:6px 14px; font-weight:700;">Expand</button>
  </div>
  <div id="ident-output" style="background:var(--card-bg); padding:14px 18px; border-radius:8px; border:1px solid var(--border); font-size:0.92rem; line-height:1.6; margin-top:10px;">
    <div style="font-weight:700; color:var(--primary); margin-bottom:6px;">Expansion of $(2x + 3)^2$:</div>
    <div>• Using Identity: $(u + v)^2 = u^2 + 2uv + v^2$</div>
    <div>• Step 1: $(2x)^2 = 4x^2$</div>
    <div>• Step 2: $2(2x)(3) = 12x$</div>
    <div>• Step 3: $(3)^2 = 9$</div>
    <div style="margin-top:6px; font-weight:700;">• Result: $\mathbf{4x^2 + 12x + 9}$</div>
  </div>
</div>
