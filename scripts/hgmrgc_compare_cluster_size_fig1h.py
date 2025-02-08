import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats




# cluster size 
this_height=250
this_width=500
work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG'

ours_df=pd.read_csv(os.path.join(work_dir,'hgmrgc_cluster_size.csv'))
uhgg_df=pd.read_excel(os.path.join(work_dir,'uhgg_cluster_size.xlsx'))

ours_sizes=ours_df[['Number of Non-redundant Genomes']]
ours_sizes['Catalog']='HGMRGC'
ours_sizes.columns=['Cluster size','Catalog']

uhgg_sizes=uhgg_df[['Number of genomes (non-redundant)']]
uhgg_sizes['Catalog']='UHGG'
uhgg_sizes.columns=['Cluster size','Catalog']
tdf=pd.concat([ours_sizes,uhgg_sizes])

uhgg_clen=uhgg_df['Number of genomes (non-redundant)'].tolist()
ours_clen=ours_df['Number of Non-redundant Genomes'].tolist()
stat,p_value = stats.mannwhitneyu(uhgg_clen,ours_clen,alternative='less')
print('cluster size:',p_value)
print('mean:',np.mean(uhgg_clen),np.mean(ours_clen))
print('median:',np.median(uhgg_clen),np.median(ours_clen))



fig = px.histogram(tdf, x="Cluster size", color="Catalog", 
#                    marginal="box", # can be `box`, `violin`,'rug'
                   # log_x=True, 
                   log_y=True,
                   nbins=100,
                   barmode="overlay",
                   category_orders=dict(Catalog=['HGMRGC', 'UHGG']),
                   color_discrete_sequence=['red','green'],
                )
fig.update_layout(
    xaxis_title="Cluster size",#Number of non-redundant genomes in the cluster
    yaxis_title="Count",#Number of clusters
        width=this_width,
        height=this_height,
        showlegend=True,
        template='simple_white',
    )

fig.update_yaxes(title_font_size=15)
fig.update_xaxes(title_font_size=15)
      
# fig.update_layout(title_text="Cluster size", title_x=0.5)
fig.write_image(os.path.join(work_dir,'compare2uhgg'+'.'+'cluster_size'+'.pdf'),width=this_width,height=this_height,scale=2)
fig.show()
