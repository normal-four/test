#coding=utf-8
__author__ = 'wang'
import random
l=[]
for i in xrange(1,11):
    l.append(random.randint(0,100))
print l
print '-+++++++++++++++++++-'
class Algorithm:
    def __init__(self,l):
        self.l=l
    #冒泡排序，每次排出最大的
    def BubbleSort(self):
        s=self.l
        for i in range(len(s)-1,0,-1):#一共10个数，要循环十次
            for j in range(i):#第一次取出最大的数
                if s[j]>s[j+1]:
                    s[j],s[j+1]=s[j+1],s[j]
        print s

    u'''选择排序与冒泡排序的区别：冒泡算法，每次比较如果发现较小的元素在后面，就交换两个相邻的元素。
    而选择排序算法的改进在于：先并不急于调换位置，先从A[1]开始逐个检查，看哪个数最小就记下该数所在的位置P，
    等一躺扫描完毕，再把A[P]和A[1]对调，这时A[1]到A[10]中最小的数据就换到了最前面的位置。
    所以，选择排序每扫描一遍数组，只需要一次真正的交换，而冒泡可能需要很多次。比较的次数是一样的。 '''
    #选择排序：每次选出最小的值放在前面
    def SelectionSort(self):
        s=self.l
        for i in range(len(s)-1):
            smallest=s[i]
    #插入排序：每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止
    def InsertSort(self):
        s=self.l
        for i in range(1,len(s)):#定位一个s[i]，通过循环判断s[i]在之前排序的列表中的位置插进去
            j=i
            while j>0 and s[j-1]>s[i]:#循环查询，插入，并删除原索引上的值
                j-=1
                s.insert(j,s[i])
                s.pop(i+1)
                i-=1
        print s




alg=Algorithm(l)
alg.BubbleSort()
print '--------------'
alg.InsertSort()
print "==================="