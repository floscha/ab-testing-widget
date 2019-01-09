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


def build_treatment_rows(df: pd.DataFrame):
    table_rows = []
    for _, row in df.iterrows():
        table_rows.append(f'''
            <tr>
                <td>{row.group}</td>
                <td>{row.conversion}</td>
                <td>{row.total}</td>
                <td>{(row.conversion / row.total * 100):.2f}%</td>
            </tr>
        ''')

    return '\n'.join(table_rows)


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
                {build_treatment_rows(df)}
            </tbody>
        </table>
    '''
