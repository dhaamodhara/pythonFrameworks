# by using oop
class Node:
    def __init__(self,data,addr=None):
        self.data=data
        self.addr=addr
    def get_nextaddr(self):
        return self.addr
    def get_value(self):
        return self.data
    def set_nextaddr(self,addr):
        self.addr=addr
class LinkedList:
    def __init__(self):
        self.first=None
        self.last=None
    def isEmpty(self):
        return
        self.first==None and self.last==None
    def create_node(self):
        data=self.get_dataip()
        newnode=Node(data)
        return newnode
    def insert_beginning(self,newnode):
        self.first=newnode
        self.last=newnode
    def append(self):
        newNode=self.create_node()
        if self.isEmpty():
            self.insert_beginning(newnode)
            self.last=newnode
    def insert(self,pos):
        newnode=self.create_node()
        if self.isEmpty():
            self.insert_beginning(newnode)
        if pos==0:
            newnode.set_nextaddr(self.first)
            self.fist=newnode
        if pos<=len(self):
            ptr=self.first
            for i in range(0,pos):
                prev=ptr
                ptr=ptr.get_nextaddr()
                self.last.set_nextaddr(newnode)
                self.last=newnode
        else:
            print("invalid position")
    def pop(self):
        if isEmpty():
            print("List is empty")
            return None
            ptr=self.first
            if self.first==self.last:
                self.insert_beginning(None)
        else:
            while ptr.get_nextaddr()!=None:
                prev=ptr
                ptr=ptr.get_nextaddr()
                prev.set_nextaddr(None)
                self.last=None
                return ptr
    def remove(self,pos):
        if isEmpty():
            print("List is Empty")
            return None
            ptr=self.first
        if pos<0 and pos>len(self)-1:
            print("Invalid position")
            return None
        else:
            for i in range(0,pos):
                prev=ptr
                ptr=ptr.get_nextaddr()
            if pos!=0:
                prev,set_nextaddr(ptr.get_nextaddr())
                ptr.set_nextaddr(None)
                if pos==len(self)-1:
                    self.last=None
                if pos==0:
                    self.first=self.first.get_nextaddr()
                    return ptr
    def __str__(self):
        ptr=self.first
        data=" "
        while ptr!=None:
            data+=str(ptr.get_value())+" "
            ptr=ptr.get_nextaddr()
            return data
    def __getitem__(self,index):
        if index<0:
            index=len(1)+index
        if index>=0 and index<len(self):
            ptr=self.fist
            for i in range(index):
                ptr=ptr.get_nextaddr()
                return ptr.get_value()
    def __len__(self):
        ptr=self.first
        count=0
        while ptr!=None:
            ptr=ptr.get_nextaddr()
            count+=1
            return count
    @staticmethod
    def get_dataip():
        return
        int(input("Enter the data "))
l=LinkedList()
l.append()
l.append()
print(len(l))
print(l)
print(l[0])

