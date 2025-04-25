import os
import json
import pandas as pd
import plotly.express as px

work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/1_Sample'

with open(os.path.join(work_dir, 'china-province.geojson'), 'r', encoding='utf-8') as f:
    china_geojson = json.load(f)

df_world = pd.read_excel(os.path.join(work_dir, 'country_count_code_scale.xlsx'))
df_china = pd.read_excel(os.path.join(work_dir, 'province_count_code.xlsx'))


# 世界地图
fig_world = px.choropleth(df_world, 
                   locations='code',
                   color='Number of samples',
                   hover_data=['country', 'count'],
                   color_discrete_sequence=['#DC4C46','#375F1B','#66B032','#9BD770','#EBF7E3']
                  )
fig_world.update_geos(landcolor='#ffffff')
# fig_world.data[0].showlegend = False

# 中国地图
fig_china = px.choropleth(df_china,
                          geojson=china_geojson,
                          locations='code',
                          color='Number of samples',
                          scope='asia',
                          hover_data=['province', 'count'],
                          color_discrete_sequence=['#6b1714','#ab2521','#da433e','#e26d69','#efaca9','#ffffff']
                         )
fig_china.update_geos(fitbounds="locations", visible=False, landcolor='#ffffff')

# 将中国地图的数据合并到世界地图中
for trace in fig_china.data:
    fig_world.add_trace(trace)

# 显示两种不同的分类数据
fig_world.update_layout(
    title={
        'text': "Number of Samples",
        'y':0.9, 
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    legend=dict(
        title="Other countries<br>China",
        itemsizing='constant',
        orientation='h',
        yanchor="bottom",
        y=0.01,  
        xanchor="right",
        x=1
    ),
    autosize=True
)
fig_world.write_image(os.path.join(work_dir, 'world_china_map.pdf'), scale=2)
# fig_world.write_image(os.path.join(work_dir, 'world_china_map.svg'), scale=2)
