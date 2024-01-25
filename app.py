from flask import Flask, render_template, request, jsonify, Response
from pyecharts.charts import Bar
from pyecharts import options as opts
from data.loader import *
from data.illustrations import *
import numpy as np
import pandas as pd
import json
import re

app = Flask(__name__)

## init echarts config
# for page1

# for page3
maps_map = {
    "cntry": country_map,
    "inst_name": None,
    "sm-field": None,
    "sm-subfield-1": None,
    "sm-subfield-2": None
}

app.config['auth_field'] = 'cntry'
app.config['topn'] = 7
app.config['field_map'] = country_map


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page1_post_data', methods=['POST'])
def page1_post_data():

    return jsonify({'success': True})


@app.route('/page1_get_data', methods=['GET'])
def page1_get_data():
    legend_list_len = 1
    legends = ['nps (ns)']
    bins = np.arange(0, 330, 30)
    xis = ['[0, 30)', '[30, 60)', '[60, 90)', '[90, 120)', '[120, 150)', '[150, 180)', '[180, 210)', '[210, 240)',
           '[240, 270)', '[270, inif)']
    df = data_loader()

    dd = {}

    for legend in legends:
        indices = np.digitize(df[legend], bins)
        res = pd.Series(indices).value_counts().sort_index().tolist()
        dd[legend] = res

    return jsonify(legend_list=legends,
                   legend_len=legend_list_len,
                   data_dict=dd,
                   xaxis_items=xis
                   )


@app.route("/page2")
def page2():
    return render_template('page2.html')


@app.route("/page3")
def page3():
    return render_template('page3.html')


@app.route("/page3_post_data", methods=['POST'])
def page3_post_data():
    field = request.form.get('field')
    topn = int(request.form.get('topn'))

    if field:
        app.config['auth_field'] = field
        app.config['field_map'] = maps_map[field]

    if topn:
        app.config['topn'] = topn

    return jsonify({'success': True})

@app.route("/page3_get_data", methods=['GET'])
def page3_get_data():

    field = app.config['auth_field']; type_name = fields_map[field]
    top = app.config['topn']; ti = 0
    field_map = app.config['field_map']

    cvc = count_by_column(field)

    others = 0
    values = []
    names = []
    if field_map:
        for i in cvc.index:
            if ti < top:
                values.append(int(cvc[i]))
                names.append(field_map[i])
            else:
                others += cvc[i]
            ti += 1
    else:
        for i in cvc.index:
            if ti < top:
                values.append(int(cvc[i]))
                names.append(i)
            else:
                others += cvc[i]
            ti += 1

    if ti > top:
        values.append(int(others))
        names.append("Others")

    data_series = []
    for v, n in zip(values, names):
        data_series.append({'value': v, 'name': n})

    return jsonify(data_type=type_name, name_list=names, data_dict=data_series)

# @app.route("/page2_data")
# def page2_data():
#     data_list = {}
#     data1 = ['公众号：Python研究者', '直达', '营销广告', '搜索引擎', '邮件营销', '联盟广告', '视频广告', '百度', '谷歌',
#              '必应', '其他']
#     data_list['data1'] = data1
#     data2 = [
#         {'value': 2000, 'name': 'Python研究者', 'selected': True},
#         {'value': 1548, 'name': '搜索引擎'},
#         {'value': 775, 'name': '直达'},
#         {'value': 679, 'name': '营销广告'}
#     ]
#     data_list['data2'] = data2
#     data3 = [
#         {'value': 1048, 'name': '百度'},
#         {'value': 335, 'name': '直达'},
#         {'value': 310, 'name': '邮件营销'},
#         {'value': 251, 'name': '谷歌'},
#         {'value': 234, 'name': '联盟广告'},
#         {'value': 147, 'name': '必应'},
#         {'value': 135, 'name': '视频广告'},
#         {'value': 102, 'name': '其他'}
#     ]
#     data_list['data3'] = data3
#     return Response(json.dumps(data_list), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)

