#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from pyecharts import options as opts
from pyecharts.charts import Tree

# data =  {
#             "children": [
#                 {"name": "B"},
#                 {
#                     "children": [
#                         {"children": [{"name": "I"}], "name": "E"},
#                         {"name": "F"},
#                     ],
#                     "name": "C",
#                 },
#                 {
#                     "children": [
#                         {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
#                         {"name": "H"},
#                     ],
#                     "name": "D",
#                 },
#             ],
#             "name": "A",
#         }


def render_eacharts_html(data):
    c = (
        Tree()
        .add(
            "",
            [data],
            collapse_interval=2,
            orient="TB",
            label_opts=opts.LabelOpts(
                position="top",
                horizontal_align="right",
                vertical_align="middle",
                rotate=-90,
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-上下方向"))
        .render("static/tree_bottom_top.html")
    )


if __name__ == '__main__':
    pass