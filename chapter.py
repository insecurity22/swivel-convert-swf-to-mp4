# -*- coding: UTF-8 -*-
import os
import re
import subprocess
import time

chapter = "2"
subchapter = "08"
subchapter_index = 18

# 변환된 파일 저장할 경로, 제한 시간
savepath = 'C:\\Users\\user\\Desktop\\workingfolder\\'
timeout = 2000

# 제외할 파일
blacklist = ['menu.swf', 'script.swf']

try:
    # chapter, subchapter 수 만큼 반복하기 위해, 폴더 파일 리스트 가져오기
    chapterpath = './' + chapter + '\\'
    list = [l for l in os.listdir(chapterpath) if os.path.isdir(os.path.join(chapterpath, l))]
    list_trimmed = [l for l in list if re.compile(r'\d').match(l)]

    while int(subchapter) <= int(list_trimmed[len(list_trimmed)-1]):

        # 경로 설정
        print("\n- 현재 chapter", chapter)
        print("- 현재 subchapter", subchapter)

        swfpath = './' + chapter + '\\' + subchapter + '\\swf\\'
        filelist = [f for f in os.listdir(swfpath) if f.endswith('.swf')]
        print("- 현재 index", filelist[subchapter_index-1])
        print("\nswf 파일이 있는 경로:", swfpath)
        print("-> swf list:", filelist)

        savepath_changed = savepath + chapter + '\\' + subchapter + '\\'
        print("mp4 파일을 저장할 경로:", savepath_changed, "\n")

        # 폴더 없으면 만들기
        if not os.path.isdir(savepath_changed):
            os.mkdir(savepath_changed)

        # 폴더 파일 리스트만큼 동영상 만들기
        count = 1
        for l in filelist:
            if not count <= subchapter_index-1:
                if l not in blacklist:
                    # Swivel 실행
                    cmd = 'Swivel.exe ' + swfpath + l.rstrip('.swf') + '.swf -o ' + savepath_changed + l.rstrip('.swf') + '.mp4 -s 1808x1166' # -sm letterbox
                    print(cmd)
                    try:
                        print(l, "저장 중")
                        proc = subprocess.Popen(cmd, shell=True)
                        proc.communicate(timeout=timeout)
                    except subprocess.TimeoutExpired:
                        print(l + ", Timeout 되었습니다.")
                        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=proc.pid))
                        time.sleep(5)
                        continue

            count += 1

        # subchapter 증가
        temp = int(subchapter) + 1
        if temp < 10:
            subchapter = "0" + str(temp)
        else:
            subchapter = str(temp)

        # 초기화
        subchapter_index = 0

except Exception as e:
    print("프로그램 실행 오류", e)


# os.system("dir /S")
