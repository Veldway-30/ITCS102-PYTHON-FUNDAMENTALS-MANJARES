def branch(legion):
    print(f"You are of the {legion} legion")

def inputer(name):
   print(f"Your name is {name}")
   legion = input("What is your favorite legion? ")
   print(f"{name}, your favorite legion is the {legion}.")
        
    
branch("Blood Angels")
branch("Alpha")
branch("Salamander")

inputer("Cj")