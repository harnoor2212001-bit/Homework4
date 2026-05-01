# Homework 5: Debt Maturity Audit Skill

### What the skill does
Analyzes a list of debt instruments, calculates exact days until maturity, and determines the weighted average interest rate across the portfolio.

### Why the script is load-bearing
Calculating weighted averages and counting exact days between dates (handling leap years or varying month lengths) is a deterministic task. LLMs are prone to "near-miss" math errors or hallucinations with these figures. This Python script ensures 100% accuracy for financial auditing.

### Walkthrough Video
https://youtu.be/iZ4yX7ZQt84