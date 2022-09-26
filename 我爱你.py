a=input("请输入昵称1：")
b=input("请输入昵称2：")
peo=True
print("当你想转换角色时，请输入op，然后回车")
while peo==True:
    p1=input(a+":")
    if p1=="op":
        peo=False
while peo == False:
    p2=input(b+":")
    if p2 == "op":
        peo=True