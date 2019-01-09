import matplotlib.pyplot as plt
import seaborn as sns


def plot_conversion_rates(distributions, shade: bool = False):
    plt.title('Comparison of conversion rates')
    for group, dist in distributions:
        sns.kdeplot(dist, shade=shade, label=group)
    plt.xlabel('conversion rate')


def plot_pairwise_differences(distributions, shade: bool = False):
    plt.title('Pairwise differences in conversion rates')
    control_name, control_dist = distributions[0]
    for group, dist in distributions[1:]:
        sns.kdeplot(dist - control_dist, shade=shade,
                    label=f'{group} - {control_name}')
    plt.xlabel('difference in conversion rate')
