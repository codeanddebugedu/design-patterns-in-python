class PaymentProcessor:
    def pay(self, payment_method: str, amount: int):
        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs.{amount}")
            print("UPI transaction finished")
        elif payment_method == "credit_card":
            print(f"Starting credit card transaction of Rs.{amount}")
            print("Credit card transaction finished")
        elif payment_method == "net_banking":
            print(f"Starting net banking transaction of Rs.{amount}")
            print("Net Banking transaction finished")


pay_p = PaymentProcessor()
pay_p.pay("credit_card", 500)
