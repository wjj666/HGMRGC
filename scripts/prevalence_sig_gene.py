import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

gene_df=pd.read_csv(os.path.join(prevalence_dir,'prevalence_sig_genes.csv'))

gene_list=gene_df['Gene'].tolist()
gene_list=list(set(gene_list))
tdf=gene_df[gene_df['Category 2']!='Unknown']

tdf=tdf[['Gene','Category 1','Category 2','Direction']]
tdf.columns=['Gene','Primary category','Secondary category','Direction']
tdf=tdf.drop_duplicates()
gene2num={}
res=[]
cat2cnt={} 

for indexs in tdf.index:
    tmp=tdf.loc[indexs]
    gene=tmp['Gene']
    cat1=tmp['Primary category']
    cat2=tmp['Secondary category']
    if cat2 not in cat2cnt:
        cnt=1
    else:
        cnt=cat2cnt[cat2]
        cnt=cnt+1
    cat2cnt[cat2]=cnt
    res.append([gene,cat1,cat2,cnt,tmp['Direction']])
res_df=pd.DataFrame(res)
res_df.columns=['Gene name','Primary category','Secondary category','Number of genes','Direction']
# res_df=res_df.sort_values(['Category 2','Number of genes','Gene name'])
res_df=res_df.sort_values(['Gene name'])
res_df['Count']=1
# res_df=res_df

cat_df=res_df[['Primary category','Secondary category']]
cat_df=cat_df.drop_duplicates()
cat2cat1=dict(zip(cat_df['Secondary category'].tolist(),cat_df['Primary category'].tolist()))

cat2_df=res_df[['Secondary category','Gene name']]

cat2_df=cat2_df.groupby(['Secondary category']).count()
cat2_df=cat2_df.reset_index()
cat2_df['Primary category']=cat2_df['Secondary category'].replace(cat2cat1)
cat2_df=cat2_df.sort_values(['Primary category','Gene name'],ascending=[True,True])
cat2_list=cat2_df['Secondary category'].tolist()

color_discrete_map={'Secondary metabolism':'rgb(228,26,28)', 
     'Nucleotide sugar biosynthesis':'rgb(55,126,184)',
     'Energy metabolism':'rgb(77,175,74)', 
     'Genetic information processing':'rgb(152,78,163)',
     'Environmental information processing':'rgb(255,127,0)',
     'Cellular processes':'rgb(255,215,0)',
     'Carbohydrate and lipid metabolism':'rgb(166,96,40)',
     'Aminoacyl-tRNA biosynthesis':'rgb(247,129,191)', 
     'Nucleotide and amino acid metabolism':'rgb(135,206,235)',
                   'Unknown':'rgb(211,211,211)'}
this_width=1800
this_height=900
fig=px.bar(res_df,x='Count',y='Secondary category',
           template='simple_white',
           text='Gene name',
           color='Primary category',
           color_discrete_map = color_discrete_map
          )
fig.update_layout(
    xaxis_title='Number of genes',
    yaxis_title='Secondary category',
    width=this_width,
    height=this_height,
    # legend_title_text='Direction of alpha diversity',
    # title_text=stype,title_x=0.5,
    showlegend=True
    # boxmode='stack' # 柱状图模式
)
fig.update_yaxes(categoryorder='array', categoryarray= cat2_list)
# fig.update_layout(xaxis = dict(tickfont = dict(size=8)))
# fig.update_xaxes(tickangle=90)
fig.update_yaxes(tickfont_size=18)
# fig.update_xaxes(tickfont_size=20)
fig.update_xaxes(title_font_size=20)
fig.update_yaxes(title_font_size=20)
fig.update_traces(textfont_size=18, textangle=0, textposition="inside", cliponaxis=True)
fig.show()
fig.write_image(os.path.join(prevalence_dir,'sig.gene.km.anno.pdf'),width=this_width,height=this_height,scale=2)
