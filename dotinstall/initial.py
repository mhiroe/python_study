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


# lesson 2


# 変数

msg = "Hello2"
print(msg)
msg = "Hello2again"
print(msg)


# 定数：値の再代入ができない(値を変更したくないもの)
# pythonでは変数を大文字にしたら定数として扱う

ADMIN_EMAIL= "mon"
print(ADMIN_EMAIL)
ADMIN_EMAIL= "nyapo"
print(ADMIN_EMAIL)
