#!/usr/bin/env python
#coding:utf-8
#2-7的题
'''def test_for(n):
 	for i in n:
 		print i
def test_while(n): 
	index=0
	while index<len(n):
		print n[index]
		index+=1
'''
#6-5第一问 自己写的第一版。当mid=len(n)/2+1时，不知道怎么处理
'''def test(n):
	if len(n)%2==0:
		mid=len(n)/2
	else:
		mid=len(n)/2+1
	first=0
	last=len(n)-1
	while first<mid:
		print n[first]
		print n[last]
		first+=1
		last-=1
'''
#6-5第一问 第二版，函数返回list，调用后需要用print
'''def test2(str):
	n=len(str)
	list=[]
	if n%2==0:
		for i in range(0,n/2):
			list.append(str[i])
			list.append(str[n-i-1])
	else:
		for i in range(0,int(n/2)+1):
			if i!=int(n/2):
				list.append(str[i])
				list.append(str[n-i-1])
			else:
				list.append(str[int(n/2)])
	return list
'''
#6-5 第二问 第一版print会循环多次,加上break后就好了。
'''def pipei(str1,str2):
	x=len(str1)
	y=len(str2)
	if x!=y:
		print "str1!=str2"
	for i in range(x):
		if str1[i]!=str2[i]:
			print "str1!=str2"
			break
		else:
			if i!=x-1:
				continue
			else:
				print "str1=str2"
'''
'''
def pipei(str1,str2):
	for i,j in zip(str1,str2):
		if i is not j:
			print 'not'
			break
		else:
			print 'yes'
'''
def huiwen(str):
	x=list(str)
	x.reverse()
	new2=list(str)+x

	print "".join(new2)

if __name__=='__main__':
	'''myInput=raw_input('please input a str:')'''
	'''test(myInput)'''
	'''test_while(myInput)'''
	'''print test2(myInput)'''
	'''str1=raw_input('please input the first str:')
	str2=raw_input('please input the second str:')
	pipei(str1,str2)'''
	while True:
		myInput=raw_input('please input a str:')
		if myInput=='q':
			break
		else:
			print huiwen(myInput)

