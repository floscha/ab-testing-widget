from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np

from .plotting import plot_conversion_rates, plot_pairwise_differences
from .templating import build_header_html, build_summary_html
from .templating import build_treatments_html
from .util import display_html


def display_ab_test_results(groups: List[str],
                            conversions: List[int],
                            totals: List[int],
                            sample_size: int = 10000,
                            shade: bool = False,
                            figsize: Tuple[int, int] = None):
    display_html(build_header_html())

    display_html(build_summary_html())

    display_html(build_treatments_html(groups, conversions, totals))

    if figsize is None:
        figsize = (14, 4)
    plt.figure(figsize=figsize)

    binom_control = [np.random.binomial(1, conversions[0]/totals[0],
                                        totals[0]).mean()
                     for _ in range(sample_size)]
    dist_control = np.random.normal(loc=np.mean(binom_control),
                                    scale=np.std(binom_control),
                                    size=sample_size)
    binom_test = [np.random.binomial(1, conversions[1]/totals[1],
                                     totals[1]).mean()
                  for _ in range(sample_size)]
    dist_test = np.random.normal(loc=np.mean(binom_test),
                                 scale=np.std(binom_test),
                                 size=sample_size)

    plt.subplot(121)
    plot_conversion_rates(dist_control, dist_test, shade)
    plt.subplot(122)
    plot_pairwise_differences(dist_control, dist_test, shade)

    plt.show()
