# Question 1
in_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=in_file)
in_file.close()


# Question 2
in_file = open(f"name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your Name is {name}")


# Question 3
in_file = open("numbers.txt", "r")
a = int(in_file.readline())
b = int(in_file.readline())
in_file.close()
c = a + b
print(f"Resulting number from file is {c}")


# Question 4
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
in_file.close()
print(f"Total of all numbers in file is {total}")