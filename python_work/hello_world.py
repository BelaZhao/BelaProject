# 井号表示注释，方便代码的理解和阅读，运行时注释内容不会运行

# print方法：在控制台输出值
print("Hello Python")
# 定义一个字符串变量message，可以重复对其赋值，每次打印（print）输出最新的值
message = "I'm Bela"
print(message)
message = "Nice to see you"
print(message)

name = 'zHaO BeLa'
# 链式调用即连续调用title upper lower方法
name = name.title().upper().lower() 
print(name)

# f方法：format 引号内是字符串，花括号内的字符会去找对应的变量赋值，连接成一个完整的字符串
say_hi = f"{message}, {name}."
print(say_hi)
# false: print( f"{s} {name}")"

# rstrip 删除末尾空白 r: right;  lstrip 删除开头空白 l: left; strip 前后空格都删除
favorite_language = " python  "
print(favorite_language.rstrip().lstrip())
# 不会改变该变量值
print(favorite_language)
# 重新赋值后会改变变量 favorite_language 的值
favorite_language = favorite_language.strip()
print(favorite_language)