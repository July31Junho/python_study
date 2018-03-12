import os
import glob
import time

fpath = 'D:\\'

# 시간을 알아내기
t= time.localtime(time.time())
print(t.tm_year)

# 경로에 있는 .zip파일 찾아내기
for curdir, dirs, files in os.walk(fpath):
    for fname in files:
        fpath = os.path.join(curdir,fname)
        if fpath.lower().endswith('.zip'):
            print(fpath)




