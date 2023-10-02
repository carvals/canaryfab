import streamlit as st
import os

#page layout center
# set the page title and icon
st.set_page_config(page_title="Canary Fab", page_icon="	:factory:", layout="centered")


# Add custom CSS to hide the GitHub icon
#hide_github_icon = """
#GithubIcon {
#  visibility: hidden;
#}
#"""
#st.markdown(hide_github_icon, unsafe_allow_html=True)


#construct the path of the img folder
img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ressource/img'))



#center the title
st.markdown("""<h1 style="font-family: Garamond; 
text-align: center;">Canary Fab</h1>""", unsafe_allow_html=True)

#make 2 columns
col1, col2 = st.columns(2)
#in col2 put some text
col2.markdown("""<br>""", unsafe_allow_html=True)
col2.markdown("""
#### Ouverture du premier local toulousain dédié au data engineering industriel, l'électronique et la fabrication.""")

st.markdown("""Afin d'accompagner sa croissance, la société Otahy crée un établissement inédit à Toulouse Ouest. 
Son ambition est de rassembler une communauté d'indépendants et de petites structures autour des activités de data engineering industriel
ainsi que de prototypage.  
L'objectif est de pouvoir échanger, s'entraider, mutualiser compétences et outils...
Et pourquoi pas, faire des projets ensemble.
""")

st.markdown("""Notre vision est qu'un data engineer ou architecte de données dans l'industrie doit être entouré de machines.
C'est pourquoi ce site unique accueillera une capacité de fabrication accessible aux résidents.  """)

st.markdown("""Pour cela nous proposons:""")

#in col1 the image
canary_path = os.path.join(img_path, 'canary_solo_200.png')
col1.image(canary_path, output_format = "PNG")
#create a title and sub-title for the app

st.markdown("""## Un plateau de 90m2 dédié au data engineering""")

col3, col4 = st.columns(2)
#make few bullet points
col3.markdown("""* un open space de 30m2 pour 6 postes de travail ergonomiques + casier individuel 
* 2 bureaux privatifs de 12 et 15m2
* 1 salle de réunion
""")

col4.markdown("""* imprimante NB
* Sanitaire avec douche
* Serveur et switch sur onduleur
* Fibre optique / wifi""")

#image of local etage
local_path = os.path.join(img_path, 'local_etage.png')
st.image(local_path, width=400)

st.markdown("""## Un espace détente de 25m2 intérieur""")
col5, col6 = st.columns(2)

col5.markdown("""* espace cuisine""")

col6.markdown("""* PS4""")

st.markdown("""## Un atelier électronique et prototypage de 90m2""")
col7, col8 = st.columns(2)

col7.markdown(""" 
Électronique :
* Pick N Place automatique
* Pick N Place semi-automatique
* Four de refusion
* Microscope
* Station de soudure""")

col8.markdown(""" 
Construction et découpe :
* Imprimante 3D
* Découpe laser 40W
* Scie sur table 
* Compresseur
* Divers outils""")

st.markdown("""Nous sommes ouverts à l'ajout de nouveaux équipements en fonction des besoins de la communauté.""")

st.markdown("""## Conditions d'accès""")

st.markdown("""**Possibilité de location flexible :**
* un poste de travail seul avec un minimum de 3 mois avec ou sans accès à l'atelier
* un bureau privatif avec un minimum de 3 mois avec ou sans accès à l'atelier
* Mise à disposition d'une surface dédiée dans l'atelier""")

st.markdown("""Pour le moment, l'accès à l'atelier est réservé aux résidents.""")




st.markdown("""**Localisation :**""")

col9, col10 = st.columns(2)
local_ext_path = os.path.join(img_path, 'local_ext3.jpg')
col9.image(local_ext_path, output_format = "JPEG")

map_path = os.path.join(img_path, 'carte_ramassier3.jpg')
col10.image(map_path, output_format = "JPEG")

st.markdown("""
* [Chemin de l'Armurié, Colomiers](https://www.google.com/maps/place/Chemin+de+l'Armurié,+31770+Colomiers/)
* proche gare des Ramassiers
* Bus  L3 / 21 / 25 / 32 / 63
* Piste cyclable arrive devant le local
* 4 places voiture + parking vélo
* Espace détente extérieur 
* proche commerces, restaurants, salles de sport """)

st.markdown("""### Ouverture prévue le 16 Novembre 2023""")
st.markdown("""### Informations et réservations :
* [canaryfab@otahy.com](mailto:canaryfab@otahy.com)
* [0769763214](tel:0769763214)""")

#add orphan data image
#st.image(os.path.join(img_path, 'orphan_data.png'),output_format = "PNG")






