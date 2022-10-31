from guitar import Guitar

guitar = Guitar('Gibson L-5 CES', 1922, 16035.40)
print(f"Gibson L-5 CES get_age() - Expected 100. Got {Guitar.get_age(guitar)}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {Guitar.is_vitage(guitar)}")

guitar = Guitar("Another Guitar", 2013, 1234)
print(f"Anther Guitar get_age() - Expected 9. Got {Guitar.get_age(guitar)}")
print(f"Anther Guitar is_vintage() - Expected False. Got {Guitar.is_vitage(guitar)}")

