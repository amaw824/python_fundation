# 字串變數初始化
string01 = "1,2,3,4"
print(string01)


# 替換字串
'''
用法
string.replace(str1, str2)
說明
將 string 中的 str1 替換成 str2
'''
string02 = "Alex"
string02 = string02.replace('ex', 'len')
print(string02)


# 去除字串兩側空格
'''
用法
string.strip()
說明
去除字串 string 左、右兩邊的空格
'''
string03 = "        ___ccc___         "
print(string03)
print(string03.strip())


# 字串變成小寫或大寫
'''
用法
string.lower()
說明
將字串 string 裡的字母全部改成小寫
'''
print("CAR".lower())

'''
用法
string.upper()
說明
將字串 string 裡的字母全部改成大寫
'''
print("good".upper())


'''
格式化字串 - 使用 %
'''
# 多組文字
msg = '%s, %s!' % ('Hello', 'World')
print(msg)

# 整數
msg = 'I am %d years old.' % 5
print(msg)

# 文字與整數
msg = '%s is %d years old.' % ('Alex', 18)
print(msg)

# 指定寬度 (維持 10 個字元長度，預設向右對齊)
msg = '[%10s]' % 'Hello'
print(msg)

# 靠左對齊 (維持 10 個字元長度，向左對齊)
msg = '[%-10s]' % 'Hello'
print(msg)

# 指定浮點數位數
msg = '[%8.3f]' % 12.3456
print(msg)

# 指定文字長度上限 (只有文字，才在格式化字串中加入「.」來限定字串長度)
msg = '[%.3s]' % 'Hello'
print(msg)

# 空白補 0
msg = '[%06.2f]' % 3.1415926
print(msg)