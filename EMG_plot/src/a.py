import matplotlib.pyplot as plt
import pandas as pd
import os

a = input("path: ")
file = "\\teste.csv"
data_graph = pd.read_csv(a+file, sep=";", names=["idx", "signal", "ms", "sMME", "MsMME", "resultado"])
print(data_graph)
