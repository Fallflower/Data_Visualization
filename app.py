from flask import Flask, render_template, request, jsonify
from pyecharts.charts import Bar
from pyecharts import options as opts
import re

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)

