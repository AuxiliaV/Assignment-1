class allFunctions():

    def Subfields():
        List=["Sub-fields in AI are:","Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for word in List:
            print(word)

    def OddEven():
        num=int(input("Enter a Number:"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is Odd number")

    def ElegiblityForMarriage():
        Gen=input("Your Gender:")
        Ag=int(input("Your Age:"))
        if(Gen=="Male"):
            if(Ag<21):
               print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(Gen=="Female"):
            if(Ag<18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        else:
            print("INVALID INPUT")

    def percentage():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        total=Sub1+Sub2+Sub3+Sub4+Sub5
        per=(total/500)*100
        print("Total:",total)
        print("Percentage:",per)
        return total,per

    def Area():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        formula=(Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",formula)
        return formula
    
    def Perimeter():
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        formula=Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Area of Triangle:",formula)
        return formula




