# -*- coding: UTF-8 -*-
import os
import subprocess
import time

# swfPath, savePath, timeout
swfpath = './2\\01\\swf\\'
savepath = 'C:\\Users\\user\\Desktop\\workingfolder\\2\\01\\'
timeout = 2000
if not os.path.isdir(savepath):
    os.mkdir(savepath)

print("프로그램 실행")
try:
    # 폴더 파일 리스트 가져오기
    filelist = [f for f in os.listdir(swfpath) if f.endswith('.swf')]

    # 폴더 파일 리스트만큼 동영상 만들기
    for l in filelist:
        cmd = 'Swivel.exe ' + swfpath + l.rstrip('.swf') + '.swf -o '\
                + savepath + l.rstrip('.swf') + '.mp4 -sm letterbox'
        try:
            print(l, "저장 중")
            proc = subprocess.Popen(cmd, shell=True)
            proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            print(l + ", Timeout 되었습니다. 만약 인터셉트 부분이라면 swivel 프로그램을 종료 해주세요.")
            subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=proc.pid))
            time.sleep(5)
            continue

except Exception as e:
    print("프로그램 실행 오류", e)
