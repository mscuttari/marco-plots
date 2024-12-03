import pandas as pd
import os
import sys
from compare import plot_comparisons
from config_plot import plot_configs

if __name__ == '__main__':
    # Check for command line arguments correctness.
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "config_name:csv_file...")
        exit(0)

    # Load the data.
    data = {}

    for arg in sys.argv[1:]:
        config_name = arg.split(":", 1)[0]
        data[config_name] = pd.read_csv(arg.split(":")[1])

    # Plot the graphs.
    if not os.path.isdir("plots/configs"):
        os.makedirs("plots/configs")

    if not os.path.isdir("plots/compare"):
        os.makedirs("plots/compare")

    plot_configs(data, "plots/configs")
    plot_comparisons(data, "plots/compare")
