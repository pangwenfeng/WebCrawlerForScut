#encode:utf-8
'''
Created on 2016��2��13��

@author: Administrator
'''

import urllib as ul
import http.cookiejar as co
#import http as ht
#import re

#该类主要负责登陆主页面，下载验证码，凭账号登陆等操作
class HomePage:
    def __init__(self):
        self.homeurl='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/login.jsp'#主页面的url
        self.studentBMUrl='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/xjgl/xjxx/yjsjbxx.do'
        self.scoreUrl='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/pygl/cjgl/cjcx.do'
        
        self.cookies=co.CookieJar()#爬虫的cookie
        self.validateCode=None#登陆的验证码
        #self.postdata=ul.parse.urlencode({'mode':'db','j_username':'201520109260',
        #                                  'j_password':'920815_pang','validateCode':self.validateCode})
        self.opener=ul.request.build_opener(ul.request.HTTPCookieProcessor(self.cookies))#简历opener
    
    #得到指定页面的html
    #url 指定的路径
    def getPage(self,url):
        request=ul.request.Request(url=url)
        res=self.opener.open(request)
        #print(res.read().decode('utf-8'))
        return (res.read().decode('utf-8'))
    
    #下载验证码的图片
    def getValidateCode(self,path='.\\val00.jpg'):
        self.validatUrl='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/captcha.do'#下载验证码的url
        request=ul.request.Request(url=self.validatUrl)
        img_data=self.opener.open(request)
        
        with open(path,'wb') as img:#将验证码以jpg格式下载到指定路径
            img.write(img_data.read())
    
    #获取账号对应的证件照    
    def getPhoto(self,path='.\\ID_Photo.jpg',num='201520109260'):
        self.photo_url='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/photo.widgets?handler=yjsPhotoHandler&value='+num+'.jpg&bh='+num
        
        request=ul.request.Request(url=self.photo_url,headers=self.headers)
        img_data=self.opener.open(request)
        
        with open(path,'wb') as img:#将证件照以jpg格式下载到指定路径
            img.write(img_data.read())
       
    
    #使用学号、密码、验证码登陆（需要改写为更智能的人机交互模式）
    def Login(self):
        self.validateCode=input('please input the validatecode: ')#手动输入验证码
        print('you input: ',self.validateCode)
        
        self.loginUrl='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/j_spring_ids_security_check'
        self.headers = { 'User-Agent' : ("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1;"
                                    "WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729;" 
                                    ".NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.3") }#模仿浏览器
        self.postdata=ul.parse.urlencode({'mode':'db','j_username':'201520109260',#输入学号，验证码
                                         'j_password':'920815_pang','validateCode':self.validateCode}).encode('utf-8')
        request=ul.request.Request(url=self.loginUrl,data=self.postdata,headers=self.headers)
        res=self.opener.open(request)
        
        return(res.read().decode('utf-8'))
    
    #返回学生基本信息
    def getStudentBasicMessage(self):
        return self.getPage(self.studentBMUrl)
    
    #返回学生的成绩
    def getScore(self):
        return self.getPage(self.scoreUrl)
    
    def collectValidateImg(self,path='.\\'):
        for num in range(200):
            self.photo_url='http://yjsjy.1yd3.cas.scut.edu.cn/ssfw/captcha.do?'+str(num)        
            request=ul.request.Request(url=self.photo_url)
            try:
                img_data=self.opener.open(request)
                print('loading'+str(num))
            except ul.error as e:
                print(e.reason,str(num)+'fail')
                continue
            with open(path+'\\'+str(num)+'.jpg','wb') as img:#将证件照以jpg格式下载到指定路径
                img.write(img_data.read())
             
if __name__=='__main__':
    hp=HomePage()
    #print('get homepage')
    hp.getPage(hp.homeurl)
    #print('get validatecode')
    #hp.getValidateCode()
    #print('get the valiadecode')
    #hp.Login()
    #print(hp.getStudentBasicMessage())
    #hp.getPhoto()
    
    hp.collectValidateImg(path='.\\validate_img')