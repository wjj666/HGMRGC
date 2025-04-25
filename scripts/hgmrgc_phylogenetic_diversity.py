import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

# Phylogenetic diversity
work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG/phygenetic diversity'
df=pd.read_csv(os.path.join(work_dir,'hgmrgc_phylogenetic_diversity.csv'))
df=df[df['Phylum']!='Total']
df.sort_values(by='OUR_PD',ascending=False,inplace=True)
phylum_list=df['Phylum'].tolist()
# print(df)


fig = px.bar(df, y='OUR_PD', x='Phylum', 
             text='OUR_PD',text_auto='.2f',
             category_orders={'Phylum': phylum_list}
            )
fig.update_traces(marker_color='orange')
fig.update_traces(textfont_size=10, textangle=0,  cliponaxis=True)
fig.update_layout(
        width=1000,
        height=400,
        legend_title_text='Quality',
        showlegend=False,
        template='simple_white',
    )
fig.update_layout(
    yaxis_title='Phylogenetic diversity',  
    xaxis_title=''
    
)
fig.update_traces(textposition='outside') 
fig.show()
fig.write_image(os.path.join(work_dir,'phylum_diversity.pdf'),width=1000,height=400,scale=2)
