import os
import sys

# --- 인자값
# 1. 변경하고 싶은 폴더 경로
# 2. 넣고 싶은 문자
# 3. 자를 문자
# 4. 바꿀 문자
# 5. 확장자
path = "C:\\Users\\user\\Desktop\\ex\\"
cName = "07"
splitText = "-"
changeSplitText = "_"
extension = '.mp4'

# ex) 07-003.mp4 -> 07_03.mp4

def changeName(path, cName):
    count = 0
    for filename in os.listdir(path):
        print("\n---------------------------")
        print("[변경 전]")

        try:
            name = filename.split(splitText)[0]
            index = filename.split(splitText)[1].replace(extension, "")
            print("텍스트: " + name)
            print("중간 기호:", splitText)
            print("Index: " + index)
            print("폴더 이름:", filename)
            print("-------------------->")

            # 앞에 0을 몇 개 붙일건지 ex) test_001, test_01
            if int(index) < 10: changedIndex = "0" + str(int(index))
            else: changedIndex = "" + str(int(index))

            print("[변경 후]")
            print("텍스트: " + cName)
            print("중간 기호: " + changeSplitText)
            print("Index: " + changedIndex)
            print("최종 변경 폴더 이름: " + cName + changeSplitText + changedIndex + extension)
            print("---------------------------")

            # 변경 확인
            if count == 0:
                print("-- 최종 변경 폴더 이름을 확인해주세요.")
                print("-- 전체 변경하시겠습니까? (Y|N)")
                answer = input()
                if answer == "Y":
                    count = 1
                elif answer == "N":
                    sys.exit()
            if count == 1:
                try:
                    os.rename(path + filename, path + cName + changeSplitText + changedIndex + extension)
                    print("변경되었습니다.")
                except Exception as e:
                    print("변경되지 않았습니다.")
        except IndexError:
            print("---> 나눌 문자열이 다릅니다")

changeName(path, cName)
