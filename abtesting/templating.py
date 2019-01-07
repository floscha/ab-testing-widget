# -*- coding: future_fstrings -*-
from typing import List

import pandas as pd


def build_header_html():
    # Use H2 for cell title since H1 should be used for the notebook's title
    return '<h2>A/B Test Results</h2>'


def build_summary_html():
    return '''
        <table width="380">
            <thead>
                <tr style="text-align: right;">
                    <th>Comparison</th>
                    <th>Confidence</th>
                    <th>Relative Increase</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>test</b> converts higher than <b>control</b></td>
                    <td>
                        <span class="badge" style="background:green;">
                            97%
                        </span>
                    </td>
                    <td>
                        <span class="badge" style="background:green;">
                            9,6%
                        </span>
                    </td>
                </tr>
            </tbody>
        </table>
    '''


def build_treatments_html(df: pd.DataFrame):
    return f'''
        <table width="380">
            <thead>
                <tr style="text-align: right;">
                    <th>Group</th>
                    <th>Conversion</th>
                    <th>Total</th>
                    <th>Observed Rate</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>{df.groups.iloc[0]}</td>
                    <td>{df.conversions.iloc[0]}</td>
                    <td>{df.totals.iloc[0]}</td>
                    <td>{(df.conversions.iloc[0] / df.totals.iloc[0] * 100):.2f}%</td>
                </tr>
                <tr>
                    <td>{df.groups.iloc[1]}</td>
                    <td>{df.conversions.iloc[1]}</td>
                    <td>{df.totals.iloc[1]}</td>
                    <td>{(df.conversions[1] / df.totals[1] * 100):.2f}%</td>
                </tr>
            </tbody>
        </table>
    '''
