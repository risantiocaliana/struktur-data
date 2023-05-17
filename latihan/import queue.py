import queue
class myQueue:
    def __init__(self):
        self.items = queue.Queue()

    # Memeriksa apakah queue dalam keadaan kosong
    def isEmpty(self):
        return self.items.empty()
    # Menambah data ke queue
    def qPut(self, item):
        self.items.put(item)
    # Mengeluarkan data dari queue
    def qGet(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "empty"
    # Menghitung panjang queue
    def size(self):
        return self.items.qsize()

    # Main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("=========================")
            print("| Menu aplikasi queue |")
            print("=========================")
            print("1. Put objek")
            print("2. Get objek")
            print("3. Cek Empty")
            print("4. Panjang dari queue")
            print("5. tampilkan semua queue")
            print("=========================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                obj = str(input("Masukan objek yang ingin anda tambahkan: "))
                self.qPut(obj)
                print("Object "+obj+" telah ditambahkan")
                x = input("")
            elif(pilihan=="2"):
                temp = self.qGet()
                if temp != "empty":
                    print("Objek "+temp+" dihapus")
                else:
                    print("Queue kosong")
                    x = input("")
            elif(pilihan=="3"):
                    print(self.isEmpty())
                    x = input("")
            elif(pilihan=="4"):
                    print("Panjang dari queue adalah:"+str(self.size()))
                    x = input("")
            elif(pilihan=="4"):
                    print("Panjang dari queue adalah:"+str(self.size()))
                    x = input("")
            elif(pilihan=="5"):
                    print(list(self.items.queue))
                    x = input("")
if __name__ == "__main__":
 q=myQueue()
 q.mainmenu()