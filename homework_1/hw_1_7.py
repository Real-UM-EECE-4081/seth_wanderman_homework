print("Question 7")
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius **2 *3.14
    def perimeter(self):
        return 2 *self.radius *3.14
updated_Cicrle = Circle(10)
print(updated_Cicrle.area())
print(updated_Cicrle.perimeter())