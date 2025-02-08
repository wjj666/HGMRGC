import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats


# The proportion of top five phyla and other phyla
work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG'
df=pd.read_csv(os.path.join(work_dir,'phylum_cnt.csv'))
total_cnt=df['The number of species'].sum()
df['Proportion']=(df['The number of species']/total_cnt)*100
df=df.sort_values(['Proportion'],ascending=False)
df['x_phylum']='X'

import ujson
with open('/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/results_draft_wjj_V2/tree_color_dict/phylum2color.json') as f:
    phylum2color=ujson.load(f)

this_phylum_list=df['Phylum'].tolist()
print(len(this_phylum_list),len(phylum2color))
top5_phylum_list=['Firmicutes_A','Actinobacteriota','Firmicutes','Bacteroidota','Proteobacteria']
new_phylum_list=[]
new_phylum2color={}
for phylum in this_phylum_list:
    # print(phylum)
    if phylum not in top5_phylum_list:
        new_phylum2color['Others']='#778899'
        new_phylum_list.append('Others')
        # print(phylum,new_phylum2color[phylum])
    else:
        new_phylum2color[phylum]=phylum2color[phylum]
        new_phylum_list.append(phylum)
        print(phylum,new_phylum2color[phylum])

        
df['New phylum']=new_phylum_list


this_width=1000
this_height=280
fig = px.bar(df, y='x_phylum', x='Proportion', 
             color='New phylum',text='Proportion',text_auto='.2f',
             color_discrete_map=new_phylum2color
            )
# fig.update_traces(textfont_size=12, textangle=0,  cliponaxis=True)
# fig.update_traces(textposition='outside', selector=dict(type='bar')) 
fig.update_layout(
        width=this_width,
        height=this_height,
        legend_title_text='  Phylum',
        showlegend=True,
        template='simple_white',
    )
# fig.update_yaxes(showticklabels=False)
fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
fig.show()
fig.write_image(os.path.join(work_dir,'phylum_cnt.pdf'),width=this_width,height=this_height,scale=2)
