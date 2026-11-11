class Transaction:
    def __init__(self, transaction_id, book_id, member_id, issue_date):
        self.transaction_id = transaction_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.return_date = None

    def display_info(self):
        print("=================================== Transaction Details ===================================")
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Book ID: {self.book_id}")
        print(f"Member ID: {self.member_id}")
        print(f"Issue Date: {self.issue_date}")
        if self.return_date is not None:
            print(f"Return Date: {self.return_date}")
        else:
            print("The book has not been returned yet.")

    def mark_returned(self, return_date):
        self.return_date = return_date

transaction1 = Transaction("T001", "B001", "M001", "05-11-2026")

transaction1.display_info()

transaction1.mark_returned("10-11-2026")

transaction1.display_info()