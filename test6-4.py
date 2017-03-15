#!usr/bin/env python
#coding:utf-8
def test(myInput):
	n=0
	nums=myInput.split()
	for y in (int(i) for i in nums):
		n+=y
		'print n'
	final=float(n)/len(nums)
	return final
if __name__=='__main__':
	myInput=raw_input("please input some numbers:")
	print test(myInput)
