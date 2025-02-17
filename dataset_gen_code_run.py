import random


def generate_input(layers,p,n):
    N=n
    filename="./datasets/"+str(n)+"_"+str(layers)+"_"+str(p)+".dataset"
    file=open(filename,'w')
    # print(N," ",1)
    file.write(f"{N} {layers}\n")
    edg=[]
    

    for iter in range(layers):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if random.random()>=1-p and i!=j:
                    edg.append([i,j,random.random()])

        # print(len(edg))
        file.write(str(len(edg))+"\n")
        for i in range(1,N+1):
            # print(i," ",random.random())
            line=str(i)+" "+str(random.random())+"\n"
            file.write(line)

        for i in range(len(edg)):
            # print(edg[i][0]," ",edg[i][1]," ",edg[i][2])
            line=str(edg[i][0])+" "+str(edg[i][1])+" "+str(edg[i][2])+"\n"
            file.write(line)
    file.close()

import subprocess as sbp
# for i in range(400, 600, 100):
#     for j in range(1,3):
#         p=0.4
#         p-=0.1
#         while p>=0.1:
#             # if p>=0.6:
#             #     p-=0.1
#             #     continue
#             # generate_input(j,p,i)
#             filename="./datasets/"+str(i)+"_"+str(j)+"_"+str(p)+".dataset"
#             rfile="./results_after_midsem/"+str(i)+"_"+str(j)+"_"+str(p)+".out"
            # with open(filename, 'r') as infile, open(rfile, 'w') as outfile:
            #     sbp.run(['./a.exe'], stdin=infile, stdout=outfile, text=True)
#             p-=0.1

import os
directory_path="./datasets/"
files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
# print(files)
for i in range(24,len(files)):
    dataset=files[i]
    infile="./datasets/"+dataset
    name=dataset
    name=name.split('.')
    curname=""
    for j in range(0,len(name)-1):
        curname+=name[j]
    outfile="./results_after_midsem/"+curname+".out"
    print(curname)
    with open(infile, 'r') as infile, open(outfile, 'w') as outfile:
        sbp.run(['./a.exe'], stdin=infile, stdout=outfile, text=True)
    print(files[24])