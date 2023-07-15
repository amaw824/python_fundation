# 匯入模組
import myModule

# 計算幾次方
num = myModule.pow(2, 3)
print(num)

# 簡單斷句
txt = "I will always love you"
list_result = myModule.segmentSentence(txt)
print(list_result)


# 直接從模組中匯入函式
from myModule import pow, segmentSentence

# 計算幾次方
num = pow(2, 3)
print(num)

# 簡單斷句
txt = "I will always love you"
list_result = segmentSentence(txt)
print(list_result)