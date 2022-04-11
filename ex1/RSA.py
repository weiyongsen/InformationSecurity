import math

ming = "CQUINFORMATIONSECURITYEXP1"

# 加密可替换字符
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
# 假设 p3 q11
p = 3
q = 13
# 计算b和phi
n = p*q
f = (p-1)*(q-1)
# 选择e
e=0
for i in range(3,100):
    if(math.gcd(i,f)==1):
        e=i
        break
# 选择d
d = 0
for i in range(3,100):
    if((i * e) % f == 1):
        d=i
        break

# 原文
print("原文:",ming)
# 数字尝试
mima = []
print("0-35加密:",end="")
for i in range(36):
    mima.append(i**e % n)
    print(i**e %n, end=" ")
print("\n解密：", end=" ")
for i in range(36):
    print(mima[i]**d % n, end=" ")



# 加密
print("\n\nencode: e = ",e)
mi = ""
l = len(ming)

for i in range(l):
    pos = alpha.find(ming[i])
    temp = pos**e % n
    mi += alpha[temp]
print("加密后:",mi)
# 解密
print("decode: d = ",d)
ans = ""
for i in range(l):
    pos = alpha.find(mi[i])
    temp = pos**d % n
    ans += alpha[temp]
print("解密后:",ans)