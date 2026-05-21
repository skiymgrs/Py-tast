x = int(input("Enter a 1number: "))
print(x)

y = int(input("Enter a 2number: "))
print(y)

# 1. ใช้ True เพื่อสั่งให้ลูปนี้ทำงานไปเรื่อยๆ ไม่มีวันหยุด จนกว่าเราจะสั่งสั่งหยุดเอง
while True:
    z = input("Do you want to add the two numbers? (y/n): ")

    if z == "y":
        print(x + y)
        break  # 2. เจอคำว่า break โปรแกรมจะหลุดออกจากลูปทันทีเพราะทำงานสำเร็จแล้ว
        
    elif z == "n":
        print("Okay, not adding the numbers.")
        print(x, y)
        print("this is your numbers")
        print("Goodbye!")
        break  # 3. หลุดออกจากลูปเช่นกันเมื่อกด n
        
    else:
        # 4. ถ้าพิมพ์อย่างอื่นเข้ามา มันจะไม่เจอ break ลูป while ก็จะวนกลับไปถามคำถามด้านบนใหม่ทันที!
        print("Invalid input. Please enter 'y' or 'n'. Only!")
        