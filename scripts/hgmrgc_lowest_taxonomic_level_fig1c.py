import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats


# annotation level
work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG'
this_height=250
this_width=800
uhgg_df=pd.read_csv(os.path.join(work_dir,'uhgg_annotation_gtdb202.csv'))
uhgg_df=uhgg_df[['rep','new_lineage','new_level']]
uhgg_df.columns=['Representative genome','Taxonomic label','Annotation level']
uhgg_df['Catalog']='UHGG'
uhgg_df['Annotation level'].replace({'Family':'Family/Order/Class'},inplace=True)
uhgg_df['Annotation level'].replace({'Order':'Family/Order/Class'},inplace=True)
uhgg_df['Annotation level'].replace({'Class':'Family/Order/Class'},inplace=True)

our_df=pd.read_excel(os.path.join(work_dir,'hgmrgc_annotation_gtdb202.xlsx11'))
our_df=our_df[['cluster name','taxonomic lable','annotation level']]
our_df.columns=['Representative genome','Taxonomic label','Annotation level']
our_df['Catalog']='Ours'
our_df['Annotation level'].replace({'Family':'Family/Order/Class'},inplace=True)
our_df['Annotation level'].replace({'Order':'Family/Order/Class'},inplace=True)
our_df['Annotation level'].replace({'Class':'Family/Order/Class'},inplace=True)

tdf=pd.concat([uhgg_df,our_df])
tdf=tdf[['Representative genome','Annotation level','Catalog']]

cnt_df=tdf.groupby(['Annotation level','Catalog']).count()
color_map={
    'Family/Order/Class':'#b3e6ff',
    'Genus':'#4dc3ff',
    'Species':'#0099e6'
}
cnt_df=cnt_df.reset_index()
cnt_df['Catalog']=cnt_df['Catalog'].replace({'Ours':'HGMRGC'})
cnt_df.columns=['Annotation level','Catalog','Number of representatives']
fig = px.bar(cnt_df, y="Catalog", x="Number of representatives", 
             color="Annotation level",
             text='Number of representatives',
             color_discrete_map=color_map,
                 # text_auto='.2f',
            orientation='h')
fig.update_layout(
    width=this_width,
    height=this_height,
    showlegend=True,
    template='simple_white',
    yaxis_title='',
    xaxis_title_font=dict(size=15),
    yaxis_title_font=dict(size=20),
    
    )
fig.update_traces(textfont_size=15, textangle=0, textposition="inside", cliponaxis=False)
# fig.update_layout(title_text="Annotation Level", title_x=0.5)
fig.update_yaxes(categoryorder='array', categoryarray= ['UHGG','HGMRGC'])
fig.write_image(os.path.join(work_dir,'compare2uhgg'+'.'+'Annotation'+'.pdf'),width=this_width,height=this_height,scale=2)
fig.show()