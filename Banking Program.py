import os
import sys
from datetime import datetime


class Borrower:
    """
    Layer 1 - Data Layer
    Stores all applicant information collected during the loan application process.
    Acts as the single source of truth for borrower attributes throughout the system.
    """

    def __init__(self, name, dob, cash_flow, monthly_income, credit_score, loan_amount, loan_term):
        self.name = name
        self.dob = dob
        self.monthly_income = monthly_income
        self.cash_flow = cash_flow
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.loan_term = loan_term

    def get_summary(self):
        """Prints a formatted summary of the borrower's profile."""
        print(f"Borrower Name  : {self.name}")
        print(f"Date Of Birth  : {self.dob}")
        print(f"Monthly Income : ${self.monthly_income:,.2f}")
        print(f"Cash Flow      : ${self.cash_flow:,.2f}")
        print(f"Credit Score   : {self.credit_score}")
        print(f"Loan Amount    : ${self.loan_amount:,.2f}")
        print(f"Loan Term      : {self.loan_term} years")


class RiskEngine:
    """
    Layer 2 - Math Engine
    Performs all financial ratio calculations (DSCR, DTI) on a Borrower object.
    Produces a risk verdict based on industry-standard thresholds.
    Does not store data or make final decisions — only calculates and classifies.
    """

    def __init__(self, borrower_data):
        self.borrower_data = borrower_data

    def calculate_dti(self):
        """Debt-to-Income Ratio: measures what percentage of income goes toward debt."""
        return self.borrower_data.loan_amount / self.borrower_data.monthly_income

    def calculate_dscr(self):
        """Debt Service Coverage Ratio: measures cash flow against monthly loan repayment."""
        monthly_payment = self.borrower_data.loan_amount / (self.borrower_data.loan_term * 12)
        return self.borrower_data.cash_flow / monthly_payment

    def get_risk_verdict(self):
        """Classifies borrower risk into four tiers based on DTI, DSCR, and credit score."""
        dscr = self.calculate_dscr()
        dti = self.calculate_dti()
        score = self.borrower_data.credit_score

        if dti < 0.36 and dscr >= 1.25 and score >= 700:
            return "Low Risk"
        elif dti < 0.43 and dscr < 1.25 and score >= 650:
            return "Medium Risk"
        elif dti >= 0.43 or dscr < 1.0 or score < 650:
            return "High Risk"
        else:
            return "Undetermined Risk"


class CreditPersistence:
    """
    Layer 3 - Persistence Layer
    Handles all file operations: initializing storage and saving borrower records.
    Uses static methods because it operates on data passed to it, not on instance state.
    All records are saved to a CSV file for future analysis with Pandas.
    """

    @staticmethod
    def initialize_database():
        """Creates the borrower CSV file with headers if it does not already exist."""
        if not os.path.exists("borrowers.csv"):
            with open("borrowers.csv", "w") as f:
                f.write("Name,Date of Birth,Monthly Income,Cash Flow,"
                        "Credit Score,Loan Amount,Loan Term,Risk Verdict\n")

    @staticmethod
    def save_borrower(borrower_data, risk_verdict):
        """Appends a borrower record and their risk verdict to the CSV file."""
        with open("borrowers.csv", "a") as f:
            f.write(f"{borrower_data.name},{borrower_data.dob},{borrower_data.monthly_income},"
                    f"{borrower_data.cash_flow},{borrower_data.credit_score},"
                    f"{borrower_data.loan_amount},{borrower_data.loan_term},{risk_verdict}\n")


class CreditDecision:
    """
    Layer 4 - Decision Layer
    Translates the RiskEngine verdict into a clear, actionable loan decision.
    Exists so that any non-technical stakeholder can read the final outcome directly.
    """

    def __init__(self, borrower, risk_engine):
        self.borrower = borrower
        self.risk_engine = risk_engine

    def make_decision(self):
        """Returns a formal loan decision based on the risk classification."""
        verdict = self.risk_engine.get_risk_verdict()

        if verdict == "Low Risk":
            return "APPROVED"
        elif verdict == "Medium Risk":
            return "APPROVED WITH CONDITIONS"
        elif verdict == "High Risk":
            return "DENIED"
        elif verdict == "Undetermined Risk":
            return "FURTHER REVIEW REQUIRED"
        else:
            return "ERROR IN RISK ASSESSMENT"


class GenerateCreditMemo:
    """
    Layer 5 - Memo Layer
    Assembles all outputs from the other layers into a single, readable credit memo.
    This is the final document a loan officer reviews — it contains the borrower
    profile, financial ratios, risk verdict, and the ultimate credit decision.
    """

    def __init__(self, borrower, risk_engine, credit_decision):
        self.borrower = borrower
        self.risk_engine = risk_engine
        self.credit_decision = credit_decision

    def generate_memo(self):
        """Prints the full credit assessment memo to the console."""
        print("\n" + "=" * 45)
        print("        IRON BANK — CREDIT ASSESSMENT MEMO")
        print("=" * 45)
        self.borrower.get_summary()
        print("-" * 45)
        print(f"DSCR           : {self.risk_engine.calculate_dscr():.2f}")
        print(f"DTI            : {self.risk_engine.calculate_dti():.2f}")
        print("-" * 45)
        print(f"Risk Verdict   : {self.risk_engine.get_risk_verdict()}")
        print(f"Decision       : {self.credit_decision.make_decision()}")
        print("=" * 45 + "\n")


# --- ENTRY POINT ---

def main():
    CreditPersistence.initialize_database()

    borrower = Borrower(
        name="SOMANJAN SAHA",
        dob="18-09-2006",
        monthly_income=5000.00,
        cash_flow=2000.00,
        credit_score=720,
        loan_amount=150000.00,
        loan_term=30
    )

    risk_engine = RiskEngine(borrower)
    credit_decision = CreditDecision(borrower, risk_engine)
    memo = GenerateCreditMemo(borrower, risk_engine, credit_decision)

    memo.generate_memo()

    CreditPersistence.save_borrower(borrower, risk_engine.get_risk_verdict())
    print("[LOG] Borrower record saved to borrowers.csv")


if __name__ == "__main__":
    main()
