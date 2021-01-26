class A:
    def __init__(self,data):
        self.next=None
        self.data=data 
class B:
    def __init__(self):
        self.head=None
    def insertBeg(self,data):
        new=A(data)
        if self.head==None :
            self.head=new
            return
        temp=self.head
        self.head=new
        new.next=temp
    def deletionend(self):
        if self.head==None:
            print("List is Already Empty")
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    
        
    def display(self):
        if self.head==None:
            print("No node to print")
            return 
        temp=self.head 
        while temp!=None:
            print(temp.data)
            temp=temp.next
l=B()

l.insertBeg(93)
l.insertBeg(931)
l.insertBeg(934)
l.insertBeg(842)
l.deletionend()
l.deletionend()
l.display()