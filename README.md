# PREDICTAPPbeta

##### télécharger le fichier ".h5" depuis de le drive suivant : [get model save](https://drive.google.com/file/d/1tBMtW4vHkHDVKtKQu-zg3Yzl_ExBz48a/view?usp=sharing)

prerequis:
- python3
- virtualenv
*si vous ne disposé pas de virtualenv*
```
pip install virtualenv
```
**etape 1 :**

clone le repository

```
git clone https://github.com/rezar12/PREDICTAPPbeta.git
```
en suite rdv dans le repo
```
cd PREDICTAPPbeta
```
**etape 2 :**
creation d'un env virtuel
```
virtualenv myenv
```

**etape 3 :**
instaler les dependances
```
pip install -r requirements.txt
```

**etape 4 :**

**deplacer le fichier du model sauvegardé dans le repertoire de l'APP.**


**etape 5 :**
creation du dossier *''images''*
```
mkdir images
```
##### structure de dossier :
|---PREDICTAPPbeta|
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---images
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---App.py
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---README.md
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---requirements.txt
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---model.h5

**etape 6 :**
lancé streamlit pour utilisé l'app :
```
streamlit run App.py
```
