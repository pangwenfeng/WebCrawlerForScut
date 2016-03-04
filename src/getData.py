#encode:'utf-8'

'''
Created on 2016��2��13��

@author: Administrator
'''

import re 

#获取学生的基本信息
class GetBasicData:
    
    __item_dict={'学号':None,'姓名':None,'性别':None,'民族':None,'证件号码':None}
    
    def __init__(self):
        self.value_pattern=re.compile(r'(?<=value=")(.+?)(?=")',re.S)#获取学生信息标签所对应的值
   
    #粗定位，定位对应的标签
    def setKeyWord(self,word):
        item_pattern=re.compile(r'<td class="text_td"\s*?><span>'+word+'(.*?)/>',re.S)#查找对应的标签
        #print(item_pattern)
        return item_pattern
    
    #在字典中添加想知道的标签
    def setItem(self,key_word):
        if key_word  not in self.__item_dict:
            self.__item_dict[key_word]=None
    
    #获取对应标签的目标值
    def getMessageData(self,page,pattern):
        match=re.search(pattern,page)
        if match:
            #print(match.group())
            result=re.search(self.value_pattern,match.group()).group()
            return result
        else:
            print("target not find")
            
    #获取字典上的标签所对应的值        
    def getAllBasicMessage(self,page):
        for i in self.__item_dict.keys():
            pattern=self.setKeyWord(i)
            result=self.getMessageData(page, pattern)
            if result:
                self.__item_dict[i]=result
            else:
                print('final target not find')
        return self.__item_dict
             
    #从本地文本中读取，方便进行测试
    def test(self,path='..//capture学生信息.html'):
        with open(path,'r',encoding='utf-8') as f:
            page=f.read()
            return page
            
if __name__=='__main__':
    getData=GetBasicData()
   
    #加载用于测试的文本
    page=getData.test()
    
#     pattern=getData.setKeyWord('性别')
#     result=getData.getMessageData(page, pattern)
#     if result:
#         print(result.group())
#     else:
#         print('final target not find')
    
    #result=getData.getAllBasicMessage()
    getData.setItem('出生日期')
    result=getData.getAllBasicMessage(page)
    print('the message is \n',result)
    
   
    