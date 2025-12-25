# 🏠 Sample Test Data for House Price Prediction

Use these sample houses to test your web application and demonstrate to your instructor.

---

## 📋 Test Case 1: Average Suburban House
**Expected Price Range**: $150,000 - $180,000

### Input Values:
```
General Information:
- Overall Quality: 5
- Overall Condition: 5
- Year Built: 1995
- Year Remodeled: 1995

Area & Space:
- Above Ground Living Area: 1200 sq ft
- Total Basement Area: 600 sq ft
- First Floor Area: 1000 sq ft
- Second Floor Area: 200 sq ft
- Lot Area: 8000 sq ft

Rooms & Features:
- Bedrooms Above Ground: 3
- Full Bathrooms: 2
- Half Bathrooms: 0
- Basement Full Bathrooms: 0
- Basement Half Bathrooms: 0
- Garage Car Capacity: 2
- Garage Area: 400 sq ft

Additional Features:
- Zoning: RL (Residential Low Density)
- Neighborhood: NAmes
- House Style: 1Story
- Central Air: Y
- Kitchen Quality: TA (Typical/Average)
- Fireplaces: 0
```

---

## 📋 Test Case 2: High-End Modern House
**Expected Price Range**: $280,000 - $350,000

### Input Values:
```
General Information:
- Overall Quality: 8
- Overall Condition: 8
- Year Built: 2005
- Year Remodeled: 2005

Area & Space:
- Above Ground Living Area: 2200 sq ft
- Total Basement Area: 1100 sq ft
- First Floor Area: 1100 sq ft
- Second Floor Area: 1100 sq ft
- Lot Area: 12000 sq ft

Rooms & Features:
- Bedrooms Above Ground: 4
- Full Bathrooms: 3
- Half Bathrooms: 1
- Basement Full Bathrooms: 1
- Basement Half Bathrooms: 0
- Garage Car Capacity: 3
- Garage Area: 700 sq ft

Additional Features:
- Zoning: RL
- Neighborhood: NridgHt (Northridge Heights - Premium)
- House Style: 2Story
- Central Air: Y
- Kitchen Quality: Ex (Excellent)
- Fireplaces: 2
```

---

## 📋 Test Case 3: Small Starter Home
**Expected Price Range**: $100,000 - $130,000

### Input Values:
```
General Information:
- Overall Quality: 4
- Overall Condition: 5
- Year Built: 1960
- Year Remodeled: 1960

Area & Space:
- Above Ground Living Area: 900 sq ft
- Total Basement Area: 450 sq ft
- First Floor Area: 900 sq ft
- Second Floor Area: 0 sq ft
- Lot Area: 6000 sq ft

Rooms & Features:
- Bedrooms Above Ground: 2
- Full Bathrooms: 1
- Half Bathrooms: 0
- Basement Full Bathrooms: 0
- Basement Half Bathrooms: 0
- Garage Car Capacity: 1
- Garage Area: 250 sq ft

Additional Features:
- Zoning: RL
- Neighborhood: OldTown
- House Style: 1Story
- Central Air: N
- Kitchen Quality: TA
- Fireplaces: 0
```

---

## 📋 Test Case 4: Luxury Estate
**Expected Price Range**: $400,000 - $550,000

### Input Values:
```
General Information:
- Overall Quality: 10
- Overall Condition: 9
- Year Built: 2008
- Year Remodeled: 2008

Area & Space:
- Above Ground Living Area: 3500 sq ft
- Total Basement Area: 1800 sq ft
- First Floor Area: 1750 sq ft
- Second Floor Area: 1750 sq ft
- Lot Area: 20000 sq ft

Rooms & Features:
- Bedrooms Above Ground: 5
- Full Bathrooms: 4
- Half Bathrooms: 2
- Basement Full Bathrooms: 1
- Basement Half Bathrooms: 1
- Garage Car Capacity: 3
- Garage Area: 900 sq ft

Additional Features:
- Zoning: RL
- Neighborhood: StoneBr (Stone Brook - Premium)
- House Style: 2Story
- Central Air: Y
- Kitchen Quality: Ex
- Fireplaces: 3
```

---

## 📋 Test Case 5: Older Home with Renovation
**Expected Price Range**: $180,000 - $220,000

### Input Values:
```
General Information:
- Overall Quality: 6
- Overall Condition: 7
- Year Built: 1975
- Year Remodeled: 2010

Area & Space:
- Above Ground Living Area: 1500 sq ft
- Total Basement Area: 750 sq ft
- First Floor Area: 1000 sq ft
- Second Floor Area: 500 sq ft
- Lot Area: 9000 sq ft

Rooms & Features:
- Bedrooms Above Ground: 3
- Full Bathrooms: 2
- Half Bathrooms: 1
- Basement Full Bathrooms: 1
- Basement Half Bathrooms: 0
- Garage Car Capacity: 2
- Garage Area: 500 sq ft

Additional Features:
- Zoning: RL
- Neighborhood: CollgCr (College Creek)
- House Style: 1.5Fin
- Central Air: Y
- Kitchen Quality: Gd (Good)
- Fireplaces: 1
```

---

## 🎯 How to Use These Test Cases

### For Demonstration:
1. **Start with Test Case 1** (Average house) - shows typical prediction
2. **Show Test Case 4** (Luxury) - demonstrates high-end pricing
3. **Compare Test Case 3 vs Test Case 2** - shows how quality affects price

### For Validation:
- Run all 5 test cases
- Check if predictions are in expected ranges
- Verify that higher quality = higher price
- Confirm that larger area = higher price

### For Your Instructor:
1. **Show Test Case 2** and explain the inputs
2. Get prediction
3. Explain why the price makes sense:
   - "High quality (8/10) increases value"
   - "Large living area (2200 sq ft) adds to price"
   - "Premium neighborhood (NridgHt) commands higher prices"
   - "Modern construction (2005) valued higher"

---

## 📊 Expected Model Behavior

### Ridge Regression Predictions:
- More consistent across similar houses
- Smoother price curves
- May underestimate luxury homes
- May overestimate low-quality homes

### Random Forest Predictions:
- More varied predictions
- Better captures quality thresholds
- More accurate for extreme cases
- Wider confidence intervals

### Comparison:
```
Test Case 1 (Average):
- Ridge: ~$165,000
- Random Forest: ~$168,000
- Difference: Small (~2%)

Test Case 4 (Luxury):
- Ridge: ~$420,000
- Random Forest: ~$485,000
- Difference: Larger (~15%)
```

**Why?** Random Forest better captures non-linear jumps in luxury market!

---

## 💡 Tips for Testing

### Quick Test:
Just use Test Case 1 - it's representative of most houses.

### Comprehensive Test:
Use all 5 cases to show model handles diverse properties.

### Edge Case Test:
Try extreme values:
- Overall Quality: 1 (worst)
- Overall Quality: 10 (best)
- Living Area: 500 sq ft (tiny)
- Living Area: 5000 sq ft (mansion)

### Neighborhood Effect Test:
Use same house specs but change neighborhood:
- OldTown → Lower price
- NridgHt → Higher price
- StoneBr → Highest price

---

## 🎓 For Your Presentation

### Demo Script:
1. **Open web app**: `streamlit run app.py`
2. **Load Test Case 2**: "Let me predict a high-quality modern house..."
3. **Enter values**: Show the input form
4. **Click Predict**: Get result
5. **Explain**: "The model predicts $XXX,XXX because..."
6. **Show comparison**: Go to Model Comparison tab
7. **Discuss**: "Random Forest was X% more accurate because..."

### Key Points:
- ✅ Model handles diverse house types
- ✅ Predictions are reasonable and explainable
- ✅ Quality and size are major price drivers
- ✅ Both algorithms provide useful insights

---

## 📝 Quick Reference Card

**Print this and keep it handy during presentation:**

```
AVERAGE HOUSE (Test Case 1):
Quality: 5 | Area: 1200 | Built: 1995 | Bed: 3 | Bath: 2 | Garage: 2
Expected: $150K-$180K

HIGH-END HOUSE (Test Case 2):
Quality: 8 | Area: 2200 | Built: 2005 | Bed: 4 | Bath: 3 | Garage: 3
Expected: $280K-$350K

STARTER HOME (Test Case 3):
Quality: 4 | Area: 900 | Built: 1960 | Bed: 2 | Bath: 1 | Garage: 1
Expected: $100K-$130K
```

---

**Good luck with your testing and presentation! 🎉**
