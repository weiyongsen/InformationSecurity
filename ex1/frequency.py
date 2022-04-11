from numpy import double
from sympy import ordered

#替换字符串string中指定位置p的字符为c
def replace(string,p,c):
    new = []
    for s in string:
        new.append(s)
    new[p] = c
    return ''.join(new)

#根据替换表dict解密密文mi，返回明文ming
def decode(dict,mi):
    size_p = len(dict)
    size_m = len(m)
    # 记录字符位置
    ming = m
    pos=[]
    for i in range(size_p):
        temp = []
        for j in range(size_m):
            if m[j]==list(dict.keys())[i]:
                temp.append(j)
        pos.append(temp)
    # print(pos)

    # 根据位置替换字符
    len1 = len(pos)
    for i in range(len1):
        for j in range(len(pos[i])):
            ming=replace(ming,pos[i][j],dict[list(dict.keys())[i]])

    return ming.lower()

# 处理密文概率
m = "UZ QSO VUOHXMOPV GPOZPEVSG ZWSZ OPFPESX UDBMETSX AIZ VUEPHZ HMDZSHZO WSFP APPD TSVP QUZW YMXUZUHSX EPYEPOPDZSZUFPO MB ZWP FUPZ HMDJ UD TMOHMQ"
code = "".join(m.split())
l = len(code)
p = {}
for i in range(l):
    if code[i] not in p:
        p[code[i]]=1
    else:
        p[code[i]]+=1
# print(p)
sum=sum(p.values())
for i in p.keys():
    p[i] = round(float(p[i]/len(m)),3)
print("密文中字母概率:")
print(p)
# 处理给定概率
order = "ETAONISRHLDCUPFMWYBGVKQXJZ"
freq = [0.123,0.096,0.081,0.079,0.072,0.072,0.066,0.060,0.051,0.04,0.037,0.032,0.031,0.023,0.023,0.023,0.02,0.019,0.016,0.016,0.009,0.005,0.002,0.002,0.001,0.001]
prob= {}
for i in range(len(order)):
    prob[order[i]]=freq[i]
print("正常英文中字母概率:")
print(prob)
# 得到替换表
dict = {}
for i in p.keys():
    min_fre = 1 # 最大概率
    for j in prob.keys():
        temp = abs(prob[j]-p[i])
        if temp<min_fre:
            dict[i] = j
            min_fre = temp
print("替换表:")
print(dict)
# 解密
print(decode(dict,m))
# 开始尝试
dict['U']='I'
dict['S']='A'
dict['W']='H'
print(decode(dict,m))

dict['D']='N'
dict['F']='V'
dict['T']='M'
print(decode(dict,m))

dict['I']='U'
print(decode(dict,m))

dict['E']='R'
print(decode(dict,m))

dict['X']='L'
print(decode(dict,m))

dict['Y']='P'
print(decode(dict,m))
# "UZ QSO VUOHXMOPV GPOZPEVSG ZWSZ OPFPESX UDBMETSX AIZ VUEPHZ HMDZSHZO WSFP APPD TSVP QUZW YMXUZUHSX EPYEPOPDZSZUFPO MB ZWP FUPZ HMDJ UD TMOHMQ"
dict['H']='C'
print(decode(dict,m))

dict['M']='O'
print(decode(dict,m))

dict['B']='F'
print(decode(dict,m))

dict['G']='Y'
print(decode(dict,m))

dict['J']='G'
# 最终解
print("最终替换表为:",dict)
print("最终解密结果:",decode(dict,m))
