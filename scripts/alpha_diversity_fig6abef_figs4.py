import os
import sys
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats
# box plot

phe_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/0_Phenotype/'
phe_df=pd.read_csv(os.path.join(phe_dir,'discovery_replication.phe.csv'))


div_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/11_alpha_div/update'
def cohort_info(stype,n_sd,df,div_name):
    raw_sid_list=df['sid'].tolist()
    for raw_sid in raw_sid_list:
        if '.' in raw_sid: 
            # print(raw_sid)
            pass
    new_sid_list=[sid.split('.')[0] for sid in raw_sid_list]
    raw2new=dict(zip(raw_sid_list, new_sid_list))
    df['sid'].replace(raw2new,inplace=True)
    
    # remove the outliers
    df_mean=np.mean(df[div_name])
    df_std=np.std(df[div_name])

    df_abover=df_mean+n_sd*df_std
    df_belower=df_mean-n_sd*df_std
    

    
    if n_sd==0:
        pass
    else:
        df=df[(df[div_name]<=df_abover)&(df[div_name]>=df_belower)]
    
    df['sid']=df['sid'].astype(str)
    df.set_index(['sid'],inplace=True)
    phe_df.reset_index(inplace=True)
    phe_df['sid']=phe_df['sid'].astype(str)
    phe_df.set_index(['sid'],inplace=True)
    
    merge_df=pd.concat([df,phe_df],join='inner',axis=1)
    # merge_df.to_csv(os.path.join(div_dir,'1.'+stype+'.div.rm.'+str(n_sd)+'sd.csv'))

    return stype,merge_df


def compare_div(stype,merge_df,div_name,this_height,this_width):
    
    if stype=='abundance':
        stype='Abundance-based'
        this_title_text=''
        this_yaxis_title='Abundance-based alpha diversity'
    if stype=='dsv':
        stype='Deletion SV-based'
        this_title_text=''
        this_yaxis_title='dSV-based alpha diversity'
    if stype=='vsv':
        stype='Variable SV-based'
        this_title_text=''
        this_yaxis_title='vSV-based alpha diversity'
        
    if stype=='snp':
        stype='SNP-based'
        this_title_text=''
        this_yaxis_title='SNP-based alpha diversity'
    if stype=='Species_256':
        stype='Lawsonibacter asaccharolyticus'
        this_title_text='Lawsonibacter asaccharolyticus'
        this_yaxis_title='SNP-based alpha diversity'
    if stype=='Species_309':
        stype='Escherichia coli_C'
        this_title_text='Escherichia coli_C'
        this_yaxis_title='SNP-based alpha diversity'
        
        
    
    
    merge_df['location']=merge_df['location'].replace({'East':'HC','West':'NC'})
    merge_df['cohort']=merge_df['cohort'].replace({'discovery':'Discovery cohort','replication':'Replication cohort'})
    merge_df=merge_df[[div_name,'cohort','location']]
    merge_df.columns=['Alpha diversity','Cohort','Population']
    
    merge_df.to_csv(os.path.join(alpha_dir,stype+'.alpha.div.csv'))
    category_order=['HC','NC']
    colors={'HC':'red','NC':'green'}
    
    
    fig=px.box(merge_df,x='Cohort',y='Alpha diversity',color='Population',
               template='simple_white',
               notched=True,
               category_orders={'Population': category_order},
               color_discrete_map=colors,
              )
    fig.update_layout(
        yaxis_title=this_yaxis_title,
        xaxis_title='',
        # title=cohort_str,
        width=this_width,
        height=this_height,
        title_text=this_title_text,title_x=0.5,title_font=dict(size=20),
        # legend_title_text='Catalog',
        showlegend=True
        # boxmode='group' # 柱状图模式
    )
    # fig.update_layout(
    #             title={
    #             'text' : ,
    #             'x':0.5,
    #             'xanchor': 'center'
                    
    #         })
    
    fig.update_xaxes(categoryorder='array', categoryarray= ['Discovery cohort','Replication cohort'])
    fig.update_xaxes(tickfont_size=20)
    fig.update_yaxes(tickfont_size=15)
    fig.update_yaxes(title_font_size=20)
    
    fig.show()
    fig.write_image(os.path.join(alpha_dir,stype+'.alpha.div.pdf'),width=this_width,height=this_height,scale=2)


# abundance 
abd_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/1_Abundance/update'
df=pd.read_csv(os.path.join(abd_dir,'abundance_alpha_div.csv'))
df=df.dropna(how='any')
stype,merge_df=cohort_info('abundance',3,df,'Shannon diversity')
this_width=600
this_height=450
compare_div('abundance',merge_df,'Shannon diversity',this_height,this_width)


#snp
snp_dir=div_dir
df=pd.read_csv(os.path.join(snp_dir,'allsid.snp.alpha.diversity.csv'))
df=df.dropna(how='any')
df=df[['sid','within_sample_diversity']]
stype,merge_df=cohort_info('snp',3,df,'within_sample_diversity')
this_width=600
this_height=450
compare_div('snp',merge_df,'within_sample_diversity',this_height,this_width)



# Species_256, Lawsonibacter asaccharolyticus

df=pd.read_csv(os.path.join(alpha_dir,'Species_256.snp.alpha.diversity.csv'))
df=df.dropna(how='any')
df=df[['sid','species-level snp diversity']]
stype,merge_df=cohort_info('snp',3,df,'species-level snp diversity')

this_width=600
this_height=450
compare_div('Species_256',merge_df,'species-level snp diversity',this_height,this_width)


# Species_309, Escherichia coli C

df=pd.read_csv(os.path.join(alpha_dir,'Species_309.snp.alpha.diversity.csv'))
df=df.dropna(how='any')
df=df[['sid','species-level snp diversity']]
stype,merge_df=cohort_info('snp',3,df,'species-level snp diversity')

this_width=600
this_height=450
compare_div('Species_309',merge_df,'species-level snp diversity',this_height,this_width)







# dSV
div_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/11_alpha_div/update'
sv_dir=div_dir
tdf1=pd.read_csv(os.path.join(sv_dir,'dsv.discovery.shannon_div.csv'))
tdf2=pd.read_csv(os.path.join(sv_dir,'dsv.replication.shannon_div.csv'))
df=pd.concat([tdf1,tdf2])

# df=pd.read_csv(os.path.join(sv_dir,'1_dsv_shannon_div.csv'))
df=df.dropna(how='any')
df=df[['sid','Shannon diversity']]
stype,merge_df=cohort_info('dsv',3,df,'Shannon diversity')
this_width=600
this_height=450
compare_div('dsv',merge_df,'Shannon diversity',this_height,this_width)


# vSV
div_dir='/Users/wangjingjing/Library/CloudStorage/OneDrive-个人/tmp_code/myproject/00_MetaVariCall/5_Sample/11_alpha_div/update'
sv_dir=div_dir
tdf1=pd.read_csv(os.path.join(sv_dir,'vsv.discovery.shannon_div.csv'))
tdf2=pd.read_csv(os.path.join(sv_dir,'vsv.replication.shannon_div.csv'))
df=pd.concat([tdf1,tdf2])

# df=pd.read_csv(os.path.join(sv_dir,'1_dsv_shannon_div.csv'))
df=df.dropna(how='any')
df=df[['sid','Shannon diversity']]
stype,merge_df=cohort_info('vsv',3,df,'Shannon diversity')
this_width=600
this_height=450
compare_div('vsv',merge_df,'Shannon diversity',this_height,this_width)
