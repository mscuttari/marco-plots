import pandas as pd
import matplotlib.pyplot as plt
import os

def collect_all_variables(configs_data: dict) -> list:
    variables = []

    for config in configs_data:
        csv = configs_data[config]

        for name in csv.columns.values:
            if name != "time" and name not in variables:
                variables.append(name)

    variables.sort()
    return variables

def plot_comparisons(configs: dict, path: str):
    variables = collect_all_variables(configs)

    for variable in variables:
        plt.figure(figsize=(8, 6))

        for config in configs:
            csv = configs[config]

            if variable in csv.columns.values:
                x_values = csv.iloc[:, 0]
                y_values = csv[variable]
                plt.plot(x_values, y_values, label=config, marker='o')

        plt.title(variable)
        plt.xlabel("time")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(path, variable + ".png"))
