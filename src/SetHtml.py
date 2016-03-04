#encode:'utf-8'
'''
Created on 2016��2��17��

@author: Administrator
'''

class SetHtml:
    def __init__(self):
        self.table=''
        self.table_item=''
        self.table_head=''
        self.table_th='<table border="1">\n'
        self.table_ed='</table>'
    
    def setTableHead(self,heads):
        for i in range(len(heads)):
            self.table_head+='<th>'+heads[i]+'</th>\n'
        self.table_haed='<tr>\n'+self.table_head+'</tr>\n'
    
    def setTableItem(self,contents):
        tmp=''
        for i in range(len(contents)):
            tmp+='<td>'+contents[i]+'</td>\n'
        tmp='<tr>\n'+tmp+'</tr>\n'
        self.table_item+=tmp
    
    def setHtmlTable(self):
        self.table+=self.table_th
        self.table+=self.table_haed
        self.table+=self.table_item
        self.table+=self.table_ed
        return self.table

if __name__=='__main__':
    setHtml=SetHtml()
    setHtml.setTableHead(['col1','col2'])     
    setHtml.setTableItem(['a','b'])
    setHtml.setTableItem(['c','d'])
    result=setHtml.setHtmlTable()
    print(result)