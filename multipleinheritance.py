class Father:
    def gardening(self):
        print("I love gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

#derived class from mother and father
class Child(Father,Mother):
    def sports(self):
        print("I love playing football")

#objects 
c = Child()
c.gardening()
c.cooking()
c.sports()

#if the methods are same 
# class Father:
#     def skills(self):
#         print("gardening")

# class Mother:
#     def skills(self):
#         print("cooking")

# class Child(Father,Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("playing football")

# c = Child()
# c.skills()