# -*- coding: future_fstrings -*-
from typing import List

import pandas as pd


def build_header_html():
    # Use H2 for cell title since H1 should be used for the notebook's title
    return '<h2>A/B Test Results</h2>'


def build_summary_rows(df: pd.DataFrame):
    control_data = df.iloc[0]
    control_name = control_data.group
    control_rate = control_data.conversion / control_data.total
    confidence = 0.97
    relative_increase = 0.096

    summary_rows = []
    for _, row in df.iloc[1:].iterrows():
        treatment_rate = row.conversion / row.total
        is_better_than_control = treatment_rate > control_rate
        summary_rows.append(f'''
            <tr>
                <td>
                    <b>{row.group}</b> converts
                    {'higher' if relative_increase > 0 else 'lower'}
                    than <b>{control_name}</b>
                </td>
                <td>
                    <span class="badge"
                          style="background:{'green' if confidence > 0.9
                                             else 'red'};">
                        {confidence * 100}%
                    </span>
                </td>
                <td>
                    <span class="badge"
                          style="background:{'green' if relative_increase > 0
                                             else 'red'};">
                        {relative_increase * 100}%
                    </span>
                </td>
            </tr>
        ''')

    return '\n'.join(summary_rows)


def build_summary_html(df: pd.DataFrame):
    return f'''
        <table width="380">
            <thead>
                <tr style="text-align: right;">
                    <th>Comparison</th>
                    <th>Confidence</th>
                    <th>Relative Increase</th>
                </tr>
            </thead>
            <tbody>
                {build_summary_rows(df)}
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
