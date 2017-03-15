#!/usr/bin/env python
#coding:utf-8
#按照字典序从大到小排列
'''myInput=raw_input("plaese input some numbers:")
for i in reversed(sorted(myInput.split())):
	print i
'''
def order(myInput):
	final=[]
	num=myInput.split()
	for n in reversed(sorted(int(i) for i in num)):
		final.append(n)
	return final
if __name__=='__main__':
	myInput=raw_input("plaese input some numbers:")
	print order(myInput)

