# สร้างลิสต์ของตัวเลขในช่วง 21 ถึง 40
numbers = list(range(21, 41))

# หาตัวเลขคี่
odd_numbers = [num for num in numbers if num % 2 != 0]

# หาตัวเลขคู่
even_numbers = [num for num in numbers if num % 2 == 0]

print("จำนวนคี่:", odd_numbers)
print("จำนวนคู่:", even_numbers)