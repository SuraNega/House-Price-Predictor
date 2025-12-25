# 📝 Complete Input Fields Guide - House Price Predictor

This guide explains **every input field** in the web application so you know exactly what data to enter.

---

## 🏗️ Section 1: General Information

### 1. **Overall Quality (1-10)**
**What it measures:** The overall material and finish quality of the house

**Scale:**
- **10** = Very Excellent (luxury materials, top-tier finishes)
- **9** = Excellent (high-quality materials throughout)
- **8** = Very Good (above average quality)
- **7** = Good (better than average)
- **6** = Above Average
- **5** = Average (typical quality)
- **4** = Below Average
- **3** = Fair (lower quality materials)
- **2** = Poor
- **1** = Very Poor (minimal quality)

**Examples:**
- Luxury home with marble countertops, hardwood floors, custom cabinets = **9-10**
- Well-built suburban home with good materials = **6-7**
- Basic starter home with standard materials = **4-5**
- Fixer-upper needing major work = **1-3**

---

### 2. **Overall Condition (1-10)**
**What it measures:** The current physical condition and maintenance level

**Scale:**
- **10** = Very Excellent (like new, pristine)
- **9** = Excellent (very well maintained)
- **8** = Very Good
- **7** = Good
- **6** = Above Average
- **5** = Average (normal wear and tear)
- **4** = Below Average (needs some repairs)
- **3** = Fair (needs significant repairs)
- **2** = Poor (major issues)
- **1** = Very Poor (uninhabitable)

**Examples:**
- Recently renovated, everything works perfectly = **9-10**
- Well-maintained, minor cosmetic issues = **6-7**
- Needs new roof, some plumbing issues = **3-4**
- Severe structural problems = **1-2**

**Note:** Quality ≠ Condition!
- High quality, poor condition: Luxury home that's been neglected (Quality 9, Condition 3)
- Low quality, good condition: Basic home that's well-maintained (Quality 4, Condition 8)

---

### 3. **Year Built**
**What it measures:** The year the house was originally constructed

**Range:** 1872 - 2024

**Examples:**
- Historic Victorian home = **1890**
- Post-war suburban home = **1955**
- Modern construction = **2010**
- Brand new = **2024**

**Impact on Price:**
- Newer homes (2000+) typically command premium
- Mid-century homes (1950-1980) moderate pricing
- Historic homes (pre-1900) varies (could be valuable if preserved)

**Validation:** Must be ≤ Year Remodeled (you can't remodel before building!)

---

### 4. **Year Remodeled**
**What it measures:** The year of the last major renovation or remodeling

**Range:** 1872 - 2024

**Important:**
- If **never remodeled**: Enter the same year as Year Built
- If **remodeled**: Enter the renovation year

**Examples:**
- Built 1980, never remodeled = Year Built: **1980**, Year Remodeled: **1980**
- Built 1980, remodeled 2015 = Year Built: **1980**, Year Remodeled: **2015**
- Built 2020, brand new = Year Built: **2020**, Year Remodeled: **2020**

**What counts as remodeling:**
- ✅ Kitchen renovation
- ✅ Bathroom updates
- ✅ New roof
- ✅ Major additions
- ❌ Painting walls (too minor)
- ❌ New appliances (not structural)

**Validation:** Must be ≥ Year Built

---

## 📐 Section 2: Area & Space

### 5. **Above Ground Living Area (sq ft)**
**What it measures:** Total living space above ground level (excluding basement)

**Range:** 300 - 6,000 sq ft

**Includes:**
- ✅ First floor living space
- ✅ Second floor (if applicable)
- ✅ Finished attic space
- ❌ Basement (counted separately)
- ❌ Garage
- ❌ Unfinished areas

**Examples:**
- Small apartment/condo = **600-900 sq ft**
- Starter home = **1,000-1,500 sq ft**
- Average family home = **1,500-2,500 sq ft**
- Large home = **2,500-4,000 sq ft**
- Mansion = **4,000+ sq ft**

**Tip:** This is usually the number advertised in real estate listings!

---

### 6. **Total Basement Area (sq ft)**
**What it measures:** Total square footage of basement space

**Range:** 0 - 3,000 sq ft

**Includes:**
- ✅ Finished basement
- ✅ Unfinished basement
- ✅ Partially finished basement

**Examples:**
- No basement = **0**
- Partial basement = **400-600 sq ft**
- Full basement (matches first floor) = **800-1,200 sq ft**
- Large basement = **1,500+ sq ft**

**Note:** Doesn't matter if finished or unfinished - this is total basement area

---

### 7. **First Floor Area (sq ft)**
**What it measures:** Square footage of the first/ground floor

**Range:** 300 - 5,000 sq ft

**Includes:**
- ✅ Living room
- ✅ Kitchen
- ✅ Dining room
- ✅ First floor bedrooms
- ✅ First floor bathrooms
- ❌ Garage
- ❌ Basement

**Examples:**
- Small ranch home = **800-1,000 sq ft**
- Average home = **1,000-1,500 sq ft**
- Large home = **1,500-2,500 sq ft**

---

### 8. **Second Floor Area (sq ft)**
**What it measures:** Square footage of the second floor

**Range:** 0 - 2,000 sq ft

**Includes:**
- ✅ Upstairs bedrooms
- ✅ Upstairs bathrooms
- ✅ Loft areas
- ✅ Finished attic

**Examples:**
- Single-story home (ranch, bungalow) = **0**
- Two-story with 3 bedrooms upstairs = **800-1,200 sq ft**
- Large two-story = **1,500+ sq ft**

**Note:** If you have a 1-story home, enter **0**

---

### 9. **Lot Area (sq ft)**
**What it measures:** Total land/property size

**Range:** 1,300 - 100,000 sq ft

**Includes:**
- ✅ House footprint
- ✅ Front yard
- ✅ Backyard
- ✅ Side yards
- ✅ Driveway

**Examples:**
- Small urban lot = **2,000-5,000 sq ft**
- Typical suburban lot = **6,000-10,000 sq ft**
- Large suburban lot = **10,000-20,000 sq ft**
- Acreage (1 acre = 43,560 sq ft) = **43,560+ sq ft**

**Conversion:**
- 1/4 acre = **10,890 sq ft**
- 1/2 acre = **21,780 sq ft**
- 1 acre = **43,560 sq ft**

---

## 🛏️ Section 3: Rooms & Features

### 10. **Bedrooms Above Ground**
**What it measures:** Number of bedrooms NOT in the basement

**Range:** 0 - 10

**Counts as bedroom:**
- ✅ Has a closet
- ✅ Has a window
- ✅ Can fit a bed
- ❌ Office (unless used as bedroom)
- ❌ Den
- ❌ Basement bedrooms (counted separately in dataset)

**Examples:**
- Studio apartment = **0**
- Small home = **2**
- Average family home = **3-4**
- Large home = **5+**

---

### 11. **Full Bathrooms**
**What it measures:** Bathrooms with toilet, sink, AND bathtub/shower

**Range:** 0 - 5

**Full bathroom includes:**
- ✅ Toilet
- ✅ Sink
- ✅ Bathtub OR shower (or both)

**Examples:**
- Small home = **1**
- Average home = **2**
- Large home = **3-4**

**Note:** This is ABOVE GROUND only (basement bathrooms counted separately)

---

### 12. **Half Bathrooms**
**What it measures:** Bathrooms with toilet and sink ONLY (no tub/shower)

**Range:** 0 - 3

**Half bathroom (powder room) includes:**
- ✅ Toilet
- ✅ Sink
- ❌ NO bathtub
- ❌ NO shower

**Examples:**
- No powder room = **0**
- One guest bathroom downstairs = **1**
- Multiple powder rooms = **2+**

**Common names:** Powder room, guest bath, half bath

---

### 13. **Basement Full Bathrooms**
**What it measures:** Full bathrooms located IN THE BASEMENT

**Range:** 0 - 3

**Same rules as regular full bathroom, but in basement:**
- ✅ Toilet
- ✅ Sink
- ✅ Bathtub/shower

**Examples:**
- No basement or unfinished basement = **0**
- Finished basement with bathroom = **1**

---

### 14. **Basement Half Bathrooms**
**What it measures:** Half bathrooms (toilet + sink only) in basement

**Range:** 0 - 2

**Examples:**
- No basement bathroom = **0**
- Basement powder room = **1**

---

### 15. **Garage Car Capacity**
**What it measures:** How many cars can fit in the garage

**Range:** 0 - 5

**Examples:**
- No garage (street parking only) = **0**
- Single car garage = **1**
- Standard two-car garage = **2**
- Three-car garage (luxury) = **3**
- Oversized garage = **4-5**

**Note:** This is capacity, not current usage!

---

### 16. **Garage Area (sq ft)**
**What it measures:** Total square footage of garage space

**Range:** 0 - 1,500 sq ft

**Examples:**
- No garage = **0**
- Single car garage = **200-300 sq ft**
- Two-car garage = **400-600 sq ft**
- Three-car garage = **600-900 sq ft**
- Oversized/workshop garage = **1,000+ sq ft**

**Tip:** Typical single car = ~250 sq ft, so 2-car ≈ 500 sq ft

---

## 🔧 Section 4: Additional Features (Optional)

These fields are in the expandable "Additional Features" section. They're optional but improve prediction accuracy!

### 17. **Zoning Classification**
**What it measures:** The legal zoning designation of the property

**Options:**
- **RL** = Residential Low Density (most common)
  - Single-family homes
  - Larger lots
  - Suburban areas

- **RM** = Residential Medium Density
  - Townhouses
  - Small apartment buildings
  - Denser neighborhoods

- **FV** = Floating Village Residential
  - Specific planned developments
  - Mixed-use residential

- **RH** = Residential High Density
  - Apartment complexes
  - High-rise buildings
  - Urban areas

- **C (all)** = Commercial
  - Mixed commercial/residential
  - Business districts

**Most Common:** **RL** (Residential Low Density) - use this if unsure!

**Impact:** RL typically commands higher prices than RM or RH

---

### 18. **Neighborhood**
**What it measures:** The specific neighborhood/subdivision where the house is located

**Available Options:**
- **CollgCr** = College Creek
- **Veenker** = Veenker
- **Crawfor** = Crawford
- **NoRidge** = Northridge
- **Mitchel** = Mitchell
- **Somerst** = Somerset
- **NWAmes** = Northwest Ames
- **OldTown** = Old Town
- **BrkSide** = Brookside
- **Sawyer** = Sawyer
- **NridgHt** = Northridge Heights (Premium!)
- **NAmes** = North Ames
- **SawyerW** = Sawyer West
- **IDOTRR** = Iowa DOT and Rail Road
- **MeadowV** = Meadow Village
- **Edwards** = Edwards
- **Timber** = Timberland
- **Gilbert** = Gilbert
- **StoneBr** = Stone Brook (Premium!)
- **ClearCr** = Clear Creek
- **NPkVill** = Northpark Villa
- **Blmngtn** = Bloomington Heights
- **BrDale** = Briardale
- **SWISU** = South & West of Iowa State University
- **Blueste** = Bluestem

**Premium Neighborhoods (Higher Prices):**
- **NridgHt** (Northridge Heights)
- **StoneBr** (Stone Brook)
- **NoRidge** (Northridge)

**Budget-Friendly Neighborhoods:**
- **MeadowV** (Meadow Village)
- **BrDale** (Briardale)
- **IDOTRR** (Iowa DOT area)

**Default:** Use **CollgCr** if you don't know the specific neighborhood

**Impact:** Can change price by 20-50%! Premium neighborhoods command much higher prices.

---

### 19. **House Style**
**What it measures:** The architectural style/configuration of the house

**Options:**

- **1Story** = One-story/Ranch
  - All living space on one level
  - No stairs
  - Popular for accessibility

- **2Story** = Two-story
  - Living areas on first floor
  - Bedrooms typically on second floor
  - Most common style

- **1.5Fin** = One and a half story, finished
  - Main floor plus finished attic/loft
  - Cape Cod style
  - Sloped ceilings upstairs

- **1.5Unf** = One and a half story, unfinished
  - Main floor plus unfinished attic space
  - Potential for expansion

- **SFoyer** = Split Foyer
  - Entry between two levels
  - Raised ranch style
  - Stairs up and down from entry

- **SLvl** = Split Level
  - Multiple levels offset by half floors
  - 1970s popular style

- **2.5Unf** = Two and a half story, unfinished
  - Two full floors plus unfinished attic

- **2.5Fin** = Two and a half story, finished
  - Two full floors plus finished third level

**Most Common:** **2Story** or **1Story**

**Impact:** 2-story homes often have better price per sq ft than 1-story

---

### 20. **Central Air Conditioning**
**What it measures:** Does the house have central air conditioning?

**Options:**
- **Y** = Yes (has central AC)
- **N** = No (no central AC, or only window units)

**What counts as "Yes":**
- ✅ Whole-house central AC system
- ✅ HVAC system with cooling
- ❌ Window AC units (this is "No")
- ❌ Portable AC units (this is "No")

**Impact:** Central AC adds significant value, especially in hot climates

**Default:** **Y** (most modern homes have it)

---

### 21. **Kitchen Quality**
**What it measures:** The quality of kitchen materials and appliances

**Options:**

- **Ex** = Excellent
  - High-end appliances (Sub-Zero, Wolf, etc.)
  - Granite/marble countertops
  - Custom cabinets
  - Professional-grade fixtures

- **Gd** = Good
  - Quality appliances (KitchenAid, Bosch)
  - Granite or quartz countertops
  - Good quality cabinets
  - Above average finishes

- **TA** = Typical/Average
  - Standard appliances (Whirlpool, GE)
  - Laminate or basic granite counters
  - Stock cabinets
  - Average finishes

- **Fa** = Fair
  - Basic/older appliances
  - Laminate countertops
  - Dated cabinets
  - Below average quality

**Examples:**
- Luxury kitchen with high-end everything = **Ex**
- Nice updated kitchen = **Gd**
- Standard builder-grade kitchen = **TA**
- Outdated 1980s kitchen = **Fa**

**Default:** **TA** (Typical/Average) for most homes

**Impact:** Kitchen quality significantly affects home value!

---

### 22. **Number of Fireplaces**
**What it measures:** Total count of functional fireplaces

**Range:** 0 - 4

**Counts as fireplace:**
- ✅ Wood-burning fireplace
- ✅ Gas fireplace
- ✅ Electric fireplace (if built-in)
- ❌ Decorative non-functional fireplace
- ❌ Portable space heater

**Examples:**
- No fireplace = **0**
- Living room fireplace = **1**
- Living room + master bedroom = **2**
- Multiple rooms with fireplaces = **3-4**

**Impact:** Fireplaces add value, especially in colder climates

---

## 📊 Quick Reference Summary

### Minimum Inputs (Required):
1. Overall Quality (1-10)
2. Overall Condition (1-10)
3. Year Built
4. Year Remodeled
5. Above Ground Living Area
6. Total Basement Area
7. First Floor Area
8. Second Floor Area
9. Lot Area
10. Bedrooms Above Ground
11. Full Bathrooms
12. Half Bathrooms
13. Basement Full Bathrooms
14. Basement Half Bathrooms
15. Garage Car Capacity
16. Garage Area

### Optional (But Recommended):
17. Zoning Classification
18. Neighborhood
19. House Style
20. Central Air Conditioning
21. Kitchen Quality
22. Number of Fireplaces

---

## 💡 Tips for Accurate Predictions

1. **Be Honest:** Don't inflate quality/condition ratings
2. **Measure Carefully:** Use actual square footage, not estimates
3. **Check Records:** Year built/remodeled should be from official records
4. **Count Correctly:** Only count full bathrooms (with tub/shower)
5. **Use Defaults:** If unsure about optional fields, use the defaults:
   - Zoning: **RL**
   - Neighborhood: **CollgCr**
   - House Style: **2Story** or **1Story**
   - Central Air: **Y**
   - Kitchen Quality: **TA**
   - Fireplaces: **0** or **1**

---

## 🎯 Example: Complete Input

Here's a complete example for a typical suburban home:

```
General Information:
- Overall Quality: 7 (good quality)
- Overall Condition: 5 (average condition)
- Year Built: 2000
- Year Remodeled: 2000 (never remodeled)

Area & Space:
- Above Ground Living Area: 1,500 sq ft
- Total Basement Area: 750 sq ft
- First Floor Area: 750 sq ft
- Second Floor Area: 750 sq ft
- Lot Area: 8,000 sq ft

Rooms & Features:
- Bedrooms Above Ground: 3
- Full Bathrooms: 2
- Half Bathrooms: 1
- Basement Full Bathrooms: 0
- Basement Half Bathrooms: 0
- Garage Car Capacity: 2
- Garage Area: 500 sq ft

Additional Features:
- Zoning: RL
- Neighborhood: CollgCr
- House Style: 2Story
- Central Air: Y
- Kitchen Quality: TA
- Fireplaces: 1
```

**Expected Prediction:** ~$180,000 - $220,000

---

**Now you know exactly what each field means! 🎉**
