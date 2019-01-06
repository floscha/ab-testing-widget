# -*- coding: future_fstrings -*-
from typing import List


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


def build_treatments_html(groups: List[str],
                          conversions: List[int],
                          totals: List[int]):
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
                    <td>{groups[0]}</td>
                    <td>{conversions[0]}</td>
                    <td>{totals[0]}</td>
                    <td>{(conversions[0] / totals[0] * 100):.2f}%</td>
                </tr>
                <tr>
                    <td>{groups[1]}</td>
                    <td>{conversions[1]}</td>
                    <td>{totals[1]}</td>
                    <td>{(conversions[1] / totals[1] * 100):.2f}%</td>
                </tr>
            </tbody>
        </table>
    '''
