import os
import matplotlib.pyplot as plt
from graph_plotting import parser_for_name

def map_input(files_before_midsem):
    nresults=dict()
    for files in files_before_midsem:
        name=files
        name=name.split('.')
        # name.remove(name[-1])
        fname=""
        for j in name:
            if j!=name[-1]:
                fname+=j
        fname+="."+name[-1]
        # print(fname)
        # nresults[files]=fname
        nresults[fname]=files
    # pass
    return nresults

def plot_and_save(A,B,name):
    X=[0.1,0.2,0.3,0.4,0.5,0.6]
    A=[int(j) for j in A]
    B=[int(j) for j in B]
    # print(A)
    # print(B)
    Name=parser_for_name(name)
    filename=f"Nodes = {Name[0]}, Layers = {Name[1]}, Probability_for_edge = {Name[2][:3]}"
    plt.plot(X, A, label="hops= 4 ", color="blue", linestyle="--", marker="o")
    plt.plot(X, B, label="hops= infinity", color="red", linestyle="-.", marker="X")
    plt.title(filename)
    plt.xlabel("beta fraction of total graph")
    plt.ylabel("seed set size")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"./hops_plots/{filename}.png")
    plt.close()
    pass

def run():
    one_directory="./results_after_midsem/"
    two_directory="./results/"
    files_after_midsem = [f for f in os.listdir(one_directory) if os.path.isfile(os.path.join(one_directory,f))]
    files_after_midsem=files_after_midsem
    files_before_midsem= [f for f in os.listdir(two_directory) if os.path.isfile(os.path.join(two_directory,f))]
    print(files_after_midsem[0])
    print(files_before_midsem[0])
    mapping_input=map_input(files_before_midsem)
    for f in files_after_midsem:
        print(f)
        one_full_path=one_directory+f
        # two_full_path=two_directory+mapping_input[f]
        if f in mapping_input.keys():
            two_full_path=two_directory+mapping_input[f]
        else:
            continue
        with open(one_full_path,'r') as file_one, open(two_full_path,'r') as file_two:  
            data_one=file_one.readlines()
            data_two=file_two.readlines()
            data_one=[j.split('\n')[0] for j in data_one]
            data_one=[j.split(' ')[0] for j in data_one]
            data_two=[j.split('\n')[0] for j in data_two]
            data_two=[j.split(' ')[0] for j in data_two]
            
            data_two=[data_two[j] for j in range(len(data_one))]
            # print(data_two)
            plot_and_save(data_one,data_two,f)
            # pass
        # break 

        




if __name__=="__main__":
    run()