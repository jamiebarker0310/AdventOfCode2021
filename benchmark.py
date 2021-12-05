import importlib
import pkgutil
import time

import matplotlib.pyplot as plt
import pandas as pd

import aoc


def benchmark(func: callable, file_path: str, N=5) -> list:

    return [time_function(func, file_path) for i in range(N)]


def time_function(func: callable, file_path: str) -> float:

    start = time.time()
    func(file_path)
    return time.time() - start


def get_modules():
    modules = [name for _, name, _ in pkgutil.iter_modules(["aoc"])]
    module_dict = {}
    for module_str in modules:
        module = importlib.import_module(f"aoc.{module_str}", package=aoc)
        func_1 = getattr(module, "part_one")
        func_2 = getattr(module, "part_two")
        file_path = f"aoc/inputs/{module_str}.txt"
        module_dict[f"{module_str}-pt1"] = (func_1, file_path)
        module_dict[f"{module_str}-pt2"] = (func_2, file_path)
    return module_dict


def run_benchmarks():

    module_dict = get_modules()

    for key, value in module_dict.items():
        module_dict[key] = benchmark(*value)

    return pd.DataFrame(module_dict)


def save_figure(df):

    df.mean().plot(figsize=(15, 10), kind="bar")
    plt.xticks(ticks=range(len(df.columns)), labels=df.columns, rotation=90)
    plt.ylabel("seconds")
    plt.yscale("log")
    return plt.savefig("benchmark.png")


if __name__ == "__main__":
    df = run_benchmarks()
    save_figure(df)
