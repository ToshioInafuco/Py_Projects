import matplotlib.pyplot as plt
import pandas as pd

data_graph = pd.read_csv("data_read.csv", sep=";", names=["LDR", "Solo", "Temperatura", "Humidade", "Horario"])

#https://matplotlib.org/stable/tutorials/index.html 

figure = plt.figure(figsize = (17,9))#Tamanho da aba


plt.subplot(321)
plt.plot(data_graph["Horario"], data_graph["LDR"], label = "LDR", c = "k")
plt.plot(data_graph["Horario"], data_graph["Solo"], label = "Solo", c = "g")
plt.legend()
plt.title("  1  ")

plt.subplot(322)
plt.plot(data_graph["Horario"], data_graph["Temperatura"], label = "Temperatura", c = "r")
plt.plot(data_graph["Horario"], data_graph["Humidade"], label = "Humidade", c = "b")
plt.legend()
plt.title("  2  ")

plt.subplot(323)
plt.plot(data_graph["Horario"], data_graph["LDR"], label = "LDR", c = "k")
plt.plot(data_graph["Horario"], data_graph["Solo"], label = "Solo", c = "g")
plt.legend()
plt.title("  3  ")

plt.subplot(324)
plt.plot(data_graph["Horario"], data_graph["Temperatura"], label = "Temperatura", c = "r")
plt.plot(data_graph["Horario"], data_graph["Humidade"], label = "Humidade", c = "b")
plt.legend()
plt.title("  4  ")

plt.subplot(325)
plt.plot(data_graph["Horario"], data_graph["LDR"], label = "LDR", c = "k")
plt.plot(data_graph["Horario"], data_graph["Solo"], label = "Solo", c = "g")
plt.legend()
plt.title("  5  ")

plt.subplot(326)
plt.plot(data_graph["Horario"], data_graph["Temperatura"], label = "Temperatura", c = "r")
plt.plot(data_graph["Horario"], data_graph["Humidade"], label = "Humidade", c = "b")
plt.legend()
plt.title("  6  ")



# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
plt.tight_layout()
plt.show()
