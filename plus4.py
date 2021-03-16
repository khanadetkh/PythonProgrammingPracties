# Input: รับจำนวนจริง 1 จำนวนจากแป้นพิมพ์ เก็บใน a
# Process: ให้ x มีค่าเป็น 1 จากนั้นทำคำสั่ง x = (x + a/x)/2 จำนวน 4 ครั้ง
# Output: ค่า x ที่ได้จากการทำงานข้างบนน

print('Enter Your Real Number')
a = float(input())
x = 1
x = (x + a/x)/2
x = (x + a/x)/2
x = (x + a/x)/2
x = (x + a/x)/2
print(x)