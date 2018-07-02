# -*- coding: utf-8 -*-

def add(a,b):
    print "덧셈 %d + %d" % (a, b)
    return a + b
    
def subtract(a,b):
    print "뺄셈 %d - %d" % (a, b)
    return a - b
    
def multiply(a,b):
    print "곱셈 %d * %d" % (a, b)
    return a * b
    
def divide(a,b):
    print "나눗셈 %d / %d" % (a, b)
    return a / b
    
print "함수만으로 계산해 봅시다."

add(40, 2)
print "함수 애드()는 %d를 리턴합니다." % add(1, 1)
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "나이: %d, \n 키: %d, \n 몸무게: %d, \n 아이큐: %d" % (age, height, weight, iq)
# 추가 점수 문제, 일단 써 보세요.
print "문제가 있어요."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "결과:", what, "손으로 계산할 수 있나요?"