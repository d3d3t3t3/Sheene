# -*- coding: utf-8 -*-
# 에스와이에스에서 아규밸류를 가져옴
from sys import argv
# 본 스크립트엔 파일네임을 같이 입력후 실행해야 됨
script, filename = argv
# 파일네임을 열고 티엑스티에 값으로 정의
txt = open(filename)
# 파일 파일네임의 내용을 보여줘
print "파일 %r의 내용:" % filename
# 티엑스티파일을 읽고 보여줘
print txt.read()

print "파일 이름을 다시 입력해주세요."
# 입력프롬프트를 >로써 표시하고 입력 받을 준비
# 입력 받은 값을 파일어게인에 정의
file_again = raw_input(">")
# 텍스트어게인 에 파일어겐인을 열어줘
txt_again = open(file_again)
# 텍스트어게인 파일을 읽어서 보여줘
print txt_again.read()