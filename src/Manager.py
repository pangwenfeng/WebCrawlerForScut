#encode:'utf-8'
'''
Created on 2016��2��17��

@author: Administrator
'''
import getHomePage as gh
import getData as gd
import getScore as gs
import SetHtml as sh
import SendEmail as se

if __name__=='__main__':
    #获取主页并登陆
    hp=gh.HomePage()
    hp.getPage(hp.homeurl)
    hp.getValidateCode()
    hp.Login()
    
    #登陆学生信息页并获取学生信息
    page=hp.getStudentBasicMessage()
    getData=gd.GetBasicData()
    result_message=getData.getAllBasicMessage(page)
    print('the message is \n',result_message)
    
    #登陆学生分数页并获取分数
    page=hp.getScore()
    getScore=gs.GetScore()
    getScore.getAllSubjects(page)
    result_score=getScore.getAllScores(page)
    print('the score is \n',result_score)
    
    #将相关的信息准变为html
    setHtml=sh.SetHtml()
    setHtml.setTableHead(list(result_message.keys()))     
    setHtml.setTableItem(list(result_message.values()))
    #setHtml.setTableHead(list(result_score.keys()))   
    #setHtml.setTableItem(list(result_score.values()))
    result_html=setHtml.setHtmlTable()
    print('html result',result_html)
    
    #发送相应的html到指定的邮箱
    sendEmail=se.SendEmail('pang_6170504@sina.com','9208150016','448680688@qq.com','smtp.sina.com')
    content=result_html
    sendEmail.setHeader('pang', 'feng', 'Student Message',content)
    sendEmail.send()
    
    