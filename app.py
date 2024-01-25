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
app.config['legend_list'] = ['nps (ns)']
# for page2
app.config['fields_list'] = ['sm-field-frac']

colors_dict = {
    'sm-field-frac': {'0':'rgb(128, 255, 165)','1':'rgb(1, 191, 236)'},
    'sm-subfield-1-frac': {'0':'rgb(0, 221, 255)','1':'rgb(77, 119, 255)'},
    'sm-subfield-2-frac': {'0':'rgb(255, 0, 135)','1':'rgb(135, 0, 157)'},
}
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
    legend_list = request.form['selectedOptions'].split(',')
    if legend_list == ['']:
        legend_list = []
    app.config['legend_list'] = legend_list

    return jsonify({'success': True})


@app.route('/page1_get_data', methods=['GET'])
def page1_get_data():

    legends = app.config['legend_list']
    legend_list_len = len(legends)

    bins = np.arange(0, 300, 30)
    df = data_loader()

    dd = {}

    for legend in legends:
        indices = np.digitize(df[legend], bins)
        res = pd.Series(indices).value_counts().sort_index().tolist()
        dd[fields_map[legend]] = res

    return jsonify(legend_list=[fields_map[i] for i in legends],
                   legend_len=legend_list_len,
                   data_dict=dd
                   )


@app.route("/page2")
def page2():
    return render_template('page2.html')


@app.route("/page2_post_data", methods=['POST'])
def page2_post_data():
    fields_list = request.form['selectedOptions'].split(',')
    if fields_list == ['']:
        fields_list = []
    app.config['fields_list'] = fields_list
    return jsonify({'success': True})


@app.route("/page2_get_data", methods=['GET'])
def page2_get_data():

    bins = np.linspace(0, 1, 50, endpoint=False)

    fields_list = app.config['fields_list']

    df = data_loader()
    dd = {}
    for field in fields_list:
        dd[fields_map[field]] = {}
        indices = np.digitize(df[field], bins)
        vc_res = pd.Series(indices).value_counts()
        res = np.zeros(50, dtype=int)
        for i in vc_res.index:
            res[i - 1] = vc_res[i]
        dd[fields_map[field]]['data'] = res.tolist()
        dd[fields_map[field]]['color'] = colors_dict[field]

    return jsonify(
        fields_list=[fields_map[i] for i in fields_list],
        fields_len=len(fields_list),
        data_dict=dd,
        xis=[str(i) for i in bins]
    )


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


if __name__ == '__main__':
    app.run(debug=True)

