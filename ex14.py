# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '>'

print "안녕 %s, 나는 %s 스크립트 야." % (user_name, script)
print "몇가지 물어볼께?"
print "%s야, 나를 좋아해?" % user_name
likes = raw_input(prompt)

print "%s야, 어디에 사니?" % user_name
lives = raw_input(prompt)

print "%s야, 어떤 컴퓨터를 갖고 있어?" % user_name
computer = raw_input(prompt)

print """
좋아, 나를 좋아하냐는 질문에 '%s'.
'%s'에 살고. 어딘지 모르겠는데.
글구, '%s' 컴퓨터를 쓴다구. 좋아써.
"""  % ( likes, lives, computer )