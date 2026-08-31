# Lab ระหว่างเรียน ส่วนที่ 2: การดำเนินการกับลิสต์ (Operations)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLowestValue(head):
    """
    ฟังก์ชันค้นหาค่าที่น้อยที่สุดในลิสต์
    """
    # HINT 1: กำหนดค่าเริ่มต้นให้ minValue = head.data แล้วเริ่มวนลูปเช็คจากโหนดที่สอง (head.next)[cite: 1]
    # หากเจอค่าที่น้อยกว่าให้บันทึกทับตัวแปรเดิม[cite: 1]
    
    # TODO: เขียนโค้ดหาค่าที่น้อยที่สุดและ return ค่านั้นออกมา
    pass

def insertNodeAtPosition(head, newNode, position):
    """
    ฟังก์ชันแทรกโหนดใหม่ลงในตำแหน่งที่กำหนด
    """
    # HINT 2: ใช้ลูป for เลื่อน currentNode ไปหยุดอยู่ที่โหนด "ก่อนหน้า" ตำแหน่งที่ต้องการแทรก (position - 2)[cite: 1]
    # HINT 3: ลำดับ Pointer สำคัญมาก! ต้องให้ newNode.next ชี้ไปยังโหนดถัดไปก่อน 
    # แล้วค่อยเอา currentNode.next มาชี้ที่โหนดใหม่ หากสลับลำดับกันสายลิสต์จะขาดทันที[cite: 1]
    
    # TODO: เขียนโค้ดเพื่อแทรกโหนด
    pass

def deleteSpecificNode(head, nodeToDelete):
    """
    ฟังก์ชันลบโหนดที่กำหนดออกจากลิสต์
    """
    # HINT 4: การลบโหนดคล้ายกับการแทรก คือหาโหนดที่อยู่ก่อนหน้าตัวที่ต้องการลบ 
    # แล้วสั่งให้ pointer กระโดดข้ามโดยใช้ currentNode.next = currentNode.next.next[cite: 1]
    
    # TODO: เขียนโค้ดลบโหนด และ return head ของลิสต์ที่อัปเดตแล้ว
    pass

print("--- ผลลัพธ์ส่วนที่ 2: Operations ---")
# TODO: สร้าง Singly Linked List เตรียมไว้สำหรับทดสอบ
# TODO: ทดสอบเรียกใช้ findLowestValue, insertNodeAtPosition และ deleteSpecificNode