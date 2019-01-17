# -*- coding: future_fstrings -*-
import matplotlib.pyplot as plt
import seaborn as sns

from .util import get_color_palette


def plot_conversion_rates(distributions, shade: bool = False):
    plt.title('Comparison of conversion rates')
    colors = get_color_palette(prepend_neutral_color=True)
    for color, (group, dist) in zip(colors, distributions):
        sns.kdeplot(dist, shade=shade, label=group, color=color)
    plt.xlabel('conversion rate')


def plot_pairwise_differences(distributions, shade: bool = False):
    plt.title('Pairwise differences in conversion rates')
    control_name, control_dist = distributions[0]
    colors = get_color_palette()
    for color, (group, dist) in zip(colors, distributions[1:]):
        sns.kdeplot(dist - control_dist, shade=shade, color=color,
                    label=f'{group} - {control_name}')
    plt.xlabel('difference in conversion rate')
