# Lab ระหว่างเรียน ส่วนที่ 3: Doubly และ Circular Linked List

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_forward(head):
    # TODO: เขียนโค้ดสำรวจข้อมูลไปข้างหน้า (Forward Traversal) แบบเดียวกับ Singly
    pass

def traverse_backward(tail):
    # HINT 1: การเดินถอยหลัง (Backward Traversal) ให้เริ่มที่ tail (โหนดสุดท้าย) 
    # และเปลี่ยนคำสั่งขยับโหนดในลูปเป็น currentNode.prev[cite: 1]
    
    # TODO: เขียนโค้ดสำรวจข้อมูลย้อนกลับ (Backward Traversal)
    pass

def traverse_circular_singly(head):
    # HINT 2: ป้องกันลูปไม่รู้จบใน Circular List โดยสร้างตัวแปร startNode เก็บจุดเริ่มต้นไว้ 
    # พิมพ์ค่าแรกออกมาก่อน แล้วขยับโหนด จากนั้นวนลูปเช็คเงื่อนไขหยุดเมื่อ currentNode != startNode[cite: 1]
    
    # TODO: เขียนโค้ดแสดงผลข้อมูลของ Circular Singly Linked List
    pass

def traverse_circular_doubly_forward(head):
    # HINT 3: โครงสร้างลูปเหมือน Circular Singly คือต้องมี startNode เพื่อเช็คการวนลูป[cite: 1]
    # TODO: เขียนโค้ดสำรวจข้อมูลไปข้างหน้าสำหรับ Circular Doubly Linked List
    pass

def traverse_circular_doubly_backward(tail):
    # HINT 4: เริ่มที่ tail พิมพ์ค่าก่อน 1 ครั้ง ขยับโหนดด้วย .prev และหยุดเมื่อวนกลับมาชน startNode (ซึ่งก็คือ tail)[cite: 1]
    # TODO: เขียนโค้ดสำรวจข้อมูลย้อนกลับ (Backward) สำหรับ Circular Doubly Linked List
    pass

print("--- ผลลัพธ์ส่วนที่ 3: Doubly & Circular ---")
# HINT 5: เวลาเชื่อมโหนด Doubly ต้องจับคู่ 2 ทางเสมอ คือกำหนด .next ให้ชี้ไปข้างหน้า 
# และ .prev ให้ชี้กลับมาหาโหนดตัวก่อนหน้า[cite: 1]
# TODO: สร้าง Doubly Linked List และทดสอบ

# TODO: สร้าง Circular Singly Linked List (ให้โหนดสุดท้าย next ชี้กลับไปที่ head) และทดสอบพิมพ์ข้อมูล

# HINT 6: การสร้าง Circular Doubly Linked List จะต้องเชื่อมโหนดสุดท้าย (tail) กับโหนดแรก (head) ทั้งสองทาง[cite: 1]
# คือ tail.next = head และ head.prev = tail[cite: 1]
# TODO: สร้าง Circular Doubly Linked List และทดสอบเรียกใช้ฟังก์ชันพิมพ์ข้อมูลทั้งไปข้างหน้าและย้อนกลับ