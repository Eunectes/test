#-*-coding:utf-8-*-
import random,time
def character(name,capability,strength):
  print('角色：',name)
  print('能力：',capability)
  print('实力：',strength)
#角色信息
d={'卢卡尔':['纯格斗术，改造肉体',8.0],'神乐千鹤':['镜之力分身幻象等',8.1],'古利查力度':['强悍的肉体搏斗技能',8.2],'古娜':['操纵冰',8.3],\
   'ZEROO':['战袍攻击，改变磁场',8.4],'幻影草薙京':['操纵赤炎',8.5],'艾黛尔海特':['肉体格斗术',8.6],\
   '七枷社，夏米尔，克里斯':['分别为大地、雷电和火焰',8.7],'神乐双子':['镜之力分身幻象、封印之力等',8.8],\
   '暴走八神':['操纵苍焰，暴走状态',9.0],'紫苑':['中国枪法',9.2],'暴风高尼兹':['操纵风',9.4],'无界':['操纵岩石，石化之力',9.5],\
   '祸忌':['一定程度使用空间与空气，召唤异空间能量等',9.6],'大蛇':['大蛇之力',9.7],'伊格尼斯':['高科技战衣武器，操纵光',9.8],\
   '斋祀':['操纵冥炎，一定程度操纵时间',9.9],'血之螺旋疯狂艾森':['各种神力，操纵冥炎',10.0]}
print('\n想要知道拳皇中你钟爱的角色胜率如何吗？满足你 —v—\n')
print('可选角色如下：\n')
clist=list(str(key) for key in d.keys())
for i in clist:
  print('{:>2}.'.format(str(clist.index(i)))+' '*8+'{0:{1}<9}\t'.format(i,chr(12288)))
#选择角色及对手
n1=input('\n请选择你的角色：')
character(n1,d.get(n1)[0],d.get(n1)[1])
n2=input('\n请选择你的对手：')
character(n2,d.get(n2)[0],d.get(n2)[1])
#输入场次
ground=int(input('\n请输入模拟场次：'))
g=ground
start=time.perf_counter()
#对战得分
A,B=0,0
a=float('%.03f'%(d.get(n2)[1]-d.get(n1)[1]))
b=float('%.03f'%(0.5-a/20))
q='·'*12
print('{}正在模拟{}'.format(q,q))
while g>0:
  c=float('%.05f'%random.random())
  if c>b:
    B+=1
  else:
    A+=1
  #进度条
  g-=1
  w=int(50*(1-g/ground))*'-'
  e=int(50*g/ground)*'*'
  r=(1-g/ground)*100
  print('{:<6.2f}%[{}>{}]'.format(r,w,e),end='\r')  
#结果
print('\n%s胜率为%.2f%%'%(n1,(A/ground)*100))
print('%s胜率为%.2f%%'%(n2,(B/ground)*100))
print('模拟用时：{:.3f}s'.format(time.perf_counter()-start))

