from IPython.display import display, HTML
import numpy as np
import seaborn as sns


def display_html(html: str):
    display(HTML(html))


def get_color_palette(prepend_neutral_color:bool=False):
    colors = sns.color_palette('Set1')
    if prepend_neutral_color:
        colors = colors[-1:] + colors[:-1]
    return colors
