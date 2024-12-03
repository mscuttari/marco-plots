import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_configs(configs: dict, path: str):
    for config in configs:
        csv = configs[config]
        plt.figure(figsize=(8, 6))
        plt.title(config)
        plt.xlabel("time")

        for variable in csv.columns.values:
            if variable == "time":
                continue

            plt.plot(csv["time"], csv[variable], label=variable, marker='o')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(path, config + ".png"))
