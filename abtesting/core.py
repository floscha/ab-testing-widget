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
                            shade: bool = False,
                            figsize: Tuple[int, int] = None):
    display_html(build_header_html())

    display_html(build_summary_html())

    display_html(build_treatments_html(df))

    if figsize is None:
        figsize = (14, 4)
    plt.figure(figsize=figsize)

    distributions = []
    for _, row in df.iterrows():
        binom = [np.random.binomial(1, row.conversion / row.total,
                                    row.total).mean()
                 for _ in range(sample_size)]
        dist = np.random.normal(loc=np.mean(binom), scale=np.std(binom),
                                size=sample_size)
        distributions.append((row.group, dist))

    plt.subplot(121)
    plot_conversion_rates(distributions, shade)
    plt.subplot(122)
    plot_pairwise_differences(distributions, shade)

    plt.show()
