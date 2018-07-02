# -*- coding: utf-8 -*-
# sys에서 argv를 import해.
from sys import argv

# 스크립트와 인풋파일은 아규먼트밸류다.
script, input_file = argv

# 에프를 갖는 프린터올은:
def print_all(f):
# 에프를 read해 프린트해.
	print f.read()

# 에프를 갖는 rewind란:	
def rewind(f):
# 0을 갖고 에프를 seek해.
	f.seek(0)

# 라인카운터와 에프를 갖는 프린터라인은:	
def print_a_line(line_count, f):
    # 라인카운터와 에프리드라인을 프린트해.
	print line_count, f.readline()

# 커런트파일에 인풋파일을 갖고 open해.	
current_file = open(input_file)

# 해당 문자열과 한줄 내려 프린트해.
print "파일 전체를 출력해 봅시다.\n"

# 커런트파일을 갖고 프린터올해.
# 커런트파일을 read해 프린트해.
print_all(current_file)
print "커런트파일은 %r입니다." % current_file
# 문자열을 프린트해.
print "이번에는 테이프처럼 되감아 봅시다."

# 커런트파일을 가지고 rewind 해.
rewind(current_file)

print "커런트파일은 %r입니다." % current_file
# 문자열을 프린트해.
print "세 줄을 출력해 봅시다."

# 커런트라인을 하나 더한다.
current_line = 1
# 커런트라인과 커런트파일을 가지고 프린터라인해.
print_a_line(current_line, current_file)

# 커런트라인을 하나 더한다.
current_line = current_line + 1
# 커런트라인과 커런트파일을 가지고 프린터라인해.
print_a_line(current_line, current_file)

# 커런드라인을 하나 더한다.
current_line = current_line + 1
# 커런트라인과 커런트파일을 가지고 프린트어라인해.
print_a_line(current_line, current_file)
print "커런트라인 숫자는 %d입니다." % current_line