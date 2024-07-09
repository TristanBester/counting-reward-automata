import matplotlib.pyplot as plt
import numpy as np


def plot_results(rewards, labels, window=250):
    for reward, label in zip(rewards, labels):
        arr_smoothed = np.convolve(reward, np.ones(window) / window, mode="valid")
        plt.plot(range(len(arr_smoothed)), arr_smoothed, label=label)

    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.legend()
    plt.show()


def plot_conv_results(results):
    for name, result in results.items():
        plt.plot(range(len(result)), result, label=name)

    plt.yscale("log")
    plt.legend()
    plt.show()
