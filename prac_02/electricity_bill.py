"""
Electricity Bill

price per kWh in cents,
daily use in kWh, and
number of days in the billing period.

pseudocode:
get price_per_kWh
get daily_usage
get billing_period
estimated_bill = (price_per_kWh * daily_usage * billing_period)
display estimated_bill in $
"""

def main():
    billing_period, daily_usage, price_per_kWh = get_power_details()
    estimated_bill = calculate_estimated_bill(billing_period, daily_usage, price_per_kWh)
    print(f"Estimated_bill ${estimated_bill}")


def calculate_estimated_bill(billing_period, daily_usage, price_per_kWh):
    estimated_bill = (price_per_kWh * daily_usage * billing_period)
    return estimated_bill


def get_power_details():
    price_per_kWh = int(input("price per kWh: "))
    daily_usage = int(input("daily usage: "))
    billing_period = int(input("billing period: "))
    return billing_period, daily_usage, price_per_kWh


main()
