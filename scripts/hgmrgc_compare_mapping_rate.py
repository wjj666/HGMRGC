import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats


# mapping rate
# external all
this_height=250
this_width=500
compare2uhgg_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG'
work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/DataPreparation/UHGG'
df=pd.read_csv(os.path.join(work_dir,'mapping_rate.comparison.csv'))
df['catalog']=df['catalog'].replace({'Ours':'HGMRGC'})

print('external all:')
ex_df=df[df['internal/external']=='external']

# print(ex_df)

ex_uhgg_df=ex_df[ex_df['catalog']=='UHGG']
ex_uhgg_df=ex_uhgg_df[['sid','mapping_rate']]
ex_uhgg_df.columns=['sid','uhgg_mapping_rate']

ex_ours_df=ex_df[ex_df['catalog']=='HGMRGC']
ex_ours_df=ex_ours_df[['sid','mapping_rate']]
ex_ours_df.columns=['sid','ours_mapping_rate']

ex_uhgg_df=ex_uhgg_df.set_index(['sid'])
ex_ours_df=ex_ours_df.set_index(['sid'])
ex_df=pd.concat([ex_uhgg_df,ex_ours_df],join='inner',axis=1)

print('mean','UHGG:',np.mean(ex_df['uhgg_mapping_rate']),'HGMRGC:',np.mean(ex_df['ours_mapping_rate']))
print('median','UHGG:',np.median(ex_df['uhgg_mapping_rate']),'HGMRGC:',np.median(ex_df['ours_mapping_rate']))
from scipy.stats import wilcoxon
res = wilcoxon(ex_df['uhgg_mapping_rate'], ex_df['ours_mapping_rate'],alternative='less')
print(res)


df=pd.read_csv(os.path.join(work_dir,'mapping_rate.comparison.csv'))
df['catalog']=df['catalog'].replace({'Ours':'HGMRGC'})
print('external all:')
ex_df=df[df['internal/external']=='external']
print(ex_df)
ex_df=ex_df[['sid','mapping_rate','catalog']]
ex_df['mapping_rate']=ex_df['mapping_rate']*100
ex_df.columns=['sid','Mapping rate','Catalog']

fig = px.box(ex_df, y="Catalog", x="Mapping rate",
                color="Catalog", 
             # box=True,
                color_discrete_map = {'UHGG': 'Green','HGMRGC': 'Red'}
                # points="all",
      )
fig.update_yaxes(categoryorder='array', categoryarray= ['UHGG','HGMRGC'])
fig.update_traces(marker=dict(size=3))
fig.update_layout(
    xaxis_title="Mapping rate (%)",
    yaxis_title="",
    width=this_width,
    height=this_height,
    showlegend=False,
    template='simple_white',
)
fig.update_yaxes(tickfont_size=15)
fig.update_xaxes(tickfont_size=12)
fig.update_yaxes(title_font_size=20)
fig.update_xaxes(title_font_size=15)
# fig.update_layout(title_text="Mapping rate", title_x=0.5)
fig.show()
fig.write_image(os.path.join(compare2uhgg_dir,'compare2uhgg'+'.mappingrate.box.pdf'),width=this_width,height=this_height,scale=2)

