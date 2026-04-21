# Iron Bank — Automated Credit Risk Assessment System

> *"The Iron Bank will have its due."*

A five-layer, OOP-driven credit risk engine that evaluates loan applications using
industry-standard financial ratios and produces a formal credit assessment memo.
Built from scratch as Phase 1 of a four-year capstone series.

---

## What It Does

Given a borrower's financial profile, the system:
1. Calculates **DSCR** (Debt Service Coverage Ratio) and **DTI** (Debt-to-Income Ratio)
2. Classifies the borrower into a risk tier — Low, Medium, High, or Undetermined
3. Issues a formal credit decision — Approved, Approved with Conditions, Denied, or Further Review
4. Saves the borrower record to a CSV file for future bulk analysis
5. Prints a complete credit assessment memo to the console

---

## Architecture

This system follows a strict separation of concerns across five independent layers.
Each class has exactly one job. No layer bleeds into another.

| Layer | Class | Responsibility |
|-------|-------|----------------|
| 1 | `Borrower` | Stores all applicant data collected during loan application |
| 2 | `RiskEngine` | Calculates DSCR, DTI and classifies borrower risk tier |
| 3 | `CreditPersistence` | Saves borrower records and risk verdicts to CSV storage |
| 4 | `CreditDecision` | Translates risk verdict into a formal loan decision |
| 5 | `GenerateCreditMemo` | Assembles all outputs into a readable credit assessment memo |

---

## Key Financial Metrics

**DSCR — Debt Service Coverage Ratio**
```
DSCR = Monthly Cash Flow / Monthly Loan Payment
```
Measures whether the borrower generates enough cash flow to cover their loan repayment.
A DSCR below 1.0 means the borrower cannot cover the payment from cash flow alone.

**DTI — Debt-to-Income Ratio**
```
DTI = Total Loan Amount / Monthly Income
```
Measures what percentage of income is committed to debt obligations.

---

## Risk Classification

| DTI | DSCR | Credit Score | Risk Tier | Decision |
|-----|------|-------------|-----------|----------|
| < 0.36 | ≥ 1.25 | ≥ 700 | Low Risk | APPROVED |
| < 0.43 | < 1.25 | ≥ 650 | Medium Risk | APPROVED WITH CONDITIONS |
| ≥ 0.43 | < 1.0 | < 650 | High Risk | DENIED |
| Invalid data | — | — | Undetermined | FURTHER REVIEW REQUIRED |

---

## Sample Output

```
=============================================
        IRON BANK — CREDIT ASSESSMENT MEMO
=============================================
Borrower Name  : SOMANJAN SAHA
Date Of Birth  : 18-09-2006
Monthly Income : $5,000.00
Cash Flow      : $2,000.00
Credit Score   : 720
Loan Amount    : $150,000.00
Loan Term      : 30 years
---------------------------------------------
DSCR           : 0.16
DTI            : 30.00
---------------------------------------------
Risk Verdict   : High Risk
Decision       : DENIED
=============================================

[LOG] Borrower record saved to borrowers.csv
```

---

## Exception Handling

| Scenario | Handling |
|----------|----------|
| `monthly_income = 0` | ZeroDivisionError → returns `math.nan` → FURTHER REVIEW |
| `loan_term = 0` | ZeroDivisionError → returns `math.nan` → FURTHER REVIEW |
| CSV file locked in Excel | PermissionError caught with descriptive message |
| Disk full or read-only | OSError caught with descriptive message |
| NaN in memo output | Prints `UNDEFINED` instead of crashing |

---

## How to Run

```bash
python credit_risk_system.py
```

No external dependencies required for Phase 1. Standard library only.

---

## Roadmap

- [x] Five-layer OOP architecture
- [x] DSCR and DTI calculation engine
- [x] Three-tier risk classification
- [x] CSV persistence layer
- [x] Exception handling across all critical layers
- [ ] Pandas integration for bulk borrower analysis
- [ ] NumPy synthetic data generation (1M+ borrowers)
- [ ] IFRS 9 Expected Credit Loss engine (PD × LGD × EAD)
- [ ] Streamlit interactive dashboard
- [ ] ML-based Probability of Default scoring model
- [ ] Agentic AI narrative generation for credit memos

---

## Tech Stack

| Phase | Tools |
|-------|-------|
| Phase 1 (Current) | Python 3.x, standard library |
| Phase 2 | Pandas, NumPy |
| Phase 3 | Scikit-learn, Streamlit |
| Phase 4 | LangChain, Agentic AI |

---

*B.Sc. Econometrics Honours — Calcutta University (2025–2029)*
*Capstone 1 of 3 — targeting Credit Risk Analyst, HSBC Kolkata / Risk Advisory, Big 4*
