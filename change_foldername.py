import os
import sys
import re

# 그림2 -> video2
# 그림-2 -> video_2

path = "C:\\Users\\d0rk\\Desktop\\ex\\"
oName = "그림"
cName = "video"
oMiddleText = ""
cMiddleText = "_"
oExtension = ".mp4"
cExtension = ".mp3"

# --- 인자값
# 1. 이름을 변경하고 싶은 폴더 경로
# 2. 원본 문자         ex) 그림
# 3. 변경할 문자       ex) video
# 4. 원본 중간 문자     ex) video_2의 경우, _
# 5. 변경할 중간 문자   ex) video-2로 변경하고 싶다면 -
# 6. 원본 확장자    
# 7. 변경할 확장자     
# --> 원본과 변경할 확장자가 같을 경우, 같게 입력

def changeName(path, cName):
    count = 0
    for filename in os.listdir(path):

        # 확장자가 다르면 변경할 파일에서 제외\
        if re.findall("\.[a-zA-Z0-9]*", filename)[0] != oExtension:
            continue

        try:
            print("----------------------------")
            print("[변경 전]")
            print("폴더 이름:", filename)

            print("----------------------")
            print("[변경 후]")

            # 중간에 구분하는 문자가 없을 때. ex) 그림2
            if oMiddleText == "":
                index = re.findall("[\d*]\.", filename)[0].replace(".", "")
                if cMiddleText == "":
                    print("폴더 이름:", cName + index + cExtension)
                else: # 구분할 문자 추가
                    print("폴더 이름:", cName + cMiddleText + index + cExtension)

            # 중간에 구분하는 문자가 있을 때. ex) 그림-2
            else:
                index = filename.split(oMiddleText)[1].replace(oExtension, "")
                print("폴더 이름:", cName + cMiddleText + index + cExtension)
            print("----------------------------")

            # 만약 그림2 -> 그림02로 바꾸고 싶다면 index 앞에 "0"을 넣으면 된다.
            # ex) print("폴더 이름:", cName + cMiddleText + "0" + index + cExtension)

            # 변경 확인
            if count == 0:
                print("\n-- 바로 위, 변경 후 폴더 이름을 확인해주세요.")
                print("-- 전체 변경하시겠습니까? (Y|N|E)")
                print("-- 만약 프로그램을 종료하고 싶으시다면 E를 입력해주세요.")
                answer = input()
                if answer == "Y": count = 1
                elif answer == "N":
                    continue
                elif answer == "E": sys.exit()
            if count == 1:
                try:
                    if oMiddleText == "":
                        if cMiddleText == "": os.rename(path+filename, path+cName+index+cExtension)
                        else: os.rename(path+filename, path+cName+cMiddleText+index+cExtension)
                    else:
                        os.rename(path+filename, path+cName+cMiddleText+index+cExtension)
                    print("변경되었습니다.\n")
                except Exception as e:
                    print("변경되지 않았습니다.\n")

        except Exception as e:
            print("---> 변경할 수 없습니다.")
            print("----------------------------\n")

if __name__=="__main__":

    print("\n---- 입력 값 확인 ----")
    print("폴더 경로:", path)
    print("원본 문자:", oName)
    print("바꿀 문자:", cName)
    print("---------------------\n")

    changeName(path, cName)
