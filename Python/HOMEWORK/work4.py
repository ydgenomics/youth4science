# 1) 给定三个正整数，分别表示三条线段的长度，判断这三条线段能否构成一个三角形。

a, b, c = map(int, input().split(" "))
if a + b > c and a + c > b and b + c > a:
    print("yes")
else:
    print("no")

# 2) 读入n（1 <= n <= 10000）个整数，求它们的和与均值
# 输入
# 输入第一行是一个整数n，表示有n个整数。
# 第2~n+1行每行包含1个整数。每个整数的绝对值均不超过10000。
# 输出
# 输出一行，先输出和，再输出平均值（保留到小数点后5位），两个数间用单个空格分隔。

n = int(input())
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)

total = sum(lst)
average = round(total / n, 5)
print(total, "%.5f" % average, sep=" ")

# 3) 根据邮件的重量和用户是否选择加急计算邮费。计算规则：重量在1000克以内(包括1000克), 基本费8元。超过1000克的部分，每500克加收超重费4元，不足500克部分按500克计算；如果用户选择加急，多收5元。
# 输入
# 输入一行，包含整数和一个字符，以一个空格分开，分别表示重量（单位为克）和是否加急。如果字符是y，说明选择加急；如果字符是n，说明不加急。
# 输出
# 输出一行，包含一个整数，表示邮费。
weight, urgent = input().split(" ")
weight = int(weight)
if weight <= 1000:
    cost = 8
else:
    cost = 8 + ((weight - 1000) // 500 + ((weight - 1000) % 500 > 0)) * 4


if urgent == 'y':
    cost += 5


print(cost)


# 4) 请统计某个给定范围[L, R]的所有整数中，数字2出现的次数。
# 比如给定范围[2, 22]，数字2在数2中出现了1次，在数12中出现1次，在数20中出现1次，在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。
# 输入
# 输入共 1 行，为两个正整数 L 和 R，之间用一个空格隔开。
# 输出
# 输出共 1 行，表示数字 2 出现的次数。

n1, n2 = input().split(" ")

s = ""
for i in range(int(n1), int(n2)+1):
    i = str(i)
    s += i

num = 0
for i in s:
    if i == "2":
        num += 1

print(num)

# 5) 水仙花数是指一个n位数 (n≥3)，它的每个位上的数字的n次幂之和等于它本身。例如：153是一个“水仙花数”，因为 153 是个 3位数，而153=13+53+33。输入一个正整数Max，输出100到Max之间的所有水仙花数（包括max）。
# 输入格式:
# 共一行，为一个正整数。
# 输出格式：
# 若干行，从小到大输出水仙花数，一行为一个数。
# 输入样例：
# 2500
# 输出样例：
# 153
# 370
# 371
# 407
# 1634

max_num = int(input())

for i in range(100, max_num + 1):
    str_i = str(i)
    sum = 0
    times = len(str_i)
    for j in str_i:
        sum += int(j)**times
    if i == sum:
        print(i)
