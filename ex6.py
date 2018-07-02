# -*- coding: utf-8 -*-

# x 에 "세상에는 % 종류의 사람이 있어요" 문자열을 정의
x = "세상에는 %d 종류의 사람이 있어요." % 10
# binary 에 '이진수'란 문자열을 값으로 정의
binary = "'이진수'"
# do_not 에 "모르는" 문자열을 정의
do_not = "모르는"
# y 에 "%를 아는 사람과 % 사람." 문자열을 값으로 정의,
# 각 %는 binary, do_not 에 정의된 값을 정의
y = "%s를 아는 사람과 %s 사람." % (binary, do_not)
# z 에 "How fun is it!" 정의
z = 'How fun is it!'

print x
print y
print z

# format string %s에 x 값을 포맷
# x는 "세상에는 %종료의 사람이 있어요." 문자열 정의
# % 에는 10 값이 포맷
print "'%s'라고 했어요." % x

print "'%s'라고도 했죠." % y
# %r 에는 z 가 포맷
# z 는 "How fun is it!" 값이 정의
print "So, %r" % z

hilarious = False
joke_evaluation = "웃기는 농담 아니에요?! %r"

print joke_evaluation % hilarious

w = "이 문자열의 왼쪽 ->"
e = "<- 이 문자열의 오른쪽"

print w + e