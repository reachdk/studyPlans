"""
Refresher Data Repository for Class 9 Science.
Contains:
1. KEY_TERMS_DATA: Comprehensive glossary of key terms, definitions, formulas, and examples across all chapters.
2. BIOLOGY_DIAGRAMS_DATA: 17 Key Biology diagrams from the GCR PA2 revision material (Cell, Tissues, Reproduction).
3. CHEMISTRY_TABLE_9_1_DATA: NCERT Chapter 9 Tables 9.1(a) and 9.1(b) (Monoatomic and Polyatomic ions, valencies, rules, and quiz data).
"""

KEY_TERMS_DATA = [
    # =========================================================================
    # PHYSICS - CHAPTER 4: DESCRIBING MOTION AROUND US
    # =========================================================================
    {
        "id": "phy_ch4_01",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Reference Point (Origin)",
        "category": "Concept",
        "definition": "A fixed location or point relative to which the position or motion of an object is specified.",
        "formula": "",
        "unit": "",
        "example": "A railway station chosen as the origin to state that a school is 2 km north of it."
    },
    {
        "id": "phy_ch4_02",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Distance",
        "category": "Quantity",
        "definition": "The actual total length of the path traversed by a moving body, irrespective of the direction in which it travels. It is a scalar quantity.",
        "formula": "s = \\text{total path length}",
        "unit": "Metre (\\text{m})",
        "example": "An athlete running once around a 400 m circular track covers a distance of 400 m."
    },
    {
        "id": "phy_ch4_03",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Displacement",
        "category": "Quantity",
        "definition": "The shortest straight-line distance measured from the initial position to the final position of an object, along with direction. It is a vector quantity.",
        "formula": "\\Delta \\vec{s} = \\vec{s}_{\\text{final}} - \\vec{s}_{\\text{initial}}",
        "unit": "Metre (\\text{m})",
        "example": "An athlete returning to the starting point of a track has a displacement of exactly 0 m."
    },
    {
        "id": "phy_ch4_04",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Uniform Motion",
        "category": "Type of Motion",
        "definition": "Motion in which an object covers equal distances in equal intervals of time, no matter how small these time intervals may be.",
        "formula": "v = \\text{constant}",
        "unit": "",
        "example": "A car cruising on an empty highway on cruise control at 60 km/h."
    },
    {
        "id": "phy_ch4_05",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Non-Uniform Motion",
        "category": "Type of Motion",
        "definition": "Motion in which an object covers unequal distances in equal intervals of time, or equal distances in unequal intervals of time.",
        "formula": "v \\neq \\text{constant}",
        "unit": "",
        "example": "A bus navigating congested city traffic with frequent starts and stops."
    },
    {
        "id": "phy_ch4_06",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Speed",
        "category": "Quantity",
        "definition": "The rate of distance covered by an object per unit time. It indicates how fast an object moves without regard to direction (scalar).",
        "formula": "v = \\frac{s}{t}",
        "unit": "\\text{m/s} \\text{ (or km/h)}",
        "example": "A cheetah sprinting at a speed of 30 m/s."
    },
    {
        "id": "phy_ch4_07",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Average Speed",
        "category": "Quantity",
        "definition": "The total distance travelled by an object divided by the total time taken to cover that distance.",
        "formula": "v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{s_{\\text{total}}}{t_{\\text{total}}}",
        "unit": "\\text{m/s}",
        "example": "A train covering 180 km in 3 hours has an average speed of 60 km/h."
    },
    {
        "id": "phy_ch4_08",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Velocity",
        "category": "Quantity",
        "definition": "The rate of displacement of an object per unit time, or speed in a specified direction. It is a vector quantity.",
        "formula": "\\vec{v} = \\frac{\\vec{s}}{t}",
        "unit": "\\text{m/s}",
        "example": "An airplane flying at 250 m/s due East."
    },
    {
        "id": "phy_ch4_09",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Average Velocity (Uniform Acceleration)",
        "category": "Quantity",
        "definition": "The arithmetic mean of initial and final velocity over a given time interval when velocity changes at a uniform rate.",
        "formula": "v_{\\text{avg}} = \\frac{u + v}{2}",
        "unit": "\\text{m/s}",
        "example": "A car accelerating uniformly from 10 m/s to 30 m/s has an average velocity of 20 m/s."
    },
    {
        "id": "phy_ch4_10",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Acceleration",
        "category": "Quantity",
        "definition": "The measure of the rate of change of velocity of an object with respect to time. It is a vector quantity.",
        "formula": "a = \\frac{v - u}{t}",
        "unit": "\\text{m/s}^2",
        "example": "A sports car accelerating from rest (0 m/s) to 20 m/s in 4 s has a = 5 m/s²."
    },
    {
        "id": "phy_ch4_11",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Retardation (Deceleration)",
        "category": "Quantity",
        "definition": "Negative acceleration that occurs when the velocity of an object decreases with time.",
        "formula": "a = -\\left|\\frac{v - u}{t}\\right|",
        "unit": "\\text{m/s}^2",
        "example": "Applying brakes to stop a scooter travelling at 15 m/s in 3 s gives a retardation of 5 m/s²."
    },
    {
        "id": "phy_ch4_12",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Slope of Distance-Time (s-t) Graph",
        "category": "Graph Concept",
        "definition": "The gradient of a distance-time graph, which numerically equals the speed of the moving body.",
        "formula": "\\text{Slope} = \\frac{\\Delta s}{\\Delta t} = \\text{Speed}",
        "unit": "\\text{m/s}",
        "example": "A steeper line on an s-t graph represents an object moving at a higher speed."
    },
    {
        "id": "phy_ch4_13",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Slope of Velocity-Time (v-t) Graph",
        "category": "Graph Concept",
        "definition": "The gradient of a velocity-time graph, which numerically equals the acceleration of the body.",
        "formula": "\\text{Slope} = \\frac{\\Delta v}{\\Delta t} = \\text{Acceleration } (a)",
        "unit": "\\text{m/s}^2",
        "example": "A horizontal line on a v-t graph has slope = 0, indicating zero acceleration (constant velocity)."
    },
    {
        "id": "phy_ch4_14",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Area under Velocity-Time Graph",
        "category": "Graph Concept",
        "definition": "The geometric area enclosed between the velocity-time line and the time axis, which equals the total displacement/distance.",
        "formula": "\\text{Area} = \\int v \\, dt = \\text{Displacement } (s)",
        "unit": "Metre (\\text{m})",
        "example": "Area of the rectangle + triangle under a v-t line during uniform acceleration."
    },
    {
        "id": "phy_ch4_15",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "First Equation of Motion",
        "category": "Kinematic Law",
        "definition": "Velocity-time relation for a body moving with uniform acceleration.",
        "formula": "v = u + at",
        "unit": "",
        "example": "Finding final speed of a stone dropped from a tower after 3 s with a = 9.8 m/s²."
    },
    {
        "id": "phy_ch4_16",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Second Equation of Motion",
        "category": "Kinematic Law",
        "definition": "Position-time relation giving distance covered during uniformly accelerated motion.",
        "formula": "s = ut + \\frac{1}{2}at^2",
        "unit": "",
        "example": "Calculating braking distance of a vehicle coming to a stop."
    },
    {
        "id": "phy_ch4_17",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Third Equation of Motion",
        "category": "Kinematic Law",
        "definition": "Position-velocity relation independent of time elapsed.",
        "formula": "v^2 - u^2 = 2as",
        "unit": "",
        "example": "Determining launch speed needed for a projectile to reach a height of 20 m."
    },
    {
        "id": "phy_ch4_18",
        "sub": "phy",
        "chCode": "Ch 4",
        "chTitle": "Describing Motion Around Us",
        "term": "Uniform Circular Motion",
        "category": "Type of Motion",
        "definition": "Motion of an object along a circular path with constant speed. It is continuously accelerated because direction of velocity changes at every instant.",
        "formula": "v = \\frac{2\\pi r}{T}",
        "unit": "\\text{m/s}",
        "example": "The tip of the seconds hand of a clock, or a satellite in a circular orbit."
    },

    # =========================================================================
    # PHYSICS - CHAPTER 6: HOW FORCES AFFECT MOTION
    # =========================================================================
    {
        "id": "phy_ch6_01",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Force",
        "category": "Quantity",
        "definition": "An external push or pull upon an object resulting from its interaction with another object that can change its state of rest, motion, speed, direction, or shape.",
        "formula": "F = ma",
        "unit": "Newton (\\text{N}) = \\text{kg}\\cdot\\text{m/s}^2",
        "example": "Kicking a football at rest to accelerate it down the field."
    },
    {
        "id": "phy_ch6_02",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Balanced Forces",
        "category": "Concept",
        "definition": "Forces acting on an object whose vector sum (net resultant force) is zero. They do not change the state of rest or uniform motion.",
        "formula": "F_{\\text{net}} = \\sum \\vec{F} = 0",
        "unit": "\\text{N}",
        "example": "A book resting on a table where downward gravity equals upward normal reaction."
    },
    {
        "id": "phy_ch6_03",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Unbalanced Forces",
        "category": "Concept",
        "definition": "Forces acting on an object whose resultant is greater than zero, causing a change in speed, direction, or state of motion (acceleration).",
        "formula": "F_{\\text{net}} = \\sum \\vec{F} \\neq 0",
        "unit": "\\text{N}",
        "example": "A tug-of-war where one team pulls harder, causing both teams to move toward that side."
    },
    {
        "id": "phy_ch6_04",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Inertia",
        "category": "Property",
        "definition": "The inherent natural tendency of an object to resist any change in its state of rest or of uniform motion in a straight line.",
        "formula": "\\text{Inertia} \\propto \\text{Mass } (m)",
        "unit": "Measured by mass (\\text{kg})",
        "example": "Passengers lurching backward when a stationary bus accelerates forward suddenly."
    },
    {
        "id": "phy_ch6_05",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Newton's First Law of Motion",
        "category": "Law",
        "definition": "An object remains in a state of rest or of uniform motion in a straight line unless compelled to change that state by an applied unbalanced force.",
        "formula": "F_{\\text{net}} = 0 \\implies a = 0 \\implies v = \\text{constant}",
        "unit": "",
        "example": "Dust falling from a beaten rug due to inertia of rest of dust particles."
    },
    {
        "id": "phy_ch6_06",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Linear Momentum",
        "category": "Quantity",
        "definition": "The quantity of motion possessed by a moving body, measured as the product of its mass and velocity. It is a vector quantity.",
        "formula": "p = mv",
        "unit": "\\text{kg}\\cdot\\text{m/s}",
        "example": "A massive slow-moving truck having much higher momentum than a fast-moving bicycle."
    },
    {
        "id": "phy_ch6_07",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Newton's Second Law of Motion",
        "category": "Law",
        "definition": "The rate of change of momentum of an object is directly proportional to the applied unbalanced force and takes place in the direction of the force.",
        "formula": "F \\propto \\frac{\\Delta p}{\\Delta t} \\implies F = k \\cdot \\frac{m(v - u)}{t} = ma",
        "unit": "\\text{N}",
        "example": "A cricket fielder pulling his hands backward while catching a ball to increase time and reduce impact force."
    },
    {
        "id": "phy_ch6_08",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Newton's Third Law of Motion",
        "category": "Law",
        "definition": "To every action, there is an equal and opposite reaction. Action and reaction forces act simultaneously on two different bodies.",
        "formula": "\\vec{F}_{AB} = -\\vec{F}_{BA}",
        "unit": "\\text{N}",
        "example": "Recoil of a gun when a bullet is fired, or a swimmer pushing water backward to move forward."
    },
    {
        "id": "phy_ch6_09",
        "sub": "phy",
        "chCode": "Ch 6",
        "chTitle": "How Forces Affect Motion",
        "term": "Law of Conservation of Momentum",
        "category": "Law",
        "definition": "The total momentum of an isolated system remains constant (conserved) in the absence of an external unbalanced force.",
        "formula": "m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2",
        "unit": "\\text{kg}\\cdot\\text{m/s}",
        "example": "Collision between two billiard balls where total momentum before equals total momentum after."
    },

    # =========================================================================
    # PHYSICS - CHAPTER 7: WORK, ENERGY AND SIMPLE MACHINES
    # =========================================================================
    {
        "id": "phy_ch7_01",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Work (Scientific)",
        "category": "Quantity",
        "definition": "Work is done when a force acts on an object and causes displacement in the direction of the force.",
        "formula": "W = F \\cdot s \\cdot \\cos(\\theta)",
        "unit": "Joule (\\text{J}) = \\text{N}\\cdot\\text{m}",
        "example": "Pushing a cart through 5 m with a horizontal force of 20 N does 100 J of work."
    },
    {
        "id": "phy_ch7_02",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "1 Joule of Work",
        "category": "Definition",
        "definition": "The amount of work done when a force of 1 Newton displaces an object through a distance of 1 metre in the direction of the force.",
        "formula": "1\\text{ J} = 1\\text{ N} \\times 1\\text{ m}",
        "unit": "\\text{J}",
        "example": "Lifting an apple (approx. 100 g weight = 1 N) vertically upward by 1 metre."
    },
    {
        "id": "phy_ch7_03",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Negative Work",
        "category": "Concept",
        "definition": "Work done when the force opposes the displacement (angle between force and displacement is 180°).",
        "formula": "W = -F \\cdot s",
        "unit": "\\text{J}",
        "example": "Work done by the force of friction on a skidding car."
    },
    {
        "id": "phy_ch7_04",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Kinetic Energy",
        "category": "Quantity",
        "definition": "The energy possessed by an object by virtue of its motion.",
        "formula": "E_k = \\frac{1}{2}mv^2",
        "unit": "Joule (\\text{J})",
        "example": "A moving bowling ball knocking down stationary pins."
    },
    {
        "id": "phy_ch7_05",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Gravitational Potential Energy",
        "category": "Quantity",
        "definition": "The energy possessed by an object due to its position or height above the ground against gravity.",
        "formula": "E_p = mgh",
        "unit": "Joule (\\text{J})",
        "example": "Water stored at the top of a hydroelectric dam reservoir."
    },
    {
        "id": "phy_ch7_06",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Law of Conservation of Energy",
        "category": "Law",
        "definition": "Energy can neither be created nor destroyed; it can only be transformed from one form to another. The total energy of an isolated system remains constant.",
        "formula": "E_k + E_p = \\text{constant}",
        "unit": "\\text{J}",
        "example": "A freely falling stone losing potential energy while gaining an equal amount of kinetic energy."
    },
    {
        "id": "phy_ch7_07",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Power",
        "category": "Quantity",
        "definition": "The rate of doing work or the rate of transfer of energy per unit time.",
        "formula": "P = \\frac{W}{t} = \\frac{E}{t}",
        "unit": "Watt (\\text{W}) = \\text{J/s}",
        "example": "An electric motor lifting 100 kg water to a 10 m overhead tank in 20 s."
    },
    {
        "id": "phy_ch7_08",
        "sub": "phy",
        "chCode": "Ch 7",
        "chTitle": "Work, Energy and Simple Machines",
        "term": "Commercial Unit of Energy (kWh)",
        "category": "Unit",
        "definition": "The electrical energy consumed by an appliance of power 1000 Watts operating continuously for 1 hour.",
        "formula": "1\\text{ kWh} = 1\\text{ Unit} = 3.6 \\times 10^6\\text{ J}",
        "unit": "\\text{kWh}",
        "example": "A 100 W bulb running for 10 hours consumes 1 kWh (1 board of trade unit)."
    },

    # =========================================================================
    # CHEMISTRY - CHAPTER 5: EXPLORING MIXTURES & THEIR SEPARATION
    # =========================================================================
    {
        "id": "chem_ch5_01",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Pure Substance",
        "category": "Concept",
        "definition": "A substance consisting of a single type of constituent particle with uniform chemical composition throughout (elements or compounds).",
        "formula": "",
        "unit": "",
        "example": "Pure distilled water (H₂O), pure copper metal (Cu), or sucrose crystals."
    },
    {
        "id": "chem_ch5_02",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Homogeneous Mixture",
        "category": "Classification",
        "definition": "A mixture that has uniform composition and properties throughout; its components cannot be distinguished separately.",
        "formula": "",
        "unit": "",
        "example": "Salt dissolved completely in water, or air (mixture of gases)."
    },
    {
        "id": "chem_ch5_03",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Heterogeneous Mixture",
        "category": "Classification",
        "definition": "A mixture that does not have uniform composition throughout; visible boundaries of separation exist between components.",
        "formula": "",
        "unit": "",
        "example": "Mixture of sand and iron filings, or oil floating on water."
    },
    {
        "id": "chem_ch5_04",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "True Solution",
        "category": "Classification",
        "definition": "A homogeneous mixture of two or more substances where solute particles are smaller than 1 nm (10⁻⁹ m) and do not scatter light.",
        "formula": "\\text{Particle size} < 1\\text{ nm}",
        "unit": "",
        "example": "Copper sulfate dissolved in water (clear, homogeneous, passes through filter paper)."
    },
    {
        "id": "chem_ch5_05",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Suspension",
        "category": "Classification",
        "definition": "A heterogeneous mixture in which solute particles are larger than 100 nm, remain suspended in the medium, and settle down upon standing.",
        "formula": "\\text{Particle size} > 100\\text{ nm}",
        "unit": "",
        "example": "Chalk powder in water, or muddy river water."
    },
    {
        "id": "chem_ch5_06",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Colloid (Colloidal Solution)",
        "category": "Classification",
        "definition": "A heterogeneous mixture where particle size lies between 1 nm and 100 nm; particles do not settle upon standing and scatter light.",
        "formula": "1\\text{ nm} \\le \\text{Size} \\le 100\\text{ nm}",
        "unit": "",
        "example": "Milk, gelatin, fog, ink, or blood."
    },
    {
        "id": "chem_ch5_07",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Tyndall Effect",
        "category": "Phenomenon",
        "definition": "The scattering of a beam of light by colloidal particles, making the path of light visible.",
        "formula": "",
        "unit": "",
        "example": "Sunlight streaming through a canopy of a dense forest or dust in a cinema projector beam."
    },
    {
        "id": "chem_ch5_08",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Mass by Mass Percentage",
        "category": "Formula",
        "definition": "The concentration of a solution expressed as the mass of solute per 100 grams of solution.",
        "formula": "\\text{Mass } \\% = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100 = \\frac{\\text{Mass of Solute}}{\\text{Solute} + \\text{Solvent}} \\times 100",
        "unit": "\\%",
        "example": "Dissolving 40 g of salt in 320 g of water gives a (40 / 360) × 100 = 11.1% solution."
    },
    {
        "id": "chem_ch5_09",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Saturated Solution",
        "category": "Concept",
        "definition": "A solution in which no more solute can be dissolved at that specific temperature.",
        "formula": "",
        "unit": "",
        "example": "Adding table salt to water until solid salt begins accumulating at the beaker bottom."
    },
    {
        "id": "chem_ch5_10",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Fractional Distillation",
        "category": "Separation Technique",
        "definition": "Process used to separate a mixture of two or more miscible liquids for which the difference in boiling points is less than 25 K.",
        "formula": "\\Delta T_b < 25\\text{ K}",
        "unit": "",
        "example": "Separating various gases from liquefied air, or refining petroleum fractions."
    },
    {
        "id": "chem_ch5_11",
        "sub": "chem",
        "chCode": "Ch 5",
        "chTitle": "Exploring Mixtures & Their Separation",
        "term": "Chromatography",
        "category": "Separation Technique",
        "definition": "Technique used for the separation of solutes that dissolve in the same solvent based on their differential solubility and travel rates.",
        "formula": "",
        "unit": "",
        "example": "Separating colored dyes in black sketch pen ink on filter paper."
    },

    # =========================================================================
    # CHEMISTRY - CHAPTER 8: JOURNEY INSIDE THE ATOM
    # =========================================================================
    {
        "id": "chem_ch8_01",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Electron",
        "category": "Subatomic Particle",
        "definition": "Negatively charged subatomic particle discovered by J.J. Thomson having a relative charge of -1 and negligible mass (1/1836 of proton).",
        "formula": "e^-, \\text{ charge} = -1.6 \\times 10^{-19}\\text{ C}, \\text{ mass} \\approx 9.1 \\times 10^{-31}\\text{ kg}",
        "unit": "",
        "example": "Cathode rays produced in a discharge tube."
    },
    {
        "id": "chem_ch8_02",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Proton",
        "category": "Subatomic Particle",
        "definition": "Positively charged subatomic particle discovered by E. Goldstein (canal rays) situated in the atomic nucleus, having a charge of +1.",
        "formula": "p^+, \\text{ charge} = +1.6 \\times 10^{-19}\\text{ C}, \\text{ mass} \\approx 1.672 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}",
        "unit": "",
        "example": "Hydrogen nucleus (single proton)."
    },
    {
        "id": "chem_ch8_03",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Neutron",
        "category": "Subatomic Particle",
        "definition": "Subatomic particle discovered by J. Chadwick (1932) having no electrical charge and mass nearly equal to that of a proton.",
        "formula": "n^0, \\text{ charge} = 0, \\text{ mass} \\approx 1.674 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}",
        "unit": "",
        "example": "Present in all atomic nuclei except ordinary protium hydrogen (¹H)."
    },
    {
        "id": "chem_ch8_04",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Rutherford's Alpha Particle Scattering Experiment",
        "category": "Historical Experiment",
        "definition": "Experiment firing α-particles (He²⁺) at a thin gold foil, revealing that most of the atom is empty space and positive charge is concentrated in a tiny nucleus.",
        "formula": "",
        "unit": "",
        "example": "1 in 12,000 α-particles rebounded at 180°, proving the dense positive nucleus."
    },
    {
        "id": "chem_ch8_05",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Bohr's Atomic Model",
        "category": "Atomic Theory",
        "definition": "Model proposing that electrons revolve in discrete non-radiating orbits (energy levels: K, L, M, N) around the positive nucleus.",
        "formula": "2n^2 \\text{ maximum electrons per shell}",
        "unit": "",
        "example": "K shell (n=1) max 2 electrons; L shell (n=2) max 8 electrons."
    },
    {
        "id": "chem_ch8_06",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Valence Electrons",
        "category": "Concept",
        "definition": "Electrons present in the outermost shell of an atom that determine its chemical reactivity and bonding capacity.",
        "formula": "",
        "unit": "",
        "example": "Sodium (2, 8, 1) has 1 valence electron; Chlorine (2, 8, 7) has 7 valence electrons."
    },
    {
        "id": "chem_ch8_07",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Valency",
        "category": "Concept",
        "definition": "The combining capacity of an atom of an element to achieve a stable octet (8 electrons) in its outermost shell.",
        "formula": "\\text{Valency} = v \\text{ (if } v \\le 4) \\text{ or } 8 - v \\text{ (if } v > 4)",
        "unit": "",
        "example": "Oxygen (2, 6) has valency = 8 - 6 = 2; Aluminium (2, 8, 3) has valency = 3."
    },
    {
        "id": "chem_ch8_08",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Atomic Number (Z)",
        "category": "Quantity",
        "definition": "The total number of protons present in the nucleus of an atom of an element.",
        "formula": "Z = \\text{Number of protons } (p)",
        "unit": "",
        "example": "Carbon has Z = 6; Sodium has Z = 11."
    },
    {
        "id": "chem_ch8_09",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Mass Number (A)",
        "category": "Quantity",
        "definition": "The total number of protons and neutrons (nucleons) present in the nucleus of an atom.",
        "formula": "A = \\text{Protons } (p) + \\text{Neutrons } (n) = Z + n",
        "unit": "Unified mass (\\text{u})",
        "example": "Carbon-12 has 6 protons + 6 neutrons, so A = 12."
    },
    {
        "id": "chem_ch8_10",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Isotopes",
        "category": "Classification",
        "definition": "Atoms of the same element having the same atomic number (Z) but different mass numbers (A) due to different numbers of neutrons.",
        "formula": "{}^{A}_Z X",
        "unit": "",
        "example": "Chlorine-35 and Chlorine-37 (both Z = 17, with 18 and 20 neutrons)."
    },
    {
        "id": "chem_ch8_11",
        "sub": "chem",
        "chCode": "Ch 8",
        "chTitle": "Journey Inside the Atom",
        "term": "Isobars",
        "category": "Classification",
        "definition": "Atoms of different chemical elements having the same mass number (A) but different atomic numbers (Z).",
        "formula": "",
        "unit": "",
        "example": "Argon ({}^{40}_{18}\\text{Ar}) and Calcium ({}^{40}_{20}\\text{Ca})."
    },

    # =========================================================================
    # CHEMISTRY - CHAPTER 9: ATOMIC FOUNDATIONS OF MATTER
    # =========================================================================
    {
        "id": "chem_ch9_01",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Law of Conservation of Mass",
        "category": "Chemical Law",
        "definition": "Mass can neither be created nor destroyed in a chemical reaction. Total mass of reactants equals total mass of products.",
        "formula": "\\sum m_{\\text{reactants}} = \\sum m_{\\text{products}}",
        "unit": "\\text{g}",
        "example": "Barium chloride + Sodium sulfate → Barium sulfate ↓ + Sodium chloride (mass flask remains unchanged)."
    },
    {
        "id": "chem_ch9_02",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Law of Constant Proportions (Proust)",
        "category": "Chemical Law",
        "definition": "In a chemical substance, elements are always present in definite proportions by mass regardless of source or preparation method.",
        "formula": "\\text{Mass Ratio} = \\text{constant}",
        "unit": "",
        "example": "Water (H₂O) always contains Hydrogen and Oxygen in a 1 : 8 mass ratio."
    },
    {
        "id": "chem_ch9_03",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Atomic Mass Unit (Unified Mass, u)",
        "category": "Unit",
        "definition": "A mass unit equal to exactly one-twelfth (1/12th) the mass of one atom of carbon-12 isotope.",
        "formula": "1\\text{ u} = \\frac{1}{12} m({}^{12}\\text{C}) \\approx 1.6605 \\times 10^{-27}\\text{ kg}",
        "unit": "\\text{u}",
        "example": "Hydrogen atom mass = 1 u; Oxygen atom mass = 16 u."
    },
    {
        "id": "chem_ch9_04",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Atomicity",
        "category": "Property",
        "definition": "The number of atoms constituting a single molecule of an element.",
        "formula": "",
        "unit": "",
        "example": "Helium is monoatomic (1), O₂ is diatomic (2), Ozone O₃ is triatomic (3), Sulfur S₈ is polyatomic (8)."
    },
    {
        "id": "chem_ch9_05",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Cation",
        "category": "Ion",
        "definition": "A positively charged ion formed when an atom loses one or more valence electrons.",
        "formula": "\\text{M} \\to \\text{M}^{n+} + n e^-",
        "unit": "",
        "example": "Sodium ion: Na → Na⁺ + e⁻."
    },
    {
        "id": "chem_ch9_06",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Anion",
        "category": "Ion",
        "definition": "A negatively charged ion formed when an atom gains one or more valence electrons.",
        "formula": "\\text{X} + n e^- \\to \\text{X}^{n-}",
        "unit": "",
        "example": "Chloride ion: Cl + e⁻ → Cl⁻."
    },
    {
        "id": "chem_ch9_07",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Polyatomic Ion",
        "category": "Ion",
        "definition": "A group of atoms carrying a net positive or negative electrical charge.",
        "formula": "\\text{e.g. } \\text{NH}_4^+, \\text{SO}_4^{2-}, \\text{CO}_3^{2-}, \\text{OH}^-",
        "unit": "",
        "example": "Sulfate ion (SO₄²⁻) consisting of 1 sulfur and 4 oxygen atoms with an overall 2- charge."
    },
    {
        "id": "chem_ch9_08",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Molecular Mass",
        "category": "Quantity",
        "definition": "The sum of the atomic masses of all the atoms in a molecule of a substance.",
        "formula": "M(\\text{H}_2\\text{O}) = 2(1) + 16 = 18\\text{ u}",
        "unit": "Unified mass (\\text{u})",
        "example": "Molecular mass of HNO₃ = 1 + 14 + (3 × 16) = 63 u."
    },
    {
        "id": "chem_ch9_09",
        "sub": "chem",
        "chCode": "Ch 9",
        "chTitle": "Atomic Foundations of Matter",
        "term": "Formula Unit Mass",
        "category": "Quantity",
        "definition": "The sum of atomic masses of all atoms in a formula unit of an ionic compound.",
        "formula": "M(\\text{NaCl}) = 23 + 35.5 = 58.5\\text{ u}",
        "unit": "\\text{u}",
        "example": "Formula unit mass of CaCl₂ = 40 + (2 × 35.5) = 111 u."
    },

    # =========================================================================
    # BIOLOGY - CHAPTER 2: CELL — THE BUILDING BLOCK OF LIFE
    # =========================================================================
    {
        "id": "bio_ch2_01",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Cell",
        "category": "Fundamental Concept",
        "definition": "The basic structural, functional, and biological unit of all living organisms, capable of independent existence.",
        "formula": "",
        "unit": "",
        "example": "A single amoeba cell carrying out digestion, respiration, and reproduction."
    },
    {
        "id": "bio_ch2_02",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Cell Theory",
        "category": "Biological Theory",
        "definition": "Formulated by Schleiden, Schwann, and Virchow: 1) All living beings are composed of cells; 2) The cell is the basic unit of life; 3) All cells arise from pre-existing cells (Omnis cellula-e cellula).",
        "formula": "",
        "unit": "",
        "example": "Every new body cell in an organism arises by mitotic division of parent cells."
    },
    {
        "id": "bio_ch2_03",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Plasma Membrane (Cell Membrane)",
        "category": "Organelle / Structure",
        "definition": "A flexible, living, selectively permeable membrane composed of a phospholipid bilayer with embedded proteins, regulating the entry and exit of substances.",
        "formula": "",
        "unit": "",
        "example": "Permits oxygen and nutrients to enter while keeping cellular macromolecules inside."
    },
    {
        "id": "bio_ch2_04",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Diffusion",
        "category": "Transport Mechanism",
        "definition": "Spontaneous net movement of particles from a region of higher concentration to a region of lower concentration down a concentration gradient.",
        "formula": "",
        "unit": "",
        "example": "Exchange of carbon dioxide (CO₂) and oxygen (O₂) gas across alveolar cell membranes."
    },
    {
        "id": "bio_ch2_05",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Osmosis",
        "category": "Transport Mechanism",
        "definition": "The net passage of water molecules from a region of higher water concentration to lower water concentration across a selectively permeable membrane.",
        "formula": "",
        "unit": "",
        "example": "Dried raisins swelling when soaked in pure water (endosmosis)."
    },
    {
        "id": "bio_ch2_06",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Hypotonic Solution",
        "category": "Solution Type",
        "definition": "A solution whose solute concentration is lower (higher water potential) than the cell cytoplasm, causing endosmosis and cell swelling/turgidity.",
        "formula": "",
        "unit": "",
        "example": "Plant cells placed in tap water becoming turgid without bursting due to cell wall."
    },
    {
        "id": "bio_ch2_07",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Hypertonic Solution",
        "category": "Solution Type",
        "definition": "A solution whose solute concentration is higher (lower water potential) than the cell interior, causing exosmosis and shrinkage.",
        "formula": "",
        "unit": "",
        "example": "RBCs shrinking and crenating in concentrated brine solution."
    },
    {
        "id": "bio_ch2_08",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Plasmolysis",
        "category": "Phenomenon",
        "definition": "Shrinkage or contraction of the protoplasm away from the plant cell wall when placed in a hypertonic solution due to exosmosis.",
        "formula": "",
        "unit": "",
        "example": "Rhoeo leaf epidermal cells shedding water and shrinking away from the wall in salt solution."
    },
    {
        "id": "bio_ch2_09",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Nucleus",
        "category": "Organelle",
        "definition": "The command center of a eukaryotic cell, enclosed in a double-layered nuclear envelope with pores, containing genetic material (DNA/chromatin) and nucleolus.",
        "formula": "",
        "unit": "",
        "example": "Directs protein synthesis and cellular reproduction."
    },
    {
        "id": "bio_ch2_10",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Prokaryotic Cell",
        "category": "Cell Classification",
        "definition": "Primitive cell lacking a membrane-bound true nucleus and membrane-bound organelles; genetic material lies in an undefined region called nucleoid.",
        "formula": "",
        "unit": "",
        "example": "Bacteria (E. coli), blue-green algae (Cyanobacteria)."
    },
    {
        "id": "bio_ch2_11",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Eukaryotic Cell",
        "category": "Cell Classification",
        "definition": "Advanced cell having a well-defined membrane-bound nucleus and specialized membrane-bound organelles (mitochondria, plastids, ER, Golgi).",
        "formula": "",
        "unit": "",
        "example": "Onion peel plant cell, human cheek epithelial cell."
    },
    {
        "id": "bio_ch2_12",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Endoplasmic Reticulum (RER & SER)",
        "category": "Organelle",
        "definition": "Interconnecting network of membranous tubules and sheets. RER has ribosomes and manufactures proteins; SER synthesizes lipids/fats and detoxifies poisons.",
        "formula": "",
        "unit": "",
        "example": "Liver SER detoxifying drugs and toxins in vertebrates."
    },
    {
        "id": "bio_ch2_13",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Golgi Apparatus",
        "category": "Organelle",
        "definition": "System of membrane-bound parallel flattened sacs (cisternae) involved in the storage, modification, packaging, and dispatch of cellular products.",
        "formula": "",
        "unit": "",
        "example": "Packages proteins into secretory vesicles and synthesizes lysosomes."
    },
    {
        "id": "bio_ch2_14",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Lysosomes ('Suicide Bags')",
        "category": "Organelle",
        "definition": "Membrane-bound digestive sacs containing powerful hydrolytic enzymes that digest foreign material and damaged cell parts.",
        "formula": "",
        "unit": "",
        "example": "Autophagy: bursts to digest a damaged cell from within during starvation or infection."
    },
    {
        "id": "bio_ch2_15",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Mitochondria ('Powerhouse of the Cell')",
        "category": "Organelle",
        "definition": "Double-membrane organelle whose deeply folded inner membrane (cristae) carries out cellular respiration, synthesizing energy in the form of ATP.",
        "formula": "\\text{ATP} = \\text{Adenosine Triphosphate}",
        "unit": "",
        "example": "Muscle cells contain thousands of mitochondria to fuel contraction."
    },
    {
        "id": "bio_ch2_16",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Chloroplasts",
        "category": "Organelle",
        "definition": "Double-membrane plant plastids containing green chlorophyll pigment and thylakoid stacks (grana) where photosynthesis occurs.",
        "formula": "6\\text{CO}_2 + 6\\text{H}_2\\text{O} \\xrightarrow{\\text{Light}} \\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2",
        "unit": "",
        "example": "Mesophyll cells in leaves capturing sunlight."
    },
    {
        "id": "bio_ch2_17",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Mitosis",
        "category": "Cell Division",
        "definition": "Equational cell division in somatic cells where one diploid parent cell divides once to produce two genetically identical diploid daughter cells for growth and repair.",
        "formula": "2n \\to 2n + 2n",
        "unit": "",
        "example": "Skin healing after a scratch."
    },
    {
        "id": "bio_ch2_18",
        "sub": "bio",
        "chCode": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "term": "Meiosis",
        "category": "Cell Division",
        "definition": "Reductional cell division in reproductive organs producing four genetically diverse haploid gametes with half the chromosome number.",
        "formula": "2n \\to n + n + n + n",
        "unit": "",
        "example": "Formation of sperms and egg cells in gonads."
    },

    # =========================================================================
    # BIOLOGY - CHAPTER 3: TISSUES IN ACTION
    # =========================================================================
    {
        "id": "bio_ch3_01",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Tissue",
        "category": "Biological Concept",
        "definition": "A group of similar cells having a common origin that work together to perform a specific function.",
        "formula": "",
        "unit": "",
        "example": "Phloem tissue transporting food, or blood transporting oxygen and nutrients."
    },
    {
        "id": "bio_ch3_02",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Meristematic Tissue",
        "category": "Plant Tissue",
        "definition": "Actively dividing plant tissue with thin cellulose walls, dense cytoplasm, prominent nuclei, and no vacuoles, responsible for growth.",
        "formula": "",
        "unit": "",
        "example": "Root tips and shoot apexes showing rapid cell division."
    },
    {
        "id": "bio_ch3_03",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Apical Meristem",
        "category": "Plant Tissue",
        "definition": "Meristematic tissue present at the growing tips of stems and roots that increases the length of the plant (primary growth).",
        "formula": "",
        "unit": "",
        "example": "Elongation of shoot tips towards light and root tips deeper into soil."
    },
    {
        "id": "bio_ch3_04",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Lateral Meristem (Cambium)",
        "category": "Plant Tissue",
        "definition": "Meristematic tissue situated laterally along the circumference that increases the girth/thickness of stem and root (secondary growth).",
        "formula": "",
        "unit": "",
        "example": "Formation of annual growth rings in woody tree trunks."
    },
    {
        "id": "bio_ch3_05",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Parenchyma",
        "category": "Plant Tissue",
        "definition": "Living, unspecialized simple permanent tissue with thin cell walls and large intercellular spaces, acting as basic packing and food storage tissue.",
        "formula": "",
        "unit": "",
        "example": "Flesh of potato tubers storing starch grains."
    },
    {
        "id": "bio_ch3_06",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Collenchyma",
        "category": "Plant Tissue",
        "definition": "Living mechanical tissue with cells irregularly thickened at corners with pectin/cellulose, providing tensile strength and flexibility without breaking.",
        "formula": "",
        "unit": "",
        "example": "Leaf stalks (petioles) bending easily in strong winds without snapping."
    },
    {
        "id": "bio_ch3_07",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Sclerenchyma",
        "category": "Plant Tissue",
        "definition": "Dead permanent tissue with long, narrow cells with uniformly heavily lignified secondary cell walls and narrow lumen, providing rigidity and hardness.",
        "formula": "",
        "unit": "",
        "example": "Hard husk of a coconut (coir fibres) and shell of walnuts."
    },
    {
        "id": "bio_ch3_08",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Xylem",
        "category": "Vascular Tissue",
        "definition": "Complex vascular tissue conducting water and dissolved minerals unidirectionally from roots to aerial parts; composed of tracheids, vessels, xylem fibres, and xylem parenchyma.",
        "formula": "\\text{Root} \\to \\text{Stem} \\to \\text{Leaves (Unidirectional)}",
        "unit": "",
        "example": "Sap ascent in tall Eucalyptus trees."
    },
    {
        "id": "bio_ch3_09",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Phloem",
        "category": "Vascular Tissue",
        "definition": "Complex vascular tissue conducting prepared organic food bidirectionally from photosynthetic leaves to storage and growing organs; composed of sieve tubes, companion cells, phloem parenchyma, and phloem fibres.",
        "formula": "\\text{Bidirectional Translocation}",
        "unit": "",
        "example": "Transporting sucrose from leaves to developing fruits and roots."
    },
    {
        "id": "bio_ch3_10",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Epithelial Tissue",
        "category": "Animal Tissue",
        "definition": "Tightly packed cellular sheet covering body surfaces, cavities, and organs with minimal intercellular matrix, resting on a basement membrane.",
        "formula": "",
        "unit": "",
        "example": "Skin epidermis (stratified squamous), inner lining of mouth (squamous), kidney tubules (cuboidal)."
    },
    {
        "id": "bio_ch3_11",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Connective Tissue",
        "category": "Animal Tissue",
        "definition": "Tissue with loosely spaced living cells embedded in an intercellular matrix (fluid, jelly, or rigid) that binds, supports, and cushions organs.",
        "formula": "",
        "unit": "",
        "example": "Bone (calcium-phosphate matrix), blood (plasma matrix), and adipose (fat storage)."
    },
    {
        "id": "bio_ch3_12",
        "sub": "bio",
        "chCode": "Ch 3",
        "chTitle": "Tissues in Action",
        "term": "Neuron",
        "category": "Nervous Tissue",
        "definition": "Structural and functional unit of the nervous system consisting of a cyton (cell body), branched dendrites for receiving stimuli, and a long axon for conducting impulses.",
        "formula": "",
        "unit": "",
        "example": "Transmitting sensory reflex signals from fingertip to spinal cord upon touching a hot flame."
    },

    # =========================================================================
    # BIOLOGY - CHAPTER 11: REPRODUCTION: HOW LIFE CONTINUES
    # =========================================================================
    {
        "id": "bio_ch11_01",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Asexual Reproduction",
        "category": "Mode of Reproduction",
        "definition": "Production of offspring from a single parent without the involvement of gametes or fertilisation, resulting in genetically identical clones.",
        "formula": "",
        "unit": "",
        "example": "Binary fission in Amoeba, budding in Hydra."
    },
    {
        "id": "bio_ch11_02",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Sexual Reproduction",
        "category": "Mode of Reproduction",
        "definition": "Mode of reproduction involving two parents producing male and female gametes that fuse during fertilisation to yield genetically diverse offspring.",
        "formula": "\\text{Sperm } (n) + \\text{Ovum } (n) \\to \\text{Zygote } (2n)",
        "unit": "",
        "example": "Reproduction in flowering plants and humans."
    },
    {
        "id": "bio_ch11_03",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Vegetative Propagation",
        "category": "Plant Reproduction",
        "definition": "Asexual reproduction in plants where new individuals develop from vegetative parts such as roots, stems, or leaves (cutting, grafting, layering).",
        "formula": "",
        "unit": "",
        "example": "Bryophyllum leaves producing plantlets in marginal notches."
    },
    {
        "id": "bio_ch11_04",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Grafting",
        "category": "Horticultural Method",
        "definition": "Artificial propagation technique where a shoot with buds (scion) from a desired plant is joined onto the rooted rootstock (stock) of another plant.",
        "formula": "",
        "unit": "",
        "example": "Grafting superior commercial apple cultivars onto disease-resistant rootstocks."
    },
    {
        "id": "bio_ch11_05",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Pollination",
        "category": "Process",
        "definition": "The transfer of pollen grains from the anther of a stamen to the receptive stigma of a carpel/pistil.",
        "formula": "",
        "unit": "",
        "example": "Honeybees transferring pollen between mustard flowers."
    },
    {
        "id": "bio_ch11_06",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Fertilisation",
        "category": "Process",
        "definition": "The fusion of the male gamete (sperm/pollen nucleus) with the female gamete (egg cell/ovum) to form a single-celled diploid zygote.",
        "formula": "n + n = 2n \\text{ (Zygote)}",
        "unit": "",
        "example": "Fertilisation occurring in the ampullary region of the human fallopian tube."
    },
    {
        "id": "bio_ch11_07",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Placenta",
        "category": "Reproductive Structure",
        "definition": "A special disc-shaped vascular tissue embedded in the uterine wall that provides nutrition and oxygen from the mother to the developing embryo and removes metabolic wastes.",
        "formula": "",
        "unit": "",
        "example": "Human umbilical cord connecting foetus to the uterine placenta."
    },
    {
        "id": "bio_ch11_08",
        "sub": "bio",
        "chCode": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "term": "Menstruation",
        "category": "Physiological Cycle",
        "definition": "The monthly periodic shedding of the unfertilised ovum and thickened, vascularized uterine endometrial lining through the vagina, lasting 3–5 days.",
        "formula": "\\text{Cycle duration } \\approx 28\\text{ days}",
        "unit": "",
        "example": "Occurs when fertilisation does not take place following ovulation."
    }
]


BIOLOGY_DIAGRAMS_DATA = [
    # -------------------------------------------------------------------------
    # TISSUES (CHAPTER 3)
    # -------------------------------------------------------------------------
    {
        "id": "diag_01",
        "figCode": "Fig. 3.8",
        "chapter": "Ch 3",
        "chTitle": "Tissues in Action",
        "title": "Various Types of Simple Permanent Tissues",
        "sub": "bio",
        "ncertPage": 5,
        "pdfPath": "downloads/class-09/science/exploration/iesc103--tissues-in-action.pdf#page=5",
        "labels": [
            {"part": "Parenchyma (TS & LS)", "desc": "Thin cellulose cell walls, large central vacuole, prominent nucleus, distinct intercellular spaces."},
            {"part": "Collenchyma (TS & LS)", "desc": "Irregular wall thickenings at corners with pectin and cellulose, smaller vacuole, narrow intercellular spaces."},
            {"part": "Sclerenchyma (Fibre & Sclereid)", "desc": "Uniformly thick lignified secondary wall, narrow empty central lumen, simple pits, dead at maturity."}
        ],
        "mustDraw": [
            "Transverse vs Longitudinal sections showing wall thickness differences",
            "Clear intercellular spaces in parenchyma vs pectin-filled corners in collenchyma",
            "Lignified wall with narrow empty lumen in sclerenchyma fibres"
        ],
        "examinerTip": "Students often draw collenchyma with empty spaces; emphasize corner thickening with pectin! Note that sclerenchyma cells are dead and have no protoplasm.",
        "svgType": "permanent_tissues"
    },
    {
        "id": "diag_02",
        "figCode": "Fig. 3.9",
        "chapter": "Ch 3",
        "chTitle": "Tissues in Action",
        "title": "Vascular Tissues: (a) Xylem and (b) Phloem",
        "sub": "bio",
        "ncertPage": 6,
        "pdfPath": "downloads/class-09/science/exploration/iesc103--tissues-in-action.pdf#page=6",
        "labels": [
            {"part": "Tracheid", "desc": "Elongated dead tubular cell with tapering chisel-like ends and pitted lignified walls."},
            {"part": "Vessel Member", "desc": "Wider cylindrical tube with open perforated end plates, forming continuous conduits."},
            {"part": "Xylem Parenchyma", "desc": "Only living xylem component; stores starch/fat and conducts water radially."},
            {"part": "Sieve Tube Element", "desc": "Living tubular cell with perforated end sieve plates; loses nucleus at maturity."},
            {"part": "Companion Cell", "desc": "Specialized parenchymatous cell with prominent nucleus controlling sieve tube transport."}
        ],
        "mustDraw": [
            "Perforated sieve plate pores in phloem sieve tube",
            "Adjacent companion cell with distinct nucleus maintaining metabolic control",
            "Tapering ends of tracheids vs open continuous ends of xylem vessels"
        ],
        "examinerTip": "In xylem, only parenchyma is living; in phloem, only fibres are dead. Always show companion cells alongside sieve tubes!",
        "svgType": "vascular_tissues"
    },
    {
        "id": "diag_03",
        "figCode": "Fig. 3.10",
        "chapter": "Ch 3",
        "chTitle": "Tissues in Action",
        "title": "Tissue Systems in Plants",
        "sub": "bio",
        "ncertPage": 6,
        "pdfPath": "downloads/class-09/science/exploration/iesc103--tissues-in-action.pdf#page=6",
        "labels": [
            {"part": "Epidermal Tissue System", "desc": "Outermost protective single layer of cells covered by waxy cuticle with stomatal pores."},
            {"part": "Ground / Fundamental System", "desc": "Bulk of interior tissue (cortex, endodermis, pericycle, pith) performing photosynthesis and storage."},
            {"part": "Vascular Tissue System", "desc": "Centrally arranged xylem and phloem bundles conducting water and nutrients."}
        ],
        "mustDraw": [
            "Concentric concentric concentric arrangement: Epidermis (outer) → Cortex (middle) → Vascular Bundles (inner)",
            "Label of cuticle on outer epidermal surface"
        ],
        "examinerTip": "Remember the three concentric zones: Epidermal, Ground, and Vascular. Do not interchange cortex with pith.",
        "svgType": "tissue_systems"
    },

    # -------------------------------------------------------------------------
    # CELL (CHAPTER 2)
    # -------------------------------------------------------------------------
    {
        "id": "diag_04",
        "figCode": "Fig. 2.7",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Structure of a Cell Membrane (Fluid Mosaic Model)",
        "sub": "bio",
        "ncertPage": 5,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=5",
        "labels": [
            {"part": "Hydrophilic Polar Head", "desc": "Water-loving phosphate head pointing outwards toward watery extracellular and cytosol sides."},
            {"part": "Hydrophobic Fatty Acid Tail", "desc": "Non-polar hydrocarbon tails shielded inwards away from water."},
            {"part": "Intrinsic / Transmembrane Protein", "desc": "Spans entire bilayer, functioning as selective transport channel/carrier."},
            {"part": "Extrinsic / Peripheral Protein", "desc": "Loosely attached to outer or inner surface for signalling and attachment."}
        ],
        "mustDraw": [
            "Two distinct layers of lipid molecules with round heads facing outside and two wavy tails facing inside",
            "Channel proteins spanning the entire thickness"
        ],
        "examinerTip": "Draw the bilayer symmetry carefully: Heads point outwards; tails face inwards towards each other.",
        "svgType": "cell_membrane"
    },
    {
        "id": "diag_05",
        "figCode": "Fig. 2.10",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Cell Architectures: Bacterial, Plant, and Animal Cells",
        "sub": "bio",
        "ncertPage": 7,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=7",
        "labels": [
            {"part": "Bacterial Cell (Prokaryote)", "desc": "Peptidoglycan wall, capsule, circular naked DNA (nucleoid), 70S ribosomes, flagellum; no nuclear membrane."},
            {"part": "Plant Cell (Eukaryote)", "desc": "Cellulose cell wall, large central permanent vacuole, chloroplasts, peripheral nucleus."},
            {"part": "Animal Cell (Eukaryote)", "desc": "No cell wall, no chloroplasts, centrioles/centrosome present, small temporary vacuoles, centrally placed nucleus."}
        ],
        "mustDraw": [
            "Plant cell: Double boundary (Cell wall + Cell membrane), large central vacuole pushing nucleus to periphery",
            "Animal cell: Single outer boundary (Plasma membrane only), central nucleus, centrioles",
            "Bacterial cell: Nucleoid without envelope, flagella"
        ],
        "examinerTip": "Top scoring differentiator: Plant cells have a rigid wall, large central vacuole, and plastids; animal cells have centrioles and only small temporary vacuoles.",
        "svgType": "cells_comparison"
    },
    {
        "id": "diag_06",
        "figCode": "Fig. 2.11",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Structure of a Nucleus",
        "sub": "bio",
        "ncertPage": 9,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=9",
        "labels": [
            {"part": "Nuclear Envelope", "desc": "Double-layered membrane isolating nucleoplasm from cytoplasm."},
            {"part": "Nuclear Pore", "desc": "Openings regulating macromolecular transport (RNA, ribosomal subunits, proteins)."},
            {"part": "Nucleolus", "desc": "Dense non-membrane spherical body responsible for ribosome synthesis."},
            {"part": "Chromatin Material", "desc": "Entangled network of nucleoprotein fibres (DNA + histone proteins) that condenses into chromosomes during division."}
        ],
        "mustDraw": [
            "Double boundary with visible breaks (nuclear pores)",
            "Dense round nucleolus inside",
            "Intertwined thread-like chromatin network"
        ],
        "examinerTip": "Always leave gaps in the double nuclear membrane to represent nuclear pores. Label chromatin and nucleolus clearly.",
        "svgType": "nucleus"
    },
    {
        "id": "diag_07",
        "figCode": "Fig. 2.12",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "From Cell to DNA Hierarchy",
        "sub": "bio",
        "ncertPage": 9,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=9",
        "labels": [
            {"part": "Metaphase Chromosome", "desc": "Highly condensed genetic package with two sister chromatids joined at the centromere."},
            {"part": "Chromatin Fibre", "desc": "Nucleosome beads-on-a-string folding into higher order loops."},
            {"part": "Histone Core Octamer", "desc": "Positively charged protein spool around which negatively charged DNA is coiled."},
            {"part": "DNA Double Helix", "desc": "Antiparallel double helix carrying base pairs and genetic instructions."}
        ],
        "mustDraw": [
            "X-shaped chromosome showing centromere and two chromatids",
            "Unwinding chromatin strand revealing histone beads and double-helix DNA"
        ],
        "examinerTip": "Show the progressive uncoiling: Chromosome → Chromatin → Histones → DNA Double Helix.",
        "svgType": "chromosome_dna"
    },
    {
        "id": "diag_08",
        "figCode": "Fig. 2.13",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Endoplasmic Reticulum & Golgi Apparatus Secretory Pathway",
        "sub": "bio",
        "ncertPage": 10,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=10",
        "labels": [
            {"part": "Rough ER (RER)", "desc": "Sheets studded with ribosomes that synthesize polypeptide chains."},
            {"part": "Transport Vesicle", "desc": "Membrane-bound spheres budding from ER transporting newly formed proteins."},
            {"part": "Cis-Face of Golgi", "desc": "Receiving side facing the nucleus and ER."},
            {"part": "Golgi Cisternae", "desc": "Stack of parallel curved sacs that modify, glycosylate, and package proteins."},
            {"part": "Trans-Face & Secretory Vesicle", "desc": "Shipping side budding off mature secretory vesicles or lysosomes."}
        ],
        "mustDraw": [
            "RER continuous with nuclear envelope studded with dots (ribosomes)",
            "Convex cis-face receiving vesicles and concave trans-face dispatching vesicles"
        ],
        "examinerTip": "Highlight the functional polarity: Nuclear Envelope → RER → Transport Vesicle → Cis-Golgi → Trans-Golgi → Secretory Vesicle / Lysosome.",
        "svgType": "er_golgi"
    },
    {
        "id": "diag_09",
        "figCode": "Fig. 2.14",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Structure of a Mitochondrion",
        "sub": "bio",
        "ncertPage": 11,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=11",
        "labels": [
            {"part": "Outer Membrane", "desc": "Smooth, porous outer boundary containing porin transport channels."},
            {"part": "Inner Membrane & Cristae", "desc": "Selectively permeable inner membrane thrown into deep finger-like folds (cristae) providing huge surface area for ATP generation."},
            {"part": "Matrix", "desc": "Gel-like ground substance containing Krebs cycle enzymes, 70S ribosomes, and circular DNA."},
            {"part": "Mitochondrial DNA & Ribosomes", "desc": "Enables mitochondria to make their own proteins (semi-autonomous organelle)."}
        ],
        "mustDraw": [
            "Smooth outer oval boundary",
            "Inner membrane deeply infolded into finger-like projections (cristae)",
            "Dots in matrix representing ribosomes and circular DNA loop"
        ],
        "examinerTip": "Cristae must be clearly shown as continuous inward folds of the inner membrane, NOT disconnected floating loops!",
        "svgType": "mitochondrion"
    },
    {
        "id": "diag_10",
        "figCode": "Fig. 2.15",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Structure of a Chloroplast",
        "sub": "bio",
        "ncertPage": 11,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=11",
        "labels": [
            {"part": "Outer & Inner Membrane", "desc": "Smooth double membrane envelope with intermembrane space."},
            {"part": "Stroma", "desc": "Fluid matrix containing enzymes for the light-independent dark reaction (Calvin cycle), DNA, and ribosomes."},
            {"part": "Thylakoid", "desc": "Flattened disc-like membranous sac embedded with chlorophyll molecules."},
            {"part": "Granum (pl. Grana)", "desc": "Stack of coin-like thylakoids where the light-dependent reaction occurs."},
            {"part": "Stroma Lamella", "desc": "Tubular membrane bridges interconnecting separate grana stacks."}
        ],
        "mustDraw": [
            "Double outer membrane",
            "Stacks of coin-like discs (grana)",
            "Connecting bridge tubules (stroma lamellae)",
            "Fluid matrix (stroma)"
        ],
        "examinerTip": "Distinguish between Granum (the whole stack) and Thylakoid (a single coin disc). Stroma is the fluid surrounding the stacks.",
        "svgType": "chloroplast"
    },
    {
        "id": "diag_11",
        "figCode": "Fig. 2.18",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Mitosis: Equational Division (Two Identical Daughter Cells)",
        "sub": "bio",
        "ncertPage": 14,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=14",
        "labels": [
            {"part": "Prophase", "desc": "Chromatin condenses into visible chromosomes; nuclear membrane and nucleolus disintegrate; spindle forms."},
            {"part": "Metaphase", "desc": "Chromosomes line up in a single file along the equatorial plate (metaphase plate) attached to spindle fibres."},
            {"part": "Anaphase", "desc": "Centromeres split; sister chromatids separate and are pulled to opposite spindle poles."},
            {"part": "Telophase & Cytokinesis", "desc": "Nuclear envelopes reform around two daughter nuclei; cytoplasm divides yielding two 2n cells."}
        ],
        "mustDraw": [
            "Single equatorial plane alignment in Metaphase",
            "V-shaped sister chromatids pulling apart in Anaphase",
            "Two identical daughter cells with equal chromosome numbers (2n → 2n)"
        ],
        "examinerTip": "Key concept: Mitosis is equational. The chromosome count in daughter cells remains identical to the parent cell.",
        "svgType": "mitosis"
    },
    {
        "id": "diag_12",
        "figCode": "Fig. 2.19",
        "chapter": "Ch 2",
        "chTitle": "Cell — The Building Block of Life",
        "title": "Meiosis: Two-Step Reduction Division (Four Gametes)",
        "sub": "bio",
        "ncertPage": 15,
        "pdfPath": "downloads/class-09/science/exploration/iesc102--cell-the-building-block-of-life.pdf#page=15",
        "labels": [
            {"part": "Parent Cell (2n)", "desc": "Diploid reproductive cell containing maternal and paternal chromosome pairs."},
            {"part": "Meiosis I (Reduction)", "desc": "Homologous chromosome pairing (synapsis) and crossing over, followed by separation of homologues (2n → n)."},
            {"part": "Meiosis II (Equational)", "desc": "Separation of sister chromatids without further DNA replication."},
            {"part": "Four Gametes (n)", "desc": "Four haploid daughter cells, each with half the chromosome number and novel genetic combinations."}
        ],
        "mustDraw": [
            "Two consecutive division cycles: Meiosis I (splits pairs) and Meiosis II (splits chromatids)",
            "Result: 4 daughter cells with half the original chromosome count (haploid n)"
        ],
        "examinerTip": "In Meiosis I homologous pairs separate (reductional); in Meiosis II sister chromatids separate (equational). Total product is 4 haploid gametes.",
        "svgType": "meiosis"
    },

    # -------------------------------------------------------------------------
    # REPRODUCTION (CHAPTER 11)
    # -------------------------------------------------------------------------
    {
        "id": "diag_13",
        "figCode": "Fig. 11.3",
        "chapter": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "title": "Steps of Vegetative Propagation by Grafting",
        "sub": "bio",
        "ncertPage": 3,
        "pdfPath": "downloads/class-09/science/exploration/iesc111--reproduction-how-life-continues.pdf#page=3",
        "labels": [
            {"part": "Stock (Rootstock)", "desc": "The lower rooted plant portion providing sturdy root system and water absorption."},
            {"part": "Scion", "desc": "The upper detached shoot stem with healthy buds bearing desirable fruit/flower traits."},
            {"part": "Complementary Oblique Cuts", "desc": "Slanted cuts made to fit stock and scion closely."},
            {"part": "Cambial Layer Alignment", "desc": "Crucial alignment of vascular cambium tissues so xylem and phloem can knit together."},
            {"part": "Grafting Wax & Binding Tape", "desc": "Tied tightly to prevent dehydration and fungal pathogen entry until healed."}
        ],
        "mustDraw": [
            "Distinct labels for Stock (bottom with roots) and Scion (top with shoot/buds)",
            "Slanted interlocking joint wrapped with protective tape"
        ],
        "examinerTip": "Crucial requirement: The cambium of scion and stock must touch for vascular continuity to establish.",
        "svgType": "grafting"
    },
    {
        "id": "diag_14",
        "figCode": "Fig. 11.10",
        "chapter": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "title": "Longitudinal Section (LS) of a Flower",
        "sub": "bio",
        "ncertPage": 7,
        "pdfPath": "downloads/class-09/science/exploration/iesc111--reproduction-how-life-continues.pdf#page=7",
        "labels": [
            {"part": "Pedicel & Receptacle", "desc": "Floral stalk and swollen base supporting all four whorls."},
            {"part": "Sepals (Calyx)", "desc": "Green outermost leaf-like whorl protecting floral bud."},
            {"part": "Petals (Corolla)", "desc": "Brightly colored fragrant whorl attracting insect pollinators."},
            {"part": "Stamen (Male Part)", "desc": "Consists of two-lobed pollen-producing Anther and slender stalk Filament."},
            {"part": "Carpel / Pistil (Female Part)", "desc": "Centrally placed female organ consisting of Stigma, Style, and basal Ovary."}
        ],
        "mustDraw": [
            "All four concentric whorls clearly delineated from outside to center: Calyx → Corolla → Androecium → Gynoecium",
            "Swollen basal ovary showing internal ovules"
        ],
        "examinerTip": "Most common question in 3-mark exams! Must label both male unit (Stamen: Anther + Filament) and female unit (Carpel: Stigma + Style + Ovary).",
        "svgType": "flower_ls"
    },
    {
        "id": "diag_15",
        "figCode": "Fig. 11.11",
        "chapter": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "title": "Structure of a Carpel / Pistil",
        "sub": "bio",
        "ncertPage": 8,
        "pdfPath": "downloads/class-09/science/exploration/iesc111--reproduction-how-life-continues.pdf#page=8",
        "labels": [
            {"part": "Stigma", "desc": "Terminal sticky or papillate landing surface capturing and retaining pollen grains."},
            {"part": "Style", "desc": "Slender connecting neck through which the pollen tube grows downward."},
            {"part": "Ovary", "desc": "Swollen basal chamber housing and protecting ovules; ripens into the fruit."},
            {"part": "Ovule", "desc": "Megasporangium containing female gamete (egg cell); ripens into a seed."}
        ],
        "mustDraw": [
            "Three vertical sections: Stigma (top), Style (middle conduit), Ovary (swollen base)",
            "At least one ovule inside the ovary with embryo sac"
        ],
        "examinerTip": "Remember the developmental fate: Ovary develops into the Fruit; Ovule develops into the Seed after fertilisation.",
        "svgType": "pistil"
    },
    {
        "id": "diag_16",
        "figCode": "Fig. 11.14",
        "chapter": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "title": "Germination of Pollen on Stigma",
        "sub": "bio",
        "ncertPage": 9,
        "pdfPath": "downloads/class-09/science/exploration/iesc111--reproduction-how-life-continues.pdf#page=9",
        "labels": [
            {"part": "Pollen Grain", "desc": "Carries male gametophyte with protective exine coat."},
            {"part": "Stigmatic Secretion", "desc": "Sugary exudate inducing hydration and germination of compatible pollen."},
            {"part": "Pollen Tube", "desc": "Tubular outgrowth penetrating stigma and style tissues toward ovary."},
            {"part": "Male Germ Cells", "desc": "Two sperm nuclei carried inside tip of pollen tube."},
            {"part": "Female Gamete (Egg Cell)", "desc": "Located inside ovule's embryo sac for syngamy/fertilisation."}
        ],
        "mustDraw": [
            "Pollen grain seated on stigma surface",
            "Pollen tube growing through the entire length of style entering the ovary micropyle",
            "Two male nuclei inside the growing tube"
        ],
        "examinerTip": "Crucial drawing detail: Show the pollen tube entering the ovule specifically at the micropylar opening.",
        "svgType": "pollen_germination"
    },
    {
        "id": "diag_17",
        "figCode": "Fig. 11.19",
        "chapter": "Ch 11",
        "chTitle": "Reproduction: How Life Continues",
        "title": "Human Female Reproductive System",
        "sub": "bio",
        "ncertPage": 12,
        "pdfPath": "downloads/class-09/science/exploration/iesc111--reproduction-how-life-continues.pdf#page=12",
        "labels": [
            {"part": "Ovary (Pair)", "desc": "Primary female sex organs producing ova (egg cells) and female hormones (estrogen, progesterone)."},
            {"part": "Fallopian Tube / Oviduct", "desc": "Ciliated muscular tube with funnel-shaped fimbriae receiving ovum; site of fertilisation."},
            {"part": "Uterus (Womb)", "desc": "Inverted pear-shaped muscular organ where embryo implants and develops."},
            {"part": "Cervix", "desc": "Narrow muscular neck of uterus opening into the vagina."},
            {"part": "Vagina", "desc": "Muscular canal receiving sperm and serving as the birth canal during parturition."}
        ],
        "mustDraw": [
            "Bilateral symmetry showing both left and right ovaries and fallopian tubes",
            "Central inverted pear-shaped uterus with thick muscular wall",
            "Narrow cervix leading to vagina canal"
        ],
        "examinerTip": "High-frequency 5-mark question! Always specify that fertilisation takes place in the fallopian tube (oviduct), while implantation takes place in the uterus lining.",
        "svgType": "female_reproductive"
    }
]


CHEMISTRY_TABLE_9_1_DATA = {
    "title": "Table 9.1: Names, Formulae, and Valencies of Common Ions",
    "ncertChapter": "Chapter 9: Atomic Foundations of Matter",
    "ncertPages": "Pages 174–175",
    "rules": [
        "In naming simple ionic compounds, the cation (metal) is written first, followed by the anion (non-metal).",
        "Names of simple monoatomic anions end with the suffix '-ide' (e.g. Oxide, Chloride, Sulfide, Fluoride).",
        "Polyatomic ions are groups of atoms behaving as a single unit with a net charge; their names often end in '-ite' or '-ate' (e.g. Nitrate, Sulfate, Carbonate).",
        "When criss-crossing valencies, if a polyatomic ion has a subscript greater than 1, enclose the ion formula in parentheses before adding the subscript (e.g. Ca(OH)₂, Al₂(SO₄)₃, (NH₄)₂CO₃).",
        "If subscripts can be simplified by a common divisor, divide to give the simplest whole-number ratio (e.g. Ca₂O₂ simplifies to CaO)."
    ],
    "table_a_monoatomic": [
        # Cations
        {"name": "Sodium", "symbol": "Na", "formula": "Na⁺", "charge": "+1", "valency": 1, "type": "cation", "class": "monovalent"},
        {"name": "Lithium", "symbol": "Li", "formula": "Li⁺", "charge": "+1", "valency": 1, "type": "cation", "class": "monovalent"},
        {"name": "Potassium", "symbol": "K", "formula": "K⁺", "charge": "+1", "valency": 1, "type": "cation", "class": "monovalent"},
        {"name": "Silver", "symbol": "Ag", "formula": "Ag⁺", "charge": "+1", "valency": 1, "type": "cation", "class": "monovalent"},
        {"name": "Copper (Cuprous)", "symbol": "Cu", "formula": "Cu⁺", "charge": "+1", "valency": 1, "type": "cation", "class": "monovalent", "note": "Copper(I) lower valency"},
        {"name": "Magnesium", "symbol": "Mg", "formula": "Mg²⁺", "charge": "+2", "valency": 2, "type": "cation", "class": "divalent"},
        {"name": "Calcium", "symbol": "Ca", "formula": "Ca²⁺", "charge": "+2", "valency": 2, "type": "cation", "class": "divalent"},
        {"name": "Zinc", "symbol": "Zn", "formula": "Zn²⁺", "charge": "+2", "valency": 2, "type": "cation", "class": "divalent"},
        {"name": "Iron (Ferrous)", "symbol": "Fe", "formula": "Fe²⁺", "charge": "+2", "valency": 2, "type": "cation", "class": "divalent", "note": "Iron(II) lower valency (-ous)"},
        {"name": "Barium", "symbol": "Ba", "formula": "Ba²⁺", "charge": "+2", "valency": 2, "type": "cation", "class": "divalent"},
        {"name": "Copper (Cupric)", "symbol": "Cu", "formula": "Cu²⁺", "charge": "+2", "valency": 2, "type": "cation", "class": "divalent", "note": "Copper(II) higher valency (-ic)"},
        {"name": "Aluminium", "symbol": "Al", "formula": "Al³⁺", "charge": "+3", "valency": 3, "type": "cation", "class": "trivalent"},
        {"name": "Iron (Ferric)", "symbol": "Fe", "formula": "Fe³⁺", "charge": "+3", "valency": 3, "type": "cation", "class": "trivalent", "note": "Iron(III) higher valency (-ic)"},
        # Anions
        {"name": "Fluoride", "symbol": "F", "formula": "F⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent"},
        {"name": "Chloride", "symbol": "Cl", "formula": "Cl⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent"},
        {"name": "Bromide", "symbol": "Br", "formula": "Br⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent"},
        {"name": "Iodide", "symbol": "I", "formula": "I⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent"},
        {"name": "Oxide", "symbol": "O", "formula": "O²⁻", "charge": "-2", "valency": 2, "type": "anion", "class": "divalent"},
        {"name": "Sulfide", "symbol": "S", "formula": "S²⁻", "charge": "-2", "valency": 2, "type": "anion", "class": "divalent"},
        {"name": "Nitride", "symbol": "N", "formula": "N³⁻", "charge": "-3", "valency": 3, "type": "anion", "class": "trivalent", "note": "Companion monoatomic anion"}
    ],
    "table_b_polyatomic": [
        {"name": "Ammonium", "symbol": "NH₄", "formula": "NH₄⁺", "charge": "+1", "valency": 1, "type": "cation", "class": "monovalent", "poly": True},
        {"name": "Hydroxide", "symbol": "OH", "formula": "OH⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent", "poly": True},
        {"name": "Nitrate", "symbol": "NO₃", "formula": "NO₃⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent", "poly": True},
        {"name": "Hydrogencarbonate (Bicarbonate)", "symbol": "HCO₃", "formula": "HCO₃⁻", "charge": "-1", "valency": 1, "type": "anion", "class": "monovalent", "poly": True},
        {"name": "Carbonate", "symbol": "CO₃", "formula": "CO₃²⁻", "charge": "-2", "valency": 2, "type": "anion", "class": "divalent", "poly": True},
        {"name": "Sulfate", "symbol": "SO₄", "formula": "SO₄²⁻", "charge": "-2", "valency": 2, "type": "anion", "class": "divalent", "poly": True},
        {"name": "Phosphate", "symbol": "PO₄", "formula": "PO₄³⁻", "charge": "-3", "valency": 3, "type": "anion", "class": "trivalent", "poly": True}
    ],
    "quiz_compounds": [
        {"name": "Sodium chloride", "cation": "Na", "cVal": 1, "anion": "Cl", "aVal": 1, "formula": "NaCl", "isPoly": False},
        {"name": "Magnesium chloride", "cation": "Mg", "cVal": 2, "anion": "Cl", "aVal": 1, "formula": "MgCl₂", "isPoly": False},
        {"name": "Calcium oxide", "cation": "Ca", "cVal": 2, "anion": "O", "aVal": 2, "formula": "CaO", "isPoly": False, "rule": "2:2 ratio simplifies to 1:1"},
        {"name": "Aluminium oxide", "cation": "Al", "cVal": 3, "anion": "O", "aVal": 2, "formula": "Al₂O₃", "isPoly": False},
        {"name": "Calcium hydroxide", "cation": "Ca", "cVal": 2, "anion": "OH", "aVal": 1, "formula": "Ca(OH)₂", "isPoly": True, "rule": "Polyatomic OH requires brackets for subscript 2"},
        {"name": "Sodium carbonate", "cation": "Na", "cVal": 1, "anion": "CO₃", "aVal": 2, "formula": "Na₂CO₃", "isPoly": True, "rule": "Subscript 1 for CO₃ needs no brackets"},
        {"name": "Ammonium sulfate", "cation": "NH₄", "cVal": 1, "anion": "SO₄", "aVal": 2, "formula": "(NH₄)₂SO₄", "isPoly": True, "rule": "NH₄ requires brackets for subscript 2"},
        {"name": "Aluminium sulfate", "cation": "Al", "cVal": 3, "anion": "SO₄", "aVal": 2, "formula": "Al₂(SO₄)₃", "isPoly": True, "rule": "SO₄ requires brackets for subscript 3"},
        {"name": "Ferric chloride (Iron III chloride)", "cation": "Fe", "cVal": 3, "anion": "Cl", "aVal": 1, "formula": "FeCl₃", "isPoly": False},
        {"name": "Ferrous sulfate (Iron II sulfate)", "cation": "Fe", "cVal": 2, "anion": "SO₄", "aVal": 2, "formula": "FeSO₄", "isPoly": True, "rule": "2:2 ratio simplifies to 1:1"},
        {"name": "Copper (II) nitrate", "cation": "Cu", "cVal": 2, "anion": "NO₃", "aVal": 1, "formula": "Cu(NO₃)₂", "isPoly": True, "rule": "NO₃ requires brackets for subscript 2"},
        {"name": "Sodium hydrogencarbonate", "cation": "Na", "cVal": 1, "anion": "HCO₃", "aVal": 1, "formula": "NaHCO₃", "isPoly": True},
        {"name": "Zinc carbonate", "cation": "Zn", "cVal": 2, "anion": "CO₃", "aVal": 2, "formula": "ZnCO₃", "isPoly": True, "rule": "2:2 ratio simplifies to 1:1"},
        {"name": "Silver bromide", "cation": "Ag", "cVal": 1, "anion": "Br", "aVal": 1, "formula": "AgBr", "isPoly": False},
        {"name": "Potassium nitrate", "cation": "K", "cVal": 1, "anion": "NO₃", "aVal": 1, "formula": "KNO₃", "isPoly": True}
    ]
}
