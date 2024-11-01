from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
    """
    An extension to CreditCard that compounds interest and fees.
    """

    def __init__(self, customer, bank, acnt, limit, apr):
        # Create a new predatory credit card instance.
        # The initial balance is zero.
        # Customer - the name of the customer.
        # Bank - the name of the bank.
        # Acnt - the account identifier.
        # Limit - the credit limit. (measured in dollars)
        # Apr - the annual percentage rate.

        super().__init(customer, bank, acnt, limit) # Call Super Constructor
        
        self._apr = apr

    def charge(self, price):
        # Charge given price to the card, assuming sufficient credit limit.
        # Return True if charge was processed.
        # Return False and assess $5 fee if charge is denied.

        success = super().charge(price)

        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        # Assess monthly interest as outstanding balance.

        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor