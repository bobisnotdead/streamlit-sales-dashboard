from copyreg import pickle
from os import walk, path, listdir
import pickle

retour = r'/home/acid/martillac/retour_travaux/'
c6_base  = r'/home/acid/Documents/C6_database/'
sro_list = listdir(retour)


def get_listBySro_ppt(selected_sro):
    sro_info_db ={}
    for file in listdir(c6_base):
        # print(file)
        # if file.endswith('.p'):
        if file.startswith(selected_sro) and file.endswith('.p'):
            print(file)
            fp = path.join(c6_base, file)
            filedb = pickle.loads(open(fp,'rb'))
            sro_info_db[fp] = filedb 
    return sro_info_db


def by_nro(selected_nro):
        list_pm = listdir(path.join(retour, selected_nro))
        return list_pm


def get_picture_by_art(selected_sro, selected_pm):
    art_list = [] 
    pm_folder = path.join(retour,selected_sro, selected_pm) 
    for folder in listdir(pm_folder):
        art = path.join(pm_folder,folder) 
        if 'PHOTOS' in listdir(art):
            art_list.append(folder)
    return art_list


def number_of_poteau_by_sro(selected_sro):
    for file in listdir(c6_base):
        if file.startswith(selected_sro) and file.endswith("p"):
            fp =print(path.join(c6_base,file))
            df = pickle.load(open(fp,'rb'))

print(get_listBySro_ppt('THO'))


