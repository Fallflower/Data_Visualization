from flask import Flask, render_template, request, jsonify, Response
from pyecharts.charts import Bar
from pyecharts import options as opts
from data.loader import *
from data.illustrations import *
import json
import re

app = Flask(__name__)

## init echarts config
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
    # category = ["A", "B", "C", "D", "E"]
    # data = [5, 20, 36, 10, 75, 90]
    #
    # bar_chart = (
    #     Bar()
    #     .add_xaxis(category)
    #     .add_yaxis("y", data)
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(title="Bar-Global"),
    #     )
    # )
    #
    # chart_html = bar_chart.render_embed()

    return render_template('index.html')


@app.route('/page1', methods=['POST'])
def page1():
    selected_data = request.json.get('selectedData')
    selected_color = request.json.get('selectedColor')

    # Replace this with your actual data processing logic
    categories = ['A', 'B', 'C', 'D', 'E']
    data = [10, 20, 15, 25, 30]

    # Create a new Bar chart based on user selection
    bar_chart = (
        Bar()
        .add_xaxis(categories)
        .add_yaxis("Selected Data", data, itemstyle_opts=opts.ItemStyleOpts(color=selected_color))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar Chart"))
    )

    # Convert chart options to JSON and send back to the frontend
    chart_options = bar_chart.dump_options()
    # return jsonify(chart_options)
    return render_template('page1.html', chart_options=chart_options)


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

