from prac_09.unreliable_car import UnreliableCar

for i in range(10):
    my_car = UnreliableCar(i, 100, 60)
    my_car.drive(1)
    print(f"{my_car}")
