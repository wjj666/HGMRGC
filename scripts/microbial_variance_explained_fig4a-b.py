import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

def abd_all_sample_r2(cohort_str):
    work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/1_Abundance/update/permanova_similarity/'
    
    loc_path=os.path.join(work_dir,'abd.loc.'+cohort_str+'.permanova.res.perm.100000.csv')
    age_path=os.path.join(work_dir,'abd.age.'+cohort_str+'.permanova.res.perm.100000.csv')
    sex_path=os.path.join(work_dir,'abd.sex.'+cohort_str+'.permanova.res.perm.100000.csv')
    bmi_path=os.path.join(work_dir,'abd.bmi.'+cohort_str+'.permanova.res.perm.100000.csv')
    
    
    loc_df=pd.read_csv(loc_path)
    age_df=pd.read_csv(age_path)
    sex_df=pd.read_csv(sex_path)
    bmi_df=pd.read_csv(bmi_path)
    
    merge_df=pd.concat([loc_df,age_df,sex_df,bmi_df])
    merge_df['type']='abd'
    merge_df['cohort']=cohort_str
    merge_df=merge_df.sort_values(['r2'],ascending=[False])
    merge_df=merge_df[['pop','r2','pval']]
    merge_df['r2']=merge_df['r2']*100
    merge_df.columns=['Factor','Estimated variance (%)','P-value']
    merge_df['Factor']=merge_df['Factor'].replace(
        {'loc':'Geography',
        'age':'Age',
        'sex':'Sex',
         'bmi':'BMI'}
    )
    if cohort_str=='discovery':
        merge_df['Cohort']='Discovery cohort'
    else:
        merge_df['Cohort']='Replication cohort'
    print(merge_df)
    return merge_df

# abd_based
dis_df=abd_all_sample_r2('discovery')
rep_df=abd_all_sample_r2('replication')
merge_df=pd.concat([dis_df,rep_df])
# plot_r2_bar(merge_df,'Abundance-based, Discovery cohort',this_width,this_height)
# merge_df=abd_all_sample_r2('replication')
# plot_r2_bar(merge_df,'Abundance-based, Replication cohort',this_width,this_height)


this_width=800
this_height=400

def plot_r2_bar(merge_df,title,this_width,this_height):
    pop_list=['Geography','Age','Sex','BMI']
    fig=px.bar(merge_df,y='Estimated variance (%)',x='Cohort',
                   template='simple_white',
                   text='Estimated variance (%)',
                   text_auto='.2f',
                   color='Factor',
                   color_discrete_map = {'Geography': '#CD5C5C','Age': '#5F9EA0','Sex':'#FF7F50','BMI':'#9370DB'},
               barmode='group'
                  )
    # fig.update_traces(textposition = 'outside')
    fig.update_layout(
            xaxis_title='',
            yaxis_title=title+'<br>'+'estimated variance (%)',
            width=this_width,
            height=this_height,
            # legend_title_text='Direction of alpha diversity',
#             title_text=title,title_x=0.5,title_font=dict(size=20,),
            showlegend=True
            # boxmode='stack' # 柱状图模式
    )
    fig.update_yaxes(range=[0, 4.5])
    fig.update_traces(textfont_size=20, textangle=0, textposition="outside", cliponaxis=False)
    fig.update_xaxes(categoryorder='array', categoryarray= pop_list)
    fig.update_yaxes(tickfont_size=12)
    fig.update_xaxes(tickfont_size=20)
    fig.update_yaxes(title_font_size=20)
    # fig.update_layout(yaxis = dict(tickfont = dict(size=10)))
    # fig.update_xaxes(tickangle=270)
    fig.show()
    fig.write_image(os.path.join(geo_dir,title+'.allspecies.pdf'),width=this_width,height=this_height,scale=2)
plot_r2_bar(merge_df,'Abundance-based',this_width,this_height)


def snp_all_sample_r2(cohort_str):
    work_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/15_allele_sharing_score'
    
    loc_path=os.path.join(work_dir,'snp.loc.'+cohort_str+'.permanova.res.perm.100000.csv')
    age_path=os.path.join(work_dir,'snp.age.'+cohort_str+'.permanova.res.perm.100000.csv')
    sex_path=os.path.join(work_dir,'snp.sex.'+cohort_str+'.permanova.res.perm.100000.csv')
    bmi_path=os.path.join(work_dir,'snp.bmi.'+cohort_str+'.permanova.res.perm.100000.csv')
    
    
    loc_df=pd.read_csv(loc_path)
    age_df=pd.read_csv(age_path)
    sex_df=pd.read_csv(sex_path)
    bmi_df=pd.read_csv(bmi_path)
    
    merge_df=pd.concat([loc_df,age_df,sex_df,bmi_df])
    merge_df['type']='snp'
    merge_df['cohort']=cohort_str
    merge_df=merge_df.sort_values(['r2'],ascending=[False])
    merge_df=merge_df[['pop','r2','pval']]
    merge_df['r2']=merge_df['r2']*100
    merge_df.columns=['Factor','Estimated variance (%)','P-value']
    merge_df['Factor']=merge_df['Factor'].replace(
        {'loc':'Geography',
        'age':'Age',
        'sex':'Sex',
         'bmi':'BMI'}
    )
    if cohort_str=='discovery':
        merge_df['Cohort']='Discovery cohort'
    else:
        merge_df['Cohort']='Replication cohort'
    print(merge_df)
    return merge_df

# snp_based
dis_df=snp_all_sample_r2('discovery')
rep_df=snp_all_sample_r2('replication')
merge_df=pd.concat([dis_df,rep_df])


this_width=800
this_height=400
plot_r2_bar(merge_df,'SNP-based',this_width,this_height)