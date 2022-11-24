from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
taxi.drive(18)
print(taxi)
print(f"${taxi.get_fare():.2f}")
