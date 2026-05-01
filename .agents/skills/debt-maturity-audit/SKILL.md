---
name: debt-maturity-audit
description: Analyzes corporate debt instruments, calculates deterministic time-to-maturity, and computes weighted average interest rates. Use this for audit prep and liquidity reporting.
---

# Debt Maturity Audit

Use this skill when you have a list of debt obligations and need an accurate breakdown of maturity buckets and interest costs.

### When to use
- Auditing a debt ladder for upcoming refinancing needs.
- Calculating the weighted average cost of debt for a portfolio.
- Bucket debt into "Current" (Short-term) vs. "Long-term" liabilities.

### Expected Inputs
- A list of debt instruments with: Name, Principal, Maturity Date (MM/DD/YYYY), and Interest Rate.

### Instructions
1. Extract the debt data provided by the user into a clean JSON array.
2. Execute `scripts/calculate_maturity.py` passing that JSON.
3. Display the final weighted average and the maturity table to the user.

### Limitations
- Assumes fixed interest rates. 
- Does not provide financial advice; only performs deterministic calculation.