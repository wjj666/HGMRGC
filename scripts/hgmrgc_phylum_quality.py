import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats


# quality proportion 每个phylum下high和medium的比例
work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG/genome_quality'
import pandas as pd
import os
df=pd.read_csv(os.path.join(work_dir,'representatives_cnt.csv'))
tax_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/0_tax'
import ujson
with open(os.path.join(tax_dir,'sp2phylum.json')) as f:
    sp2phylum=ujson.load(f)
df['Phylum']=df['Species']
df['Phylum'].replace(sp2phylum,inplace=True)

df=df[['Species','The quality of representative_genome','Phylum']]
cnt_df=df.groupby(['Phylum','The quality of representative_genome']).count()

cnt_df=cnt_df.reset_index()

cnt_df2=df.groupby(['Phylum']).count()
cnt_df2=cnt_df2.reset_index()
phylum_list=cnt_df2['Phylum'].tolist()
cnt_list=cnt_df2['Species'].tolist()
phylum2cnt=dict(zip(phylum_list,cnt_list))

cnt_df['phylum_cnt']=cnt_df['Phylum']
cnt_df['phylum_cnt']=cnt_df['phylum_cnt'].replace(phylum2cnt)

cnt_df['prop']=(cnt_df['Species']/cnt_df['phylum_cnt'])*100

high_df=cnt_df[cnt_df['The quality of representative_genome']=='high-quality']
medium_df=cnt_df[cnt_df['The quality of representative_genome']=='medium-quality']
high_df=high_df.sort_values(['prop'],ascending=False)
cnt_df=pd.concat([high_df,medium_df])
cnt_df['The quality of representative_genome']=cnt_df['The quality of representative_genome'].replace({'high-quality':'High','medium-quality':'Medium'})
cnt_df.columns=['Phylum','Quality','Species','Phylum_cnt','Proportion']


cnt_df_phylum=cnt_df[['Phylum','Phylum_cnt']]
cnt_df_phylum=cnt_df_phylum.drop_duplicates()
high_df=high_df.sort_values(['prop'],ascending=False)
cnt_df_phylum.columns=['Phylum','Number of species']




fig = px.bar(cnt_df, y='Proportion', x='Phylum', 
             color='Quality',text='Proportion',text_auto='.2f'
            )
fig.update_traces(textfont_size=6, textangle=0,  cliponaxis=True)
fig.update_layout(
        width=1000,
        height=380,
        legend_title_text='Genome quality',
        showlegend=True,
        template='simple_white',
    )
fig.update_layout(
    yaxis_title='Proportion (%)',  
    xaxis_title=''
    
)
fig.show()
fig.write_image(os.path.join(work_dir,'quality_proportion_legend.pdf'),width=1000,height=380,scale=2)
