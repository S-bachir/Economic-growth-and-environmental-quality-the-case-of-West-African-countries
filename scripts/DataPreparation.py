
import matplotlib as plt
import seaborn as sns
# to read and wrangle data
import pandas as pd
# to create spatial data
import geopandas as gpd







# Pour récupérer les années d'études fonction qui sert pour récupérer les data des fichier venant de geoquery
def year_selection(year, df):
    colonnes = list(df.columns)
    list_sorti = ['shapeGroup','shapeName']
    for i in colonnes:
        if year in i:
            list_sorti.append(i)
    return(list_sorti)



df_niger = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/niger_vf/624e1e5977c33211f571ae54_results.csv")
pop_niger = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/niger_vf/niger_pop/624e216077c33211f571ae55_results.csv")
df_nigeria = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/nigeria_vf/624e208f9f9ef44ffa7fc4e2_results.csv")
df_mali = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/mali_vf/624e1f9cb6a0281a2b3b4213_results.csv")
pop_mali = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/mali_vf/mali_pop/624e218c48eade62e70959e2_results.csv")
df_togo = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/togo_vf/624e21b40e369003c4636902_results.csv")
df_guinee = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/guinee_vf/624e29f40e369003c4636903_results.csv")
df_guinee_biss = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/guinee bissao_vf/624e2a59b6a0281a2b3b4214_results.csv")
df_liberia = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/liberia_vf/624e2ad7f1c11067c210a0e2_results.csv")
df_siria_leone = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/sierra leone_vf/624e2b3d0e369003c4636904_results.csv")

df_benin = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/benin_vf/624e259948eade62e70959e3_results.csv")
df_burkina = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/burkina_vf/624e269248eade62e70959e4_results.csv")
df_ci = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/ci_vf/624e277a48eade62e70959e5_results.csv")
df_gambie = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/gambie_vf/624e27fc3290d46dae5db742_results.csv")
df_ghana = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/ghana_vf/624e2982261670583621fe45_results.csv")
df_senegal = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/senegal_vf/624e23a8c4ae757b9b63c083_results.csv")
df_cap_vert = pd.read_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/cap vert_vf/624e2bb8f1c11067c210a0e3_results.csv") 

#Liste des pays
list_pays = ['niger','nigeria','togo','guinee','guinee_biss','liberia','siria_leone','benin','burkina','ci','gambie','ghana','senegal','cap_vert']

##################################2012##############################
df_niger_2012 = df_niger[year_selection('2012.', df_niger)]
df_mali_2012 = df_mali[year_selection('2012.', df_mali)]

#pop_niger_2012 =
df_nigeria_2012 = df_nigeria[year_selection('2012.', df_nigeria)]
#pop_mali_2012 = 
df_togo_2012 = df_togo[year_selection('2012.', df_togo)]
df_guinee_2012 = df_guinee[year_selection('2012.', df_guinee)]
df_guinee_biss_2012 = df_guinee_biss[year_selection('2012.', df_guinee_biss)]
df_liberia_2012 = df_liberia[year_selection('2012.', df_liberia)] 
df_siria_leone_2012 = df_siria_leone[year_selection('2012.', df_siria_leone)]

df_benin_2012 = df_benin[year_selection('2012.', df_benin)]
df_burkina_2012 = df_burkina[year_selection('2012.', df_burkina)]
df_ci_2012 = df_ci[year_selection('2012.', df_ci)] 
df_gambie_2012 = df_gambie[year_selection('2012.', df_gambie)]
df_ghana_2012 = df_ghana[year_selection('2012.', df_ghana)]
df_senegal_2012 = df_senegal[year_selection('2012.', df_senegal)]
df_cap_vert_2012 = df_cap_vert[year_selection('2012.', df_cap_vert)]


##################################2013####################################

df_niger_2013 = df_niger[year_selection('2013.', df_niger)]
df_mali_2013 = df_mali[year_selection('2013.', df_mali)]

#pop_niger_2013 =
df_nigeria_2013 = df_nigeria[year_selection('2013.', df_nigeria)]
#pop_mali_2013 = 
df_togo_2013 = df_togo[year_selection('2013.', df_togo)]
df_guinee_2013 = df_guinee[year_selection('2013.', df_guinee)]
df_guinee_biss_2013 = df_guinee_biss[year_selection('2013.', df_guinee_biss)]
df_liberia_2013 = df_liberia[year_selection('2013.', df_liberia)] 
df_siria_leone_2013 = df_siria_leone[year_selection('2013.', df_siria_leone)]

df_benin_2013 = df_benin[year_selection('2013.', df_benin)]
df_burkina_2013 = df_burkina[year_selection('2013.', df_burkina)]
df_ci_2013 = df_ci[year_selection('2013.', df_ci)] 
df_gambie_2013 = df_gambie[year_selection('2013.', df_gambie)]
df_ghana_2013 = df_ghana[year_selection('2013.', df_ghana)]
df_senegal_2013 = df_senegal[year_selection('2013.', df_senegal)]
df_cap_vert_2013 = df_cap_vert[year_selection('2013.', df_cap_vert)]

list_pays_2012 = [df_niger_2012, df_mali_2012, df_nigeria_2012,df_togo_2012,df_guinee_2012,df_guinee_biss_2012,df_liberia_2012,df_siria_leone_2012,df_benin_2012,df_burkina_2012,df_ci_2012,df_gambie_2012,df_ghana_2012,df_senegal_2012,df_cap_vert_2012]
list_pays_2013 = [df_niger_2013,df_mali_2013, df_nigeria_2013, df_togo_2013, df_guinee_2013, df_guinee_biss_2013, df_liberia_2013, df_siria_leone_2013, df_benin_2013, df_burkina_2013, df_ci_2013, df_gambie_2013, df_ghana_2013, df_senegal_2013, df_cap_vert_2013]

name_order = ['shapeName', 'Precipitation', 'Temperature', 'Viirs_Average',
       'Viirs_Cloud_Coverage_Count', 'Viirs_Cloud_Coverage_Sum',
       'PM2.5AirPollution', 'OzoneAirPollution', 'Population', 'supprimer']

#Permet de transformer les données sur la forme voulue   
for i in list_pays_2012:
    i['Year'] = 2012
    i = i.rename(columns = {'worldpop_pop_count_1km_mosaic.2012.count':'supprimer',
                            'worldpop_pop_count_1km_mosaic.2012.sum':'Population',
                           'viirs_ntl_annual_v20_cf_cvg.2012.count':'Viirs_Cloud_Coverage_Count',
                           'viirs_ntl_annual_v20_cf_cvg.2012.sum':'Viirs_Cloud_Coverage_Sum',
                           'viirs_ntl_annual_v20_avg_masked.2012.mean':'Viirs_Average',
                           'udel_precip_v501_mean.2012.mean':'Precipitation',
                           'udel_air_temp_v501_mean.2012.mean':'Temperature',
                            'ambient_air_pollution_2013_o3.2012.mean':'OzoneAirPollution',
                            'ambient_air_pollution_2013_fus_calibrated.2012.mean':'PM2.5AirPollution'}, inplace = True)
    

for i in list_pays_2013:  
    i['Year'] = 2013
    i = i.rename(columns = {'worldpop_pop_count_1km_mosaic.2013.count':'supprimer',
                            'worldpop_pop_count_1km_mosaic.2013.sum':'Population',
                           'viirs_ntl_annual_v20_cf_cvg.2013.count':'Viirs_Cloud_Coverage_Count',
                           'viirs_ntl_annual_v20_cf_cvg.2013.sum':'Viirs_Cloud_Coverage_Sum',
                           'viirs_ntl_annual_v20_avg_masked.2013.mean':'Viirs_Average',
                           'udel_precip_v501_mean.2013.mean':'Precipitation',
                           'udel_air_temp_v501_mean.2013.mean':'Temperature',
                            'ambient_air_pollution_2013_o3.2013.mean':'OzoneAirPollution',
                            'ambient_air_pollution_2013_fus_calibrated.2013.mean':'PM2.5AirPollution'}, inplace = True)



#On cree la base total avec toutes nos dates et les différents pays 
df_2012_2013 = pd.concat([df_niger_2012, df_mali_2012, df_nigeria_2012,df_togo_2012,df_guinee_2012,df_guinee_biss_2012,df_liberia_2012,df_siria_leone_2012,df_benin_2012,df_burkina_2012,df_ci_2012,df_gambie_2012,df_ghana_2012,df_senegal_2012,df_cap_vert_2012,df_niger_2013, df_mali_2013, df_nigeria_2013,df_togo_2013,df_guinee_2013,df_guinee_biss_2013,df_liberia_2013,df_siria_leone_2013,df_benin_2013,df_burkina_2013,df_ci_2013,df_gambie_2013,df_ghana_2013,df_senegal_2013,df_cap_vert_2013]
)   


###Pour enregistrer la base


#df_2012_2013.to_excel("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/CDAO_2012_2013.xlsx", index=False)
#df_2012_2013.to_csv("C:/Users/bachi/OneDrive/cours ensai/3A/projets/Projet stat spatiale/database/VERSION FINALE/CDAO_2012_2013.csv") 
