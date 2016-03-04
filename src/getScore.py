#encode:'utf-8'

'''
Created on 2016��2��13��

@author: Administrator
'''
import re

#获取学生的分数信息
class GetScore:
    __item_dict={}
    
    def __init__(self):
        self.get_scorePattern=re.compile(r'(?<=<td>)[^<].*?(?=</td>)', re.S)
    
    #提取学生所选的所有科目，返回关键字为科目名的字典
    def getAllSubjects(self,page):
        pattern=re.compile('(?<=<td style="text-align:left;padding-left: 6px">)(.+?)(?=</td>)', re.S)
        subjects=re.findall(pattern,page)
        if subjects:
            for i in subjects:
                self.__item_dict[i]=None
        else:
            print('find subjects error')
        #print(self.__item_dict)
    
    #需要提取的学科名    
    def setKeyWord(self,word):
        item_pattern=re.compile(word+'</td>(.+?)</tr>', re.S)
        return item_pattern
    
    #获得预设好的科目的分数
    def getAllScores(self,page):
        for i_key in self.__item_dict:
            pattern=self.setKeyWord(i_key)
            result=re.search(pattern, page)
            score=re.findall(self.get_scorePattern, result.group())
            self.__item_dict[i_key]=score
        return self.__item_dict
    
    #从本地文本中读取，方便进行测试
    def test(self,path='..//成绩capture.html'):
        with open(path,'r',encoding='utf-8') as f:
            page=f.read()
            return page
    
if __name__=='__main__':
    getScore=GetScore()
    page=getScore.test()
    getScore.getAllSubjects(page)
    result=getScore.getAllScores(page)
    print(result)
            