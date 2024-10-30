# week10_05.py
import os
target_path = "c:\\202444066"
target_file = "jeondoheon02.txt"

if False == os.path.exists(target_path):
    print("폴더생성"+target_path)
    os.mkdir(target_path)

target_fullfile = target_path + "\\" + target_file

scores=[]
if os.path.exists(target_fullfile):
    with open(target_fullfile,'r') as f:
        lines = f.readlines()
        for line in lines:
            #print(line.split())
            score=line.strip().split('|')
            #print(score)
            #['math,1','kor,2','eng,3']
            dict_scores={}
            
            for values in score:
                value = values.split(',')
                #print(value)
                if 2==len(value):
                    sub = value[0]  # 과목명
                    s = int(value[1])  # 점수
                    dict_scores[sub] = s
            if dict_scores:
                scores.append(dict_scores)
    print(scores)
else:
    f=open(target_fullfile,'w')
    f.close()
