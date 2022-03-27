from pyecharts import Radar #导入Radar库/Import the Radar library
import webbrowser #导入webbrowser库/Import the webbrowser library
import os #导入os库/Import the os library

mao_schema = [ #创建列表/Create a list
    {"name": "属性1","max":500},
    {"name": "属性2","max": 500},

    {"name": "属性3","max": 500}
]
chart = Radar("例子") #以赋值的方式，命名+创建/In the way of assignment, name + create
chart.config(c_schema= mao_schema)#设置？？？（作者忘记了）/Set up??? (The author forgot)
chart.add("例子",[[200 , 300 , 500]])#对数据进行传递，注意是列表格式（嵌套）/Pass the data, noting that it is in a list format (nested)
chart.render()#对图表进行渲染/Renders the chart
webbrowser.open("file://"+os.path.realpath("render.html")) #以网页形式打开，！！！需要导入webbrowser库和os库/Open as a webpage,!!! You need to import the webbrowser library and the os library
