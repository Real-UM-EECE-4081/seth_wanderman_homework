print("Question 8")
def Tower_Of_Hanoi(n , a, b, c):
    if n == 1:
        print ("Move disk 1 from rod ",a,"to rod ",b)
        return
    Tower_Of_Hanoi(n-1, a, c, b)
    print ("Move disk",n,"from rod ", a,"to rod ", b)
    Tower_Of_Hanoi(n-1, c, b, a)
n = 4
Tower_Of_Hanoi(n, "A", "B", "C")