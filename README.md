# Iron Bank — Automated Credit Risk Assessment System

A modular, Python-based credit risk engine that evaluates loan applications using
industry-standard financial ratios and produces a formal credit assessment memo.

## Overview

This system automates the credit evaluation process by analysing borrower financial
data through a five-layer architecture. Given a borrower's income, cash flow, credit
score, and loan parameters, the system calculates key risk metrics (DSCR and DTI),
classifies the applicant into a risk tier, and issues a formal credit decision —
approved, approved with conditions, or denied.

Built as the first capstone project in a four-year roadmap targeting a Credit Risk
Analyst role at HSBC or a Risk Advisory role at a Big 4 firm.

## Architecture

| Layer | Class | Responsibility |
|-------|-------|---------------|
| 1 | `Borrower` | Stores all applicant data collected during loan application |
| 2 | `RiskEngine` | Calculates DSCR, DTI, and classifies borrower risk tier |
| 3 | `CreditPersistence` | Saves borrower records and risk verdicts to CSV storage |
| 4 | `CreditDecision` | Translates risk verdict into a formal loan decision |
| 5 | `GenerateCreditMemo` | Assembles all outputs into a readable credit assessment memo |

## Key Metrics

- **DSCR** (Debt Service Coverage Ratio) — measures cash flow against monthly repayment
- **DTI** (Debt-to-Income Ratio) — measures what percentage of income goes toward debt

## Risk Tiers

| DTI | DSCR | Credit Score | Verdict |
|-----|------|-------------|---------|
| < 0.36 | ≥ 1.25 | ≥ 700 | Low Risk → Approved |
| < 0.43 | < 1.25 | ≥ 650 | Medium Risk → Approved with Conditions |
| ≥ 0.43 | < 1.0 | < 650 | High Risk → Denied |

## How to Run

```bash
python credit_risk_system.py
```

Output: a formatted credit memo printed to console + borrower record saved to `borrowers.csv`

## Roadmap

- [ ] Pandas integration for bulk borrower analysis
- [ ] NumPy synthetic data generation for model stress testing  
- [ ] IFRS 9 Expected Credit Loss engine
- [ ] Streamlit dashboard for interactive loan evaluation
- [ ] Machine learning PD (Probability of Default) scoring model

## Tech Stack

- Python 3.x
- Standard library only (Phase 1)
- Pandas, NumPy, Streamlit — planned (Phase 2)

---

*Year 1 Capstone Project — B.Sc. Econometrics Honours, Calcutta University (2025–2029)*
