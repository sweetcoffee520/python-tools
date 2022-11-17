'''
Author: sweetcoffee qq791227132@gmail.com
Date: 2022-11-05 14:12:24
LastEditors: sweetcoffee qq791227132@gmail.com
LastEditTime: 2022-11-10 12:24:55
FilePath: /python_code/tools/plot_line.py
Github: https://github.com/sweetcoffee520
Description: 
Copyright (c) 2022 by sweetcoffee qq791227132@gmail.com, All Rights Reserved.
'''
import plotly.graph_objects as go
def plot_line(*arg,title=None,xtitle=None,ytitle=None,color=None):
    """画图,参数为元组,一对(x,y,dash_type,name),一个元组,长度可变
    Returns:
        _type_: _description_
    """
    fig = go.FigureWidget()
    if color is None:
        for i in range(len(arg)):
            if arg[i][2] == '':
                if arg[i][3] == '':
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',name=arg[i][3],showlegend=False))
                else:
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',name=arg[i][3]))
            else:
                if arg[i][3] == '':
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',line_dash = arg[i][2],name=arg[i][3],showlegend=False))
                else:
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',line_dash = arg[i][2],name=arg[i][3]))
    else:
        for i in range(len(arg)):
            if arg[i][2] == '':
                if arg[i][3] == '':
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',name=arg[i][3],line = dict(color = color[i]),showlegend=False))
                else:
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',name=arg[i][3],line = dict(color = color[i])))
            else:
                if arg[i][3] == '':
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',name=arg[i][3],line = dict(dash=arg[i][2],color = color[i]),showlegend=False))
                else:
                    fig.add_trace(go.Scatter(x = arg[i][0],y = arg[i][1],mode='lines+markers',name=arg[i][3],line = dict(dash=arg[i][2],color = color[i])))
    fig.update_layout(dict(
        title=title,
        xaxis={'title':xtitle,
            'tickfont_size':16,
            'gridwidth':1,
            'showgrid':True,
            'gridcolor':'#e0e0e0',
            'tickformat':'%Y',
            'tick0':'2005-01-01',
            'dtick':'M12',
            'ticklen':8,
            'ticks':'inside',
            'type':'date',
            'linewidth':2,
            'linecolor':'black',
            'mirror':'all',
            'spikedash': 'dash',
            },
        yaxis={'title':ytitle,
            'showgrid':True,
            'gridcolor':'#e0e0e0',
            'linewidth':2,
            'showline':True,
            'linecolor':'black',
            'ticks':'inside',
            'mirror':'all',
            'zeroline':True,
            'zerolinecolor':'#e0e0e0',
            },
        template='ggplot2',
        font_size=20,
        font_family='Arial Black',
        legend = {'xanchor':'left',
                'x':0.02,
                'yanchor':'top',
                'y':0.95,'itemwidth':30,
                'borderwidth':1,
                'bordercolor':'Black',
                },
        height = 800,
        width = 1200,
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        hovermode = 'x',
        ))
    return fig