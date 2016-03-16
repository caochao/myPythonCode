#encoding=utf-8

import random

# 原文见http://www.cppblog.com/jedi-CY/archive/2009/06/28/88712.html
class CY_LianlianKan():
	def __init__(self, row, col):
		self.m_Array=[] #存储内容的矩阵
		self.m_LinkCount=0 #需要连的总数
		self.m_FirstPosition=-1 #记下连的第一点
		self.MaxWidth=col #矩阵宽 
		self.MaxHeight=row #矩阵高
		#其它初始化内容

	#目标坐标是否有效,超过矩阵宽高即无效
	def IsTargetXYValid(self,X,Y):
		pass

	#目标是否空白可以通过
	def IsTargetXYBlank(self,X,Y):  
		pass

	#获取矩阵坐标为XY的内容, 大于0表示此格有物体, 等于0表示无物体
	def GetArrayXY(self,X,Y):
		return self.m_Array[Y*self.MaxWidth+X]
    
	def GenRandomArray(self):
		for i in range( 0, self.MaxWidth * self.MaxHeight ):
			self.m_Array.append( 0 if random.random() > 0.5 else 1 )
		#self.m_Array = [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0]	#测试代码

	#判断两点是否可以通过某方向直线连接, #方向direction：1←2→3↑4↓
	def IsLineable(self,x1,y1,x2,y2,direction):
		if direction==1:
			if y1==y2 and x1>x2:
				for i in xrange(x2,x1+1):
					if self.GetArrayXY(i,y1)>0:
						return False
					return True
		elif direction==2:
			if y1==y2 and x1<x2:
				for i in xrange(x1,x2+1):
					if self.GetArrayXY(i,y1)>0:
						return False
					return True
		elif direction==3:
			if x1==x2 and y1<y2:
				for i in xrange(y1,y2+1):
					if self.GetArrayXY(x1,i)>0:
						return False
					return True
		elif direction==4:
			if x1==x2 and y2<y1:
				for i in xrange(y2,y1+1):
					if self.GetArrayXY(x1,i)>0:
						return False
					return True
		return False

	'''
	#path成功时用于记录路径 n当前剩下的连数 LRorUD当前方向是上下还是左右
	#hasReachPoint 一个矩阵，用于记录矩阵中各个点目前已经经过多少连了还找不到目标点
	'''
	def IsNTurnReachable(self,x1,y1,x2,y2,path,n,LRorUD,hasReachPoint):
		if n<=0:
			return False
		if LRorUD: #左右方向
			for x in xrange(x1-1,-1,-1):#向左
				if self.GetArrayXY(x,y1)==0 and hasReachPoint[y1*self.MaxWidth+x]<n:
					if self.IsLineable(x,y1,x2,y2,3) or self.IsLinable(x,y1,x2,y2,4):
						path+=[x,y1,x2,y2]
						return path
					else:#到达不了，上下转弯，递归
						hasReachPoint[y1*self.MaxWidth+x]+=1
						p=self.IsNTurnReachable(x,y1,x2,y2,path+[x,y1],n-1,False,hasReachPoint)
						if p!=False:
							return p
				else:break
			for x in xrange(x1+1,self.MaxWidth):#向右
				if self.GetArrayXY(x,y1)==0 and hasReachPoint[y1*self.MaxWidth+x]<n:
					if self.IsLineable(x,y1,x2,y2,3) or self.IsLineable(x,y1,x2,y2,4):
						path+=[x,y1,x2,y2]
						return path
					else:#到达不了，上下转弯，递归
						hasReachPoint[y1*self.MaxWidth+x]+=1
						p=self.IsNTurnReachable(x,y1,x2,y2,path+[x,y1],n-1,False,hasReachPoint)
						if p!=False:
							return p
				else:break
		else:#上下移动
			for y in xrange(y1-1,-1,-1):#向上
				if self.GetArrayXY(x1,y)==0 and hasReachPoint[y*self.MaxWidth+x1]<n:
					if self.IsLineable(x1,y,x2,y2,1) or self.IsLineable(x1,y,x2,y2,2):
						path+=[x1,y,x2,y2]
						return path
					else:#到达不了，左右转弯，递归
						hasReachPoint[y*self.MaxWidth+x1]+=1
						p=self.IsNTurnReachable(x1,y,x2,y2,path+[x1,y],n-1,True,hasReachPoint)
						if p!=False:
							return p
				else:break
			for y in xrange(y1+1,self.MaxHeight):#向下
				if self.GetArrayXY(x1,y)==0 and hasReachPoint[y*self.MaxWidth+x1]<n:
					if self.IsLineable(x1,y,x2,y2,1) or self.IsLineable(x1,y,x2,y2,2):
						path+=[x1,y,x2,y2]
						return path
					else:#到达不了，左右转弯，递归
						hasReachPoint[y*self.MaxWidth+x1]+=1
						p=self.IsNTurnReachable(x1,y,x2,y2,path+[x1,y],n-1,True,hasReachPoint)
						if p!=False:
							return p
				else:break
		return False

	#n连看的计算函数
	def IsLinkAble(self,x1,y1,x2,y2,n):
		if n<=0:
		  return False
		hasReachPoint=[0]*(self.MaxWidth*self.MaxHeight)
		for i in [1,2,3,4]:
			if self.IsLineable(x1,y1,x2,y2,i):
				path=[x1,y1,x2,y2]
				return path
		path=[x1,y1]
		p=self.IsNTurnReachable(x1,y1,x2,y2,path,n-1,False,hasReachPoint)
		if p:return p
		p=self.IsNTurnReachable(x1,y1,x2,y2,path,n-1,True,hasReachPoint)
		if p:return p
		return False 


if __name__ == '__main__':
	random.seed()

	# 生成障碍点
	llk = CY_LianlianKan( 10, 10 )
	llk.GenRandomArray()
	print( llk.m_Array )

	ret = llk.IsLinkAble( 0, 1, 3, 4, 3 )
	print( ret )