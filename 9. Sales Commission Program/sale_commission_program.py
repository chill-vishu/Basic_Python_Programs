# Create A Program That Calculates Sales Commissions

def calculate_commission():
    sales = float(input("Enter the sales amount: "))
    commission_rate = 0.1  # 10% commission rate
    commission = sales * commission_rate
    print(f"Sales commission is: ${commission:.2f}")

# Calling Function
calculate_commission()
