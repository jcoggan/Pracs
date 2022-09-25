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

price_per_kWh = int(input("price per kWh: "))
daily_usage = int(input("daily usage: "))
billing_period = int(input("billing period: "))
estimated_bill = (price_per_kWh * daily_usage * billing_period)
print(f"Estimated_bill ${estimated_bill}")