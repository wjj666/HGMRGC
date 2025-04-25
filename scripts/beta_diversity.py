import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

distance_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/16_beta_diversity/distance'
import plotly.graph_objs as go
this_width=800
this_height=800

def distance_box_plot(stype,title):
    # 3.discovery.snp.pairs10000.distance.csv
    dis_df=pd.read_csv(os.path.join(distance_dir,'3.'+'discovery'+'.'+stype+'.pairs10000.distance.csv'))
#     print(len(dis_df))
    dis_df=dis_df[dis_df['Distance']>0]
    
    dis_df['Cohort']='Discovery cohort'
    dis_df.columns=['Category','Distance','Cohort']
    dis_df['Category']=dis_df['Category'].replace({
        'Intra-Chinese population':'Within HC',
        'Intra-non-Chinese population':'Within NC',
        'Inter-population':'Between HC and NC'
    })
#     print(dis_df)
    
    rep_df=pd.read_csv(os.path.join(distance_dir,'3.'+'replication'+'.'+stype+'.pairs10000.distance.csv'))
    rep_df=rep_df[rep_df['Distance']>0]
    
    rep_df['Cohort']='Replication cohort'
    rep_df.columns=['Category','Distance','Cohort']
    rep_df['Category']=dis_df['Category'].replace({
        'Intra-Chinese population':'Within HC',
        'Intra-non-Chinese population':'Within NC',
        'Inter-population':'Between HC and NC'
    })
#     print(rep_df)
    
    df=pd.concat([dis_df,rep_df])
    
#     print(df)
    category_order=['Within HC','Between HC and NC','Within NC']
    colors={'Within HC':'red','Between HC and NC':'orange','Within NC':'green'}
    
    fig=px.box(df,x='Cohort',y='Distance',color='Category',
           template='simple_white',
               notched=True,
               points='outliers',
               
               category_orders={'Category': category_order},
               color_discrete_map=colors,
          # color_discrete_sequence=['green','orange','red']
          )
    
    
    fig.update_layout(
        xaxis_title='',
        yaxis_title=title+' beta diversity',
        width=this_width,
        height=this_height,
        legend_title_text='Category',
#         title_text=title,title_x=0.5,title_font=dict(size=20, color="black"),
        showlegend=True,
        legend=dict(font=dict(size=13, color="black"))
    )
    fig.update_xaxes(categoryorder='array', categoryarray= ['Discovery cohort','Replication cohort'])
#     # fig.update_yaxes(range=[0, 6])
#     # fig.update_traces(textfont_size=20, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_yaxes(tickfont_size=15)
    fig.update_xaxes(tickfont_size=20)
    fig.update_yaxes(title_font_size=20)
    fig.update_traces(marker=dict(size=3))
    fig.show()
    fig.write_image(os.path.join(beta_dir,title+'.beta.distance.pdf'),width=this_width,height=this_height,scale=2)

distance_box_plot('snp','SNP-based')
distance_box_plot('abd','Abundance-based')
