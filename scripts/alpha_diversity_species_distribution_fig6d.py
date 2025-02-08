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


# distribution
def single_stype_direction(df,stype):
    df=df[['species','direction']]
    cnt_df=df.groupby(['direction']).count()
    print(stype,cnt_df)
snp_df=pd.read_csv(os.path.join(alpha_dir,'snp.alpha.sig.species.csv'))
single_stype_direction(snp_df,'snp')


def single_stype_barplot(this_df,stype,tax,this_width,this_height):
    
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
    this_df[tax]=this_df['Species'].replace(tax_dict)
    cnt_df=this_df.groupby([tax,'Direction']).count()
    cnt_df=cnt_df.reset_index()
    cnt_df.columns=[tax,'Direction','Number of species']
    
    cnt_df2=this_df.groupby([tax]).count()
    cnt_df2=cnt_df2.reset_index()
    cnt_df2=cnt_df2.sort_values('Species')
    tax_list=cnt_df2[tax].tolist()
    # print(tax_list)
    # print(cnt_df2)
    # print(cnt_df)
    cnt_df.columns=['Family','Category','Number of species']
    cnt_df['Category']=cnt_df['Category'].replace(
        {'Chinese > Non-Chinese': 'HC > NC',
         'Non-Chinese > Chinese': 'NC > HC'}
    )
    import plotly.express as px
    fig=px.bar(cnt_df,y=tax,x='Number of species',
               template='simple_white',text='Number of species',
               color='Category',
               color_discrete_map = {'HC > NC': '#CD5C5C','NC > HC': '#20B2AA'}
              )
    fig.update_layout(
        xaxis_title='Number of species',
        yaxis_title=tax,
        width=this_width,
        height=this_height,
        legend_title_text='Direction of<br>SNP-based alpha diversity',
#         title_text=stype,title_x=0.5,
        showlegend=True
        # boxmode='stack' # 柱状图模式
    )
    fig.update_yaxes(tickfont_size=15)
#     fig.update_xaxes(tickfont_size=20)
    fig.update_xaxes(title_font_size=20)
    fig.update_yaxes(title_font_size=20)
    fig.update_yaxes(categoryorder='array', categoryarray= tax_list)
    fig.show()
    fig.write_image(os.path.join(alpha_dir,stype+'.'+tax+'.species.distribution.pdf'),width=this_width,height=this_height,scale=2)
this_snp_df=snp_df[['species','direction']]
stype='SNP-based'
tax='Family'
single_stype_barplot(this_snp_df,stype,tax,600,600)
