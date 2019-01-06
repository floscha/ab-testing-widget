import matplotlib.pyplot as plt
import seaborn as sns


def plot_conversion_rates(dist_control, dist_test, shade: bool = False):
    plt.title('Comparison of conversion rates')
    sns.kdeplot(dist_control, shade=shade, label='control')
    sns.kdeplot(dist_test, shade=shade, label='test')
    plt.xlabel('conversion rate')


def plot_pairwise_differences(dist_control, dist_test, shade: bool = False):
    plt.title('Pairwise differences in conversion rates')
    sns.kdeplot(dist_test - dist_control, shade=shade, label='test - control')
    plt.xlabel('difference in conversion rate')
