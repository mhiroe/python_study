# coding: utf-8
# python2まではソースコードに日本語が含まれている場合は↑のように冒頭に追記する


# 単一のコメント
"""
コメントまとめてかける
シングルクオート or ダブルクオート３つで囲む
"""

# python3では ()必須
# 文末の;は省略可能
print("Hello World")

print "----------------------"

#
# lesson 2 変数
#

msg = "Hello2"
print(msg)
msg = "Hello2again"
print(msg)


# 定数：値の再代入ができない(値を変更したくないもの)
# pythonでは変数を大文字にしたら定数として扱う
# - 代入はできてしまうが、代入を避けること

ADMIN_EMAIL= "mon"
print(ADMIN_EMAIL)

print "----------------------"


#
# "lesson 3 様々なデータ""
#

# 文字列
s = "Hello world3"

# 文字列 特殊文字
s = "Hello \nworld\t3"

# 複数行の文章をそのままデータとして表現する
# - htmlとか プログラム中に書いても処理に影響を与えない
# - 結果としてはコメントと同じものとなる
html = """<html>
<body><body>
</html>"""

print(html)

# 整数
i = 10
#浮動小数
f = 23.4
#論理値
flag = True #False 頭は大文字になる

print(i)
print(f)
print(flag)

print "----------------------"
print "lesson4 データの演算"

# + - * /
# 切り捨て徐算 //
# あまり %
# ペキ乗 **


x = 10
print(x /3) # 3.333
print "lesson4 データの演算"

# + - * /
# 切り捨て徐算 //
# あまり %
# ペキ乗 **


x = 10
print(x /3) # 3.333

print "lesson4 データの演算"

# + - * /
# 切り捨て徐算 //
# あまり %
# ペキ乗 **

x = 10
print(x / 3) # 3.333...
print(x / 3) # 3
print(x // 3) # 1 切り捨て徐算
print(x % 3) # 1 余り
print(x ** 3) # 100 ぺき乗

y = 4
y = y + 12
print(y) # 16
 # よくあるので以下のような省略記法がある
Y += 4
print(y) # 20

 # 論理値 and or not
 print(True and False) # False
 print(True or False) # True
 print(not True) # True
