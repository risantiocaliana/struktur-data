class Node:
    def __init__(self, my_data):
        self.data = my_data
        self.next = None
class circularLinkedList:
    def __init__(self):
         self.head = None
    def add_data(self, my_data):
        ptr_1 = Node(my_data)
        temp = self.head
        ptr_1.next = self.head
        
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr_1
        else:
            ptr_1.next = ptr_1
        self.head = ptr_1
    
    def print_it(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print("%s" %(temp.data)),
                temp = temp.next
                if (temp == self.head):
                    break
my_list = circularLinkedList()        
pilih = "y"
while (pilih == "y"):
    print("===============================")
    print("| Menu aplikasi linked list |")
    print("===============================")
    print("1. Insert data")
    print("2. Delete data")
    print("3. Cari data")
    print("4. Panjang dari linked list")
    print("5. Tampil data")
    print("===============================")
    pilihan=str(input(("Silakan masukan pilihan anda:")))
    
    if(pilihan=="1"):
        obj = str(input("Masukan data yang ingin andatambahkan: "))
        my_list.add_data(obj)
    elif(pilihan=="2"):
        obj = str(input("Masukan data yang ingin anda dihapus: "))
        #self.delete(obj)
        x = input("")
    elif(pilihan=="3"):
        obj = str(input("Masukan data yang ingin anda dicari: "))
        status = my_list.search(obj)
        
        if status == True:
            print("Data ditemukan pada list")
        else:
            print("Data tidak ditemukan")
            x = input("")
        
    elif(pilihan=="4"):
        print("Panjang dari linked list adalah:"+str(my_list.size()))
        x = input("")
    elif(pilihan=="5"):
        my_list.print_it()
        x = input("")
    else:
        pilih="n"
    
                           