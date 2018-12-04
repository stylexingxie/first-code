#问题是 find all 4th graders in Urban schools where is no 5th grader in their same school who has the same goal and same ranking of popularity impact factors.
#  Return each student's grade, school, and goal
import pandas as pd
#首先根据'Urban'进行筛选
df1 = pd.read_csv(r'Schoolkids.csv')
df2 = df1[(df1[u'Type']=='Urban')]
#再把'4th'and '5th'筛选出来
df3 = df2[(df2[u'Grade']==4) | (df2[u'Grade']==5)]
#根据要求，删除'Grades','Sports','Looks','Money'重复的行
df4 = df3.drop_duplicates(['Grades','Sports','Looks','Money'])
#提取出'4th'的学生，并且只输出"student's grade, school, and goal"
df5 = df4[(df2[u'Grade']==4)]
df6 = df5.drop(['Age','Type','Grades','Sports','Looks','Money'],axis=1)
#要求输出tuple,首先把DateFrame转换为list，再把list转换为tuple
list_ = df6.values.tolist()
tuple_ = tuple(list_)
print(tuple_)
