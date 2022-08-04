import matplotlib.pyplot as plt
import pandas as pd
import os

path_data = "C:\\Users\\inafu\\OneDrive\\Área de Trabalho\\Git\\Py_Projects\\EMG_plot\\data\\"
path_savfig = "C:\\Users\\inafu\\OneDrive\\Área de Trabalho\\Git\\Py_Projects\\EMG_plot\\img\\"
def plot_graph(file):
    data_graph = pd.read_csv(path_data+file, sep=";", names=["idx", "signal", "ms", "sMME", "MsMME", "resultado"])
    
    figure = plt.figure(figsize = (17,9))
    
    aux = []
    for i in range(0, len(data_graph["signal"])):
        aux.append(i)

    plt.subplot(321)
    plt.plot(aux, data_graph["signal"], label = "Sinal", c = "k")
    plt.legend()
    plt.title("  1  ")

    plt.subplot(322)
    plt.plot(aux, data_graph["ms"], label = "Modulo do sinal", c = "k")
    plt.legend()
    plt.title("  2  ")

    plt.subplot(323)
    plt.plot(aux, data_graph["sMME"], label = "Sinal + MME", c = "k")
    plt.legend()
    plt.title("  3  ")

    plt.subplot(324)
    plt.plot(aux, data_graph["MsMME"], label = "Modulo do sinal + |MME|", c = "k")
    plt.legend()
    plt.title("  4  ")

    plt.subplot(325)
    plt.plot(aux, data_graph["signal"], label = "Sinal", c = "k")
    plt.plot(aux, data_graph["resultado"], label = "Resultado", c = "r")
    plt.legend()
    plt.title("  5  ")

    plt.subplot(326)
    plt.plot(aux, data_graph["ms"], label = "Módulo do sinal", c = "k")
    plt.plot(aux, data_graph["resultado"], label = "Resultado", c = "r")
    plt.legend()
    plt.title("  6  ")

    plt.subplots_adjust(top=0.95, bottom=0.05, left=0.10, right=0.95, hspace=0.30,wspace=0.40)

    plt.savefig(path_savfig+file.replace("csv", "png"), format='png')
    print(file)


files = os.listdir("C:\\Users\\inafu\\OneDrive\\Área de Trabalho\\Git\\Py_Projects\\EMG_plot\\data\\")
csv_files = []
for target_file in files:
    if(".csv" in target_file):
        csv_files.append(target_file)

for file in csv_files:
    plot_graph(file)