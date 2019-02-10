import glob
from slacker import Slacker
import pandas as pd

#슬랙 token은 채널마다 다르다.
# 파일 Path도 경로에 맞게 지정해야한다.
slack_token = ''
flist = glob.glob('')
slack = Slacker(slack_token)

dictionary_list = []

for fpath in flist:
    folder , name = os.path.split(fpath)
    head, tail = os.path.splitext(name)
    table_name = head.split('.')[0]
    a = dict()
    a["TABLE"] = table_name
    with open(fpath,'r') as f:
        #파일의 각 row에 찾는 문장이 있는지 확인 후 숫자 추출.
        for line in f.readlines():    
            if "Rows not loaded due to data errors." in line:
                a["ERROR"] = [int(s) for s in line.split() if s.isdigit()][0]
            elif "Rows successfully loaded." in line:
                a["SUCCESS"] = [int(s) for s in line.split() if s.isdigit()][0] 
            elif "Total logical records read:" in line :
                a["TOTAL"] = [int(s) for s in line.split() if s.isdigit()][0]
    dictionary_list.append(a)
            
df1=pd.DataFrame(dictionary_list,columns=["TABLE","TOTAL","SUCCESS","ERROR"])

#메세지 포맷 정리.
message_list = []
for i in df1.index:
    title = "Table: {0}".format(df1.loc[i,'TABLE']) 
    text = """Total Records : {0}\n Success Rows : {1}\nData Errors : {2} """.format(df1.loc[i,'TOTAL'],df1.loc[i,'SUCCESS'],df1.loc[i,'ERROR'])
    message = {"fallback":"Required plain-text summary of the attachment."
           ,"title":title
           ,"text":text
           ,"color":"#2b886"}
    message_list.append(message)

#채널명, Title, 메세지.
slack.chat.post_message('#blockchain','KG제로인 배치수행 결과',attachments=message_list)