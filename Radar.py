from pyecharts import Radar #导入Radar库/Import the Radar library
import webbrowser #导入webbrowser库/Import the webbrowser library
import os #导入os库/Import the os library

mao_schema = [ #创建列表/Create a list
    {"name": "属性1","max":500},
    {"name": "属性2","max": 500},

    {"name": "属性3","max": 500}
]
chart = Radar("例子") #以赋值的方式，命名+创建
chart.config(c_schema= mao_schema)
chart.add("例子",[[200 , 300 , 500]])
chart.render()
webbrowser.open("file://"+os.path.realpath("render.html"))