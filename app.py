from flask import Flask, render_template
from pyecharts.charts import Bar
from pyecharts import options as opts
import re

app = Flask(__name__)


@app.route('/')
def index():
    category = ["A", "B", "C", "D", "E"]
    data = [5, 20, 36, 10, 75, 90]

    bar_chart = (
        Bar()
        .add_xaxis(category)
        .add_yaxis("y", data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Global"),
        )
    )

    chart_html = bar_chart.render_embed()

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

