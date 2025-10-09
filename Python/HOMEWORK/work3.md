# 第三章作业
## 结果和代码
```python
# 一、            给出下列数据的类型（int/float/bool/NoneType）
# 1）3.14 float
# 2）-34 int
# 3）True bool
# 4）None NoneType
# 5）3.0 float

print("第一题")
lst = [3.14, -34, True, None, 3.0]
for i in lst:
    a = type(i)
    print(f'{i} is {a}')

# 二、            计算下列算术表达式的值
# 1）6+12-3 15
# 2）2*3.0 6.0
# 3）--4 4
# 4）10/3 3.3333333333333335
# 5）10//3 3
# 6）10.0/3.0 3.3333333333333335
# 7）(2+3)*4 20
# 8）2+3*4 14
# 9）2**3+1 9
# 10）2.1**2.0 4.41

print("第二题")
lst = ['6+12-3', '2*3.0', '--4', '10/3', '10//3', '10.0/3.0', '(2+3)*4', '2+3*4', '2**3+1', '2.1**2.0']
for i in lst:
    a = eval(i)
    print(f'{i} is {a}')


# 三、            计算下列关系表达式、逻辑表达式的值
# 1）3>4 False
# 2）4.0>3.999 True
# 3）4>4 False
# 4）4>+4 False
# 5）2+2==4 True
# 6）True or False True
# 7）False or False False
# 8）not False True
# 9）3.0-1.0!=5.0-3.0 False
# 10）3>4 or (2<3 and 9>10) False
# 11）4>5 or 3<4 and 9>8 True
# 12）not(4>3 and 100>6) False

print("第三题")
lst = ['3>4', '4.0>3.999', '4>4', '4>+4', '2+2==4', 'True or False', 'False or False', 'not False', '3.0-1.0!=5.0-3.0', '3>4 or (2<3 and 9>10)', '4>5 or 3<4 and 9>8', 'not(4>3 and 100>6)']
for i in lst:
    a = eval(i)
    print(f'{i} is {a}')


# 四、            给出下列表达式的类型（int/float/bool/error），并计算其值
# 1）3+5.0 float 8.0
# 2）5/2 float 2.5
# 3）5/2==5/2.0 bool True
# 4）5/2.0 float 2.5
# 5）round(2.6) int 3
# 6）int(2.6) int 2
# 7）round(2.5) int 2
# 8）2.0+5.0 float 7.0
# 9）5*2==5.0*2.0 bool True

print("第四题")
lst = ['3+5.0', '5/2', '5/2==5/2.0', '5/2.0', 'round(2.6)', 'int(2.6)', 'round(2.5)', '2.0+5.0', '5*2==5.0*2.0']
for i in lst:
    a = eval(i)
    print(f'{i} is {a} and type is {type(a)}')


# 五、            计算下列表达式的值，结果用十六进制表示（写出中间步骤）
# 1）3+2<<1+1 5<<2 5=0b101 左移两位 0b10100 20=0x14
# 2）2*9|3>>1 18|3>>1 3=0b11 3右移一位 0b1 18=0b10010 0b10010|0b1=0b10011 19=0x13
# 3）~5&3 5=0b101 ~5=-0b110 -0b110&0b11=0b10 2=0x2
# 4）5|3+4&5*3 5|7&15 5=0b101 7=0b111 15=0b1111 0b111&0b1111=0b111 0b101|0b111=0b111 7=0x7

print("第五题")
lst = ['3+2<<1+1', '2*9|3>>1', '~5&3', '5|3+4&5*3']
for i in lst:
    a = eval(i)
    print(f'{i} is {a} and hex is {hex(a)}')

```

## 程序运行结果
```shell
D:\APP_cs\YD_learn\github\youth4science>python ./Python/HOMEWORK/work3.py
第一题
3.14 is <class 'float'>
-34 is <class 'int'>
True is <class 'bool'>
None is <class 'NoneType'>
3.0 is <class 'float'>
第二题
6+12-3 is 15
2*3.0 is 6.0
--4 is 4
10/3 is 3.3333333333333335
10//3 is 3
10.0/3.0 is 3.3333333333333335
(2+3)*4 is 20
2+3*4 is 14
2**3+1 is 9
2.1**2.0 is 4.41
第三题
3>4 is False
4.0>3.999 is True
4>4 is False
4>+4 is False
2+2==4 is True
True or False is True
False or False is False
not False is True
3.0-1.0!=5.0-3.0 is False
3>4 or (2<3 and 9>10) is False
4>5 or 3<4 and 9>8 is True
not(4>3 and 100>6) is False
第四题
3+5.0 is 8.0 and type is <class 'float'>
5/2 is 2.5 and type is <class 'float'>
5/2==5/2.0 is True and type is <class 'bool'>
5/2.0 is 2.5 and type is <class 'float'>
round(2.6) is 3 and type is <class 'int'>
int(2.6) is 2 and type is <class 'int'>
round(2.5) is 2 and type is <class 'int'>
2.0+5.0 is 7.0 and type is <class 'float'>
5*2==5.0*2.0 is True and type is <class 'bool'>
第五题
3+2<<1+1 is 20 and hex is 0x14
2*9|3>>1 is 19 and hex is 0x13
~5&3 is 2 and hex is 0x2
5|3+4&5*3 is 7 and hex is 0x7
```