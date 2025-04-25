import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/Writing/2_Compare_UHGG'
uhgg_df=pd.read_csv(os.path.join(work_dir,'uhgg_stats.csv'))
ours_df=pd.read_excel(os.path.join(work_dir,'hgmrgc_stats.xlsx'))
import plotly.graph_objects as go
ours_df.columns=['representative genome', 'cluster name', 'taxonomic lable',
       'annotation level', 'phylum', 'newquality',
        'Completeness (%)',
       'Contamination (%)', 'Length (bp)', 'N50']
uhgg_df.columns=['Genome', 'Length (bp)', 'N50', 'Completeness (%)', 'Contamination (%)',
       'Species representative', 'MGnify accession']
import warnings
warnings.filterwarnings("ignore")
this_height=250
this_width=500
def one_measure(measure_str):
    uhgg_measure=uhgg_df[measure_str].tolist()
    ours_measure=ours_df[measure_str].tolist()
    if measure_str=='N50':
        alt_str='less'
    if measure_str=='Completeness (%)':
        alt_str='less'
    if measure_str=='Contamination (%)':
        alt_str='greater'
    if measure_str=='Length (bp)':
        alt_str='less'
    stat,p_value = stats.mannwhitneyu(uhgg_measure,ours_measure,alternative=alt_str)
    print(measure_str,p_value)
    print('mean:',np.mean(uhgg_measure),np.mean(ours_measure))
    print('median',np.median(uhgg_measure),np.median(ours_measure))
    uhgg_measure_df=uhgg_df[[measure_str]]
    uhgg_measure_df['Catalog']='UHGG'
    ours_measure_df=ours_df[[measure_str]]
    ours_measure_df['Catalog']='HGMRGC'
    tdf=pd.concat([uhgg_measure_df,ours_measure_df])
    # print(4644+5785,len(tdf))
    # print(tdf)

    fig = go.Figure()

    catalogs = ['UHGG', 'HGMRGC']
    catalog2color={}
    catalog2color['UHGG']='Green'
    catalog2color['HGMRGC']='Red'
    fig = px.box(tdf, y="Catalog", x=measure_str,
                    color="Catalog", 
                 # box=True,
                    color_discrete_map = {'UHGG': 'Green','HGMRGC': 'Red'}
                    # points="all",
          )
    fig.update_yaxes(categoryorder='array', categoryarray= ['UHGG','HGMRGC'])
    fig.update_yaxes(tickfont_size=15)
    fig.update_xaxes(tickfont_size=12)
    fig.update_yaxes(title_font_size=15)
    fig.update_xaxes(title_font_size=15)
    
    fig.update_layout(
        # title="Representatives' "+measure_str,
        xaxis_title=measure_str,
        yaxis_title="",
        width=this_width,
        height=this_height,
        showlegend=False,
        template='simple_white',
        xaxis_title_font=dict(size=15),
    yaxis_title_font=dict(size=20),
    )
    fig.update_traces(marker=dict(size=0.5))

    if measure_str=='Contamination (%)':
        measure_str='Contamination'
    if measure_str=='Completeness (%)':
        measure_str='Completeness'
    if measure_str=='Length (bp)':
        measure_str='Length'
#     fig.update_layout(title_text="Representatives' "+measure_str, title_x=0.5)
    fig.show()
    fig.write_image(os.path.join(work_dir,'compare2uhgg'+'.'+measure_str+'.box.pdf'),width=this_width,height=this_height,scale=2)
    
    print('\n')
one_measure('N50')
one_measure('Contamination (%)')
one_measure('Completeness (%)')
one_measure('Length (bp)')
