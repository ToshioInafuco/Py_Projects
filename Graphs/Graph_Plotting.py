import matplotlib.pyplot as plt
import pandas as pd

data_graph = pd.read_csv("data_read.csv", sep=";", names=["LDR", "Solo", "Temperatura", "Humidade", "Horario"])
# print(data_graph)

#https://matplotlib.org/stable/tutorials/index.html 

figure = plt.figure(figsize = (15,3))
figure.suptitle("Data Read\n")

plt.subplot(221)
plt.plot(data_graph["Horario"], data_graph["LDR"], label = "LDR", c = "k")
plt.legend()
plt.title("LDR READ")
plt.axis("auto")

plt.subplot(222)
plt.plot(data_graph["Horario"], data_graph["Solo"], label = "Solo", c = "g")
plt.legend()
plt.title("Solo READ")

figure.add_subplot(223)
plt.plot(data_graph["Horario"], data_graph["Temperatura"], label = "Temperatura", c = "r")
plt.legend()
plt.title("Temperatura READ")

figure.add_subplot(224)
plt.plot(data_graph["Horario"], data_graph["Humidade"], label = "Humidade", c = "b")
plt.legend()
plt.title("Humidade READ")

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)



plt.show()
