 #coding:utf-8
	
	
#递归二分法查找
# -*- coding: utf-8 -*- 

def f(s,arr):

    if len(arr) == 1:

        return 0 if s == arr[0] else -100 # 4



    mid = int(len(arr)/2)



    if s == arr[mid]:

        return mid

    elif s > arr[mid]:

        return mid + f(s,arr[mid:])

    else:

        return f(s,arr[0:mid])

#测试----------------------------------

list = range(1,12,2)#包含从1到12（不包括12）的有序列表,间隔2

for x in range(0,12):

    num = f(x,list)

    if num >= 0 :

        print f(x,list)

    else:

        print "False！"
#一些简单的基础排序#
  
    '''快速排序'''


def qsort(seq):

	if seq==[]:

		return []

	else:

		pivot=seq[0]

		lesser=qsort([x for x in seq[1:] if x<pivot])

		greater=qsort([x for x in seq[1:] if x>=pivot])

		return lesser+[pivot]+greater

 

if __name__=='__main__':

	seq=[5,6,78,9,0,-1,2,3,-65,12]

	print(qsort(seq))

   '''希尔排序'''

def shellSort(seq):

	length=len(seq)

	inc=0

	while inc<=length/3:

		inc=inc*3+1

	print(inc)

	while inc>=1:

		for i in range(inc,length):

			tmp=seq[i]

			for j in range(i,0,-inc):

				if tmp<seq[j-inc]:

					seq[j]=seq[j-inc]

				else:

					j+=inc

					break

			seq[j-inc]=tmp

		inc//=3

 

 

if __name__=='__main__':

	seq=[8,6,4,9,7,3,2,-4,0,-100,99]

	shellSort(seq)

	print(seq)
    
'''拓扑排序'''

def indegree0(v,e): 

	if v==[]:

		return None

	tmp=v[:]

	for i in e:

		if i[1] in tmp:

			tmp.remove(i[1])

	if tmp==[]:

		return -1

 

	for t in tmp:

		for i in range(len(e)):

			if t in e[i]:

				e[i]='toDel' #占位，之后删掉

	if e:

		eset=set(e)

		eset.remove('toDel')

		e[:]=list(eset)

	if v:

		for t in tmp:

			v.remove(t)

	return tmp

 

def topoSort(v,e):

	result=[]

	while True:

		nodes=indegree0(v,e)

		if nodes==None:

			break

		if nodes==-1:

			print('there\'s a circle.')

			return None

		result.extend(nodes)

	return result

 

v=['a','b','c','d','e']

e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]

res=topoSort(v,e)

print(res)

'''堆排序'''

def fixUp(a): #在堆尾加入新元素，fixUp恢复堆的条件

	k=len(a)-1

	while k>1 and a[k//2]<a[k]:

		a[k//2],a[k]=a[k],a[k//2]

		k=k//2

 

def fixDown(a): #取a[1]返回的值，然后把a[N]移到a[1]，fixDown来恢复堆的条件

	k=1

	N=len(a)-1

	while 2*k<=N:

		j=2*k

		if j<N and a[j]<a[j+1]: 

			j+=1

		if a[k]<a[j]:

			a[k],a[j]=a[j],a[k]

			k=j

		else:

			break

 

def insert(a,elem):

	a.append(elem)

	fixUp(a)

 

def delMax(a):

	maxElem=a[1]

	N=len(a)

	if N<=1:

		print('There\'s none element in the list')

		return -1

	if N==2:

		return a[1]

	else:

		a[1]=a.pop()

		fixDown(a)

		return maxElem

 

data=[-1,] #第一个元素不用，占位

insert(data,26)

insert(data,5)

insert(data,77)

insert(data,1)

insert(data,61)

insert(data,11)

insert(data,59)

insert(data,15)

insert(data,48)

insert(data,19)

 

result=[]

N=len(data)-1

for i in range(N):

	print(data)

	result.append(delMax(data))

print(result)

'''归并排序'''

def mergesort(seq):

	if len(seq)<=1:

		return seq

	mid=int(len(seq)/2)

	left=mergesort(seq[:mid])

	right=mergesort(seq[mid:])

	return merge(left,right)

 

def merge(left,right):

	result=[]

	i,j=0,0

	while i<len(left) and j<len(right):

		if left[i]<=right[j]:

			result.append(left[i])

			i+=1

		else:

			result.append(right[j])

			j+=1

	result+=left[i:]

	result+=right[j:]

	return result

 

if __name__=='__main__':

	seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]

	print(mergesort(seq))

	
'''冒泡排序'''

def bubbleSort(seq):

	length=len(seq)

	for i in range(length):

		for j in range(length-1,i,-1):

			if seq[j-1]>seq[j]:

				seq[j-1],seq[j]=seq[j],seq[j-1]

 

 

if __name__=='__main__':

	seq=[2,9,7,7,4,3,2,-4,54,-7,0]

	bubbleSort(seq)

	print(seq)
    
'''选择排序'''

def selectionSort(seq):

	length=len(seq)

	for i in range(length):

		mini=min(seq[i:])

		if seq[i]>mini:

			j=seq.index(mini,i)

			seq[i],seq[j]=seq[j],seq[i]

 

 

if __name__=='__main__':

	seq=[3,4,5,9,3,1,5,7,90,-2,]

	selectionSort(seq)

	print(seq)
'''插入排序--分别有基于比较和替换的两种 其实基础排序方式都差不多'''

def insertionSort(seq):

	length=len(seq)

	for i in range(1,length):

		tmp=seq[i]

		for j in range(i,0,-1):

			if seq[j-1]>tmp:

				seq[j]=seq[j-1]

			else:

				j+=1

				break

		seq[j-1]=tmp

 

 

if __name__=='__main__':

	seq=[8,6,4,9,7,3,2,-4,0,-100,99]

	insertionSort(seq)

	print(seq)
#----------------------------柔美的分割线

def insertionSort2(seq):

	length=len(seq)

	for i in range(1,length):

		for j in range(i,0,-1):

			if seq[j]<seq[j-1]:

				seq[j],seq[j-1]=seq[j-1],seq[j]

			else:

				break

 

if __name__=='__main__':

	seq=[3,5,9,8,4,2,1,0,-6,12,-8]

	insertionSort2(seq)

	print(seq)
    #大约就是这些了


