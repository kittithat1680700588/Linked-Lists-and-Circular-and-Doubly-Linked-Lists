# Lab ระหว่างเรียน ส่วนที่ 1: โครงสร้างพื้นฐานและการสำรวจ (Singly Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_singly(head):
    """
    ฟังก์ชันสำหรับสำรวจข้อมูล (Traversal) ของ Singly Linked List
    """
    # HINT 1: การสำรวจข้อมูล ควรสร้างตัวแปรใหม่มารับค่า head (เช่น currentNode = head) 
    # เพื่อป้องกันไม่ให้โครงสร้างลิสต์เดิมพัง จากนั้นใช้ลูป while currentNode:[cite: 1]
    # HINT 2: ภายในลูป while บรรทัดสุดท้ายต้องอัปเดตตำแหน่งเสมอด้วย currentNode = currentNode.next 
    # หากลืม โปรแกรมจะติดลูปไม่รู้จบ (Infinite loop)[cite: 1]
    
    # TODO: เขียนโค้ดลูป while เพื่อสำรวจข้อมูลและแสดงผลจนกว่าจะถึง null
    pass

print("--- ผลลัพธ์ส่วนที่ 1: Singly Linked List ---")
# HINT 3: การเชื่อมโหนด (Linking) ควรสร้าง object ของ Node ให้ครบทุกตัวก่อน 
# แล้วค่อยจับคู่โดยระบุว่า node.next ชี้ไปที่ใคร[cite: 1]

# TODO: สร้างโหนดข้อมูล Integer 4 ตัว ได้แก่ 9, 1, 7, 8 และเชื่อมโยง (link) เข้าด้วยกัน