from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .plotting import plot_conversion_rates, plot_pairwise_differences
from .templating import build_header_html, build_summary_html
from .templating import build_treatments_html
from .util import display_html


def display_ab_test_results(df: pd.DataFrame,
                            sample_size: int = 10000,
                            bootstrap_fraction: float = 0.1,
                            shade: bool = False,
                            figsize: Tuple[int, int] = None):
    if len(df) > 8:
        raise ValueError('Currently no more than 7 treatments (plus control'
                          + ' group) are supported')

    display_html(build_header_html())

    display_html(build_summary_html(df))

    display_html(build_treatments_html(df))

    if figsize is None:
        figsize = (14, 4)
    plt.figure(figsize=figsize)

    distributions = []
    for _, row in df.iterrows():
        observations = np.hstack([np.ones(row.conversion),
                                  np.zeros(row.total - row.conversion)])
        bootstrap_size = int(row.total * bootstrap_fraction)
        bootstrapped_means = [np.random.choice(observations,
                                               size=bootstrap_size,
                                               replace=True
                                               ).mean()
                              for _ in range(1000)]
        dist = np.random.normal(loc=np.mean(bootstrapped_means),
                                scale=np.std(bootstrapped_means),
                                size=sample_size)
        distributions.append((row.group, dist))

    plt.subplot(121)
    plot_conversion_rates(distributions, shade)
    plt.subplot(122)
    plot_pairwise_differences(distributions, shade)

    plt.show()
