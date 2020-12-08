import pandas as pd
import numpy as np
import os
import re
from datetime import date
from step0_settings import domainPath, dataPath, mmdd, needIndustry

'''
將上步驟每個董監經理人對應到的學院merge回去原本的表格中
'''

i = 0
for industry in needIndustry:
    i += 1
    print(f'第{i}個產業：{industry}')
    df = pd.read_excel(dataPath + f'1.0_學歷配對_{industry}_{mmdd}.xlsx')
    # 修改 20201201
    # df = df.iloc[:,:-2]
    df = df.drop(['學經歷及目前兼任說明','學院','科系'], axis=1)
    df['教育程度'].fillna('無', inplace = True)
    dfIdAndCollege =  pd.read_excel(dataPath + f'1.1_姓名學院_{industry}_{mmdd}.xlsx')
    final = df.merge(dfIdAndCollege, how='left', on=['姓名代碼','董監經理人姓名','教育程度'])


    final.to_excel(dataPath + f'1.2_學院更新_{industry}_{mmdd}.xlsx',
                        encoding = 'utf_8_sig', index = False
            )
print('------------------------------完成-----------------------------------------------')