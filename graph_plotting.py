import matplotlib.pyplot as plt
import time
# # Data
# x = [1, 2, 3, 4, 5]  # X-axis values
# y = [2, 3, 5, 7, 11]  # Y-axis values

# # Plot
# plt.plot(x, y, label="Line 1", color='blue', marker='o')

# # Adding title and labels
# plt.title("Line Graph Example")
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")

# # Adding grid
# plt.grid(True)

# # Adding legend
# plt.legend()
# plt.savefig('test.png')
# # Show the plot
# plt.show()

# def plot_and_save(name):

import os

# print(files)

def plot_and_save(X,Y,Name):
    X_numeric = [float(x) for x in X]
    Y_numeric = [[float(y) for y in line] for line in Y]
    X=X_numeric
    Y=Y_numeric
    plt.plot(X, Y[0], label="Algorithm 1", color="blue", linestyle="--", marker="o")
    plt.plot(X, Y[1], label="Algorithm 2", color="red", linestyle="-.", marker="X")
    plt.plot(X, Y[2], label="Algorithm 3", color="green", linestyle=":", marker="s")
    plt.autoscale(enable=True, axis='y', tight=False)
    filename=f"Nodes = {Name[0]}, Layers = {Name[1]}, Probability_for_edge = {Name[2][:3]}"
    savename=f"Nodes_{Name[0]}_Layers_{Name[1]}_Probability_{Name[2][:3]}_"
    print(filename)
    plt.title(filename)
    plt.xlabel("Seed Set Size")
    plt.ylabel("Influence Proportion")
    # plt.autoscale()   
    # plt.ylim(0,1.0)
    plt.grid(True)
    plt.legend()
    
    plt.savefig(f"./plots_after_midsem/{savename}.png")
    plt.close()

def parser_for_name(rawName):
    rawName=rawName.split('.')
    rawName.remove(rawName[-1])
    rawName=rawName[0].split('_')
    rawName[2]=int(rawName[2])
    while rawName[2]>1:
        rawName[2]*=0.1
    print(rawName)
    rawName[2]=str(rawName[2])
    return rawName
def run(files,directory_path):
    for i in range(0,len(files)):
        file=files[i]
        path=directory_path+file
        # print(file)
        name=parser_for_name(file)
        X=[]
        Y=[[],[],[]]
        with open(path,'r') as f:
            data=f.readlines()
            nData=[]
            for line in data:
                nline=line.split('\n')
                nline.remove(nline[-1])
                nline=nline[0].split(' ')
                nline.remove(nline[-1])
                nData.append(nline)
            # print(nData)
            for line in nData:
                X.append(line[0])
                for jj in range(1,len(line)):
                    Y[jj-1].append(line[jj])
        # print(X)
        # print(Y)
        plot_and_save(X,Y,name)


def pipeline():
    directory_path="./results_after_midsem/"
    files = []
    while True:
        nfiles = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path,f))]
        a=[]
        for i in nfiles:
            if i not in files:
                a.append(i)
        files=a
        run(files,directory_path)
        files=nfiles
        time.sleep(200)

if __name__ == "__main__":

    pipeline()