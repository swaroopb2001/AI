import random

class Vacuum:
    lis=[0,0]
    def __init__(self) -> None:
         #2 rooms
        self.lis=[random.choice([0,1]) for i in self.lis]
    def clean(self):
        for i in range(2):
            if self.lis[i]:
                print("Room",i,"is dirty")
                self.lis[i]=1
                print("Room",i,"is cleansed successfully")
            else:
                print("Room",i,"is already clean")
if __name__=="__main__":
    cleaner=Vacuum()
    cleaner.clean()
