class Tower:
    def __init__(self):
        self.pipeA = []
        self.pipeB = []
        self.pipeC = []

    def tower(self,disk):#5 items
        self.pipeA.append(disk)
        print("pipeA:" , self.pipeA)
        print("Disks are now in pipeA\n") 
    
    def step1(self):
        self.temp = self.pipeA.pop(4)
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"    ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step1 completed\n")
    
    def step2(self):
        self.temp = self.pipeA.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step2 completed\n")

    def step3(self):
        self.temp = self.pipeC.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step3 completed\n")

    def step4(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step4 completed\n")

    def step5(self):
        self.temp = self.pipeB.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step5 completed\n")

    def step6(self):
        self.temp = self.pipeB.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step6 completed\n")

    def step7(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step7 completed\n")

    def step8(self):
        self.temp = self.pipeA.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step8 completed\n")

    def step9(self):
        self.temp = self.pipeC.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step9 completed\n")

    def step10(self):
        self.temp = self.pipeC.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step10 completed\n")

    def step11(self):
        self.temp = self.pipeB.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step11 completed\n")

    def step12(self):
        self.temp = self.pipeC.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step12 completed\n")

    def step13(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step13 completed\n")

    def step14(self):
        self.temp = self.pipeA.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step14 completed\n")

    def step15(self):
        self.temp = self.pipeC.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step15 completed\n")

    def step16(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step16 completed\n")
    
    def step17(self):
        self.temp = self.pipeB.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step17 completed\n")

    def step18(self):
        self.temp = self.pipeB.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step18 completed\n")

    def step19(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step19 completed\n")

    def step20(self):
        self.temp = self.pipeB.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step20 completed\n")

    def step21(self):
        self.temp = self.pipeC.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step21 completed\n")

    def step22(self):
        self.temp = self.pipeC.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step22 completed\n")

    def step23(self):
        self.temp = self.pipeB.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step23 completed\n")

    def step24(self):
        self.temp = self.pipeB.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step24 completed\n")

    def step25(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step25 completed\n")

    def step26(self):
        self.temp = self.pipeA.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step26 completed\n")

    def step27(self):
        self.temp = self.pipeC.pop()
        self.pipeB.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step27 completed\n")

    def step28(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step28 completed\n")

    def step29(self):
        self.temp = self.pipeB.pop()
        self.pipeA.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step29 completed\n")

    def step30(self):
        self.temp = self.pipeB.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("Step30 completed\n")

    def step31(self):
        self.temp = self.pipeA.pop()
        self.pipeC.append(self.temp)
        print("pipeA:",self.pipeA  ,"   ",  "pipeB:",self.pipeB  ,"   ","pipeC:",self.pipeC)
        print("LastStep completed\n")


  




    

  

obj = Tower()
obj.tower("disk5")
obj.tower("disk4")
obj.tower("disk3")
obj.tower("disk2")
obj.tower("disk1")
obj.step1()
obj.step2()
obj.step3()
obj.step4()
obj.step5()
obj.step6()
obj.step7()
obj.step8()
obj.step9()
obj.step10()
obj.step11()
obj.step12()
obj.step13()
obj.step14()
obj.step15()
obj.step16()
obj.step17()
obj.step18()
obj.step19()
obj.step20()
obj.step21()
obj.step22()
obj.step23()
obj.step24()
obj.step25()
obj.step26()
obj.step27()
obj.step28()
obj.step29()
obj.step30()
obj.step31()


