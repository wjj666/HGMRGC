import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats


tax_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/0_tax'
with open(os.path.join(tax_dir,'sp2family.json')) as f:
    sp2family=ujson.load(f)
with open(os.path.join(tax_dir,'sp2phylum.json')) as f:
    sp2phylum=ujson.load(f)
with open(os.path.join(tax_dir,'sp2genus.json')) as f:
    sp2genus=ujson.load(f)
with open(os.path.join(tax_dir,'sp2tax.json')) as f:
    sp2tax=ujson.load(f)
with open(os.path.join(tax_dir,'sp2species.json')) as f:
    sp2species=ujson.load(f)
with open(os.path.join(tax_dir,'sp2class.json')) as f:
    sp2class=ujson.load(f)
with open(os.path.join(tax_dir,'sp2order.json')) as f:
    sp2order=ujson.load(f)

df=pd.read_csv(os.path.join('/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/17_prevalence','prevalence_species_126.csv'))

df=df[['species','direction']]
df['family']=df['species'].replace(sp2family)

## 画出分布图
def tax_barplot(this_df,tax,this_width,this_height):
    
    if tax=='Phylum':
        tax_dict=sp2phylum
    if tax=='Order':
        tax_dict=sp2order
    if tax=='Class':
        tax_dict=sp2class
    if tax=='Family':
        tax_dict=sp2family
    if tax=='Genus':
        tax_dict=sp2genus
    # print(df)
    this_df.columns=['Species','Direction']
    this_df['Direction']=this_df['Direction'].replace({'Chinese > Non-Chinese':'HC-PSPGs','Non-Chinese > Chinese':'NC-PSPGs'})
    this_df[tax]=this_df['Species'].replace(tax_dict)
    cnt_df=this_df.groupby([tax,'Direction']).count()
    cnt_df=cnt_df.reset_index()
    cnt_df.columns=[tax,'Direction','Number of species']
    # print(cnt_df)
    
    cnt_df2=this_df.groupby([tax]).count()
    cnt_df2=cnt_df2.reset_index()
    cnt_df2=cnt_df2.sort_values('Species')
    tax_list=cnt_df2[tax].tolist()
    # print(tax_list)
    # print(cnt_df2)
    import plotly.express as px
    fig=px.bar(cnt_df,y=tax,x='Number of species',
               template='simple_white',text='Number of species',
               color='Direction',
               color_discrete_map = {'HC-PSPGs': '#CD5C5C','NC-PSPGs': '#20B2AA'}
              )
    fig.update_layout(
        xaxis_title='Number of species',
        yaxis_title=tax,
        width=this_width,
        height=this_height,
        legend_title_text='Category',
        showlegend=True,
#         title_text=tax,title_x=0.5,title_font=dict(size=20,),
        # boxmode='stack' # 柱状图模式
    )
    fig.update_traces(textfont_size=20, textangle=0, cliponaxis=False)# textposition="inside", 
    fig.update_yaxes(tickfont_size=15)
#     fig.update_xaxes(tickfont_size=20)
    fig.update_xaxes(title_font_size=20)
    fig.update_yaxes(title_font_size=20)
    # fig.update_layout(yaxis = dict(tickfont = dict(size=10)))
    # fig.update_xaxes(tickangle=270)
    
    fig.update_yaxes(categoryorder='array', categoryarray= tax_list)
    fig.show()
    fig.write_image(os.path.join(prevalence_dir,'prevalence'+'.'+tax+'.species.distribution.pdf'),width=this_width,height=this_height,scale=2)


tax='Family'
this_df=df[['species','direction']]
tax_barplot(this_df,tax,700,900)
