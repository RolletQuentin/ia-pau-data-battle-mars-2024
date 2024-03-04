# Documentation de la base de données

## tblanimation

__Description__ :
```
???
```

__Champs__ :
```
numAnimation : key
codeTechno : foreign key vers tbltechno
idSysteme : ???
toolType : ???
codeSysteme : ???
x : position x
y : position y
largeur : largeur
hauteur : hauteur
rotateTag : balise css pour appliquer une rotation
```

__Exemples__:
```json
{
  numAniamtion: 2,
  codeTechno: 11,
  idSysteme: "filtre",
  toolType: "_tooltip",
  codeSysteme: 143,
  x: 587,
  y: 272,
  largeur: 48,
  hauteur: 18,
  rotateTag: transform:rotate(17deg);
}
```

## tblarretecee

__Description__ :
```
Arrêté sur les Certificats d'Economies d'Energies
```

__Champs__ :
```
numarrete: Numéro de l'arrêté
datearrete: Date de l'arrêté
codereference: foreign key vers tblreference
```

__Exemples__:
```json
{
  numarrete: 2,
  datarrete: 2006-06-19 00:00:00,
  codereference: 4014
}
```

## tblautodiag

__Description__ :
```
??? Peut-être une boîte de dialogue automatique avec un assistant ?
```

__Champs__ :
```
numautodiag: Identifiant
codetechno: foreign key vers tbltechno
ordreautodiag: ???
reponseautodiag: ???
codesolution: foreign key vers tblsolution
```

__Exemples__:
```json
{
  numautodiag: 1,
  codetechno: 1,
  ordreautodiag: 1,
  reponseautodiag: 1,
  codesolution: 1
}
```

## tblbenchmark

__Description__ :
```
??? Une table relative au benchmark proposer par la plateforme ?
```

__Champs__ :
```
numbenchmark: Identifiant
codeappelbenchmark: Le numéro d'appel au benchmark
xcodeunitebenchmark: ???
codemonnaiebenchmark: foreign key vers tblmonnaie
codetaxe: foreign key vers tbltaxe
abenchmark: ???
bbenchmark: ???
codelicense: foreign key vers tbllicense
```

__Exemples__:
```json
{
  numbenchmark: 2,
  codeappelbenchmark: 543,
  xcodeunitebenchmark: 16,
  codemonnaiebenchmark: 2,
  codetaxe: 3,
  abenchmark: 893.08,
  bbenchmark: -0.611,
  codelicense: 3
}
```

## tblbenchmarkvalue

__Description__ :
```
??? 
```

__Champs__ :
```
numbenchmarkvalue: Identifiant
datebenchmark: La date de réalisation du benchmark
codeappelbenchmark: Le code d'appel au benchmark
xvaluebanchmark: ???
costbenchmark: Le coût du benchmark ?
yratiobenchmark: ???
codereference: foreign key vers tblreference
coderex: foreign key vers tblrex
```

__Exemples__:
```json
{
  numbenchmarkvalue: 2,
  datebenchmark: 2006-06-19 00:00:00,
  codeappelbenchmark: 543,
  xvaluebanchmark: 12.3,
  costbenchmark: 2395.99,
  yratiobenchmark: 222.36,
  codereference: 4215,
  coderex: 1
}
```

## tblceetheme

__Description__ :
```
Les différents thèmes concernant les Certificats d'Economies d'Energies
```

__Champs__ :
```
numceetheme: Identifiant
codeceegroupe: ???
```

__Exemples__:
```json
{
  numceetheme: 1,
  codeceegroupe: 1
}
```

## tblchart

__Description__ :
```
??? Les différents graphiques ?
```

__Champs__ :
```
codeappelchart: Le code d'appel
typechart: Le type de graphique
xcodeunitechart: Le code pour utiliser une certaine unité pour l'axe des absicisses
ycodeunitechart: Le code pour utiliser une certaine unité pour l'axe des ordonnées
```

__Exemples__:
```json
{
  codeappelchart: 0,
  typechart: "pie",
  xcodeunitechart: 0,
  ycodeunitechart: 34
}
```

## tblchartvalue

__Description__ :
```
??? Les différentes valeurs pour les graphiques ?
```

__Champs__ :
```
numchartvalue : Identifiant
codeappelchart: Le code d'appel
yvaluechart: La valeur en ordonnées du graphique ?
```

__Exemples__:
```json
{
  numchartvalue: 2,
  codeappelchart: 1,
  yvaluechart: 25
}
```

## tblchiffresecteur

__Description__ :
```
???
```

__Champs__ :
```
numchiffresecteur : Identifiant
codereference: foreign key vers la tblreference
coderegion: foreign key vers tblregion
codesecteur: foreign key vers tblsecteur
```

__Exemples__:
```json
{
  numchiffresecteur: 1,
  codereference: 4028,
  coderegion: 2,
  codesecteur, 18
}
```

## tblconnexion

__Description__ :
```
Les différente connexion à l'application
```

__Champs__ :
```
numconnexion: Identifiant
idusergroup: ???
login: Type de personne qui s'est identifiée
ip: Adresse IP
dateconnexion: Date de la connexion
agent: L'agent de connexion
```

__Exemples__:
```json
{
  numconnexion: 1554,
  idusergroup: ,
  login: "Visiteur",
  ip: 77.207.255.70,
  dateconnexion: 2013-07-05 17:38:15,
  agent: "Mozilla/4.0 ..."
}
```

## tblconsosecteur

__Description__ :
```
???
```

__Champs__ :
```
numconsosecteur: Identifiant
codereference: foreign key vers tblreference
coderegion: foreign key vers tblregion
codesecteur: foreign key vers tblsecteur
```

__Exemples__:
```json
{
  numconsosecteur: 1,
  codereference: 4050,
  coderegion: 2,
  codesecteur: 3
}
```

## tblcoutrex

__Description__ :
```
???
```

__Champs__ :
```
numcoutrex: Identifiant
codesolution: foreign key vers tblsolution
coderex: foreign key vers tblrex
minicoutrex: ???
maxicoutrex: ???
reelcoutrex: ???
codemonnaiecoutrex: foreign key vers tblmonnaie
codeunitecoutrex: ???
codedifficulte: la difficulté de mise en place de la solution ???
codelicense: foreign key vers tbllicense
```

__Exemples__:
```json
{
    numcoutrex: 7,
    codesolution: 713,
    coderex: 31,
    minicoutrex: 8000,
    maxicoutrex: 10000,
    reelcoutrex: null,
    codemonnaiecoutrex: 2,
    codeunitecoutrex: 1,
    codedifficulte: 8,
    codelicense: 3
}
```

## tblcritereenr

__Description__ :
```
Critère énergie ... ?
```

__Champs__ :
```
numcritereenr: Identifiant
codetechno: foreign key vers tbltechno
codepays: foreign key vers tblpays
nomcritereenr: Nom du critère
```

__Exemples__:
```json
{
  numcritereenr: 12,
  codetechno: 39,
  codepays: 2,
  nomcritereenr: "Terre - Fonctionnement: entre 2400h et 2800h"
}
```

## tbldictionnaire

__Description__ :
```
Dictionnaire des différente traduction pour le support multilangue
```

__Champs__ :
```
numdictionnaire: Identifiant
codelangue: foreign key vers tbllangue
typedictionnaire: ???
codeappelobjet: ???
indexdictionnaire: ???
traductiondictionnaire: Valeur de la clé (traduction)
```

__Exemples__:
```json
{
  numdictionnaire: 1,
  codelangue: 2,
  typedictionnaire: "chart",
  codeappelobjet: 7,
  indexdictionnaire: 1,
  traductiondictionnaire: "Coût (EUR/kW)"
}
```

## tbldictionnairecategories

__Description__ :
```
Les différentes traduction des catégories
```

__Champs__ :
```
numdictionnairecategories: Identifiant
codelangue: foreign key vers tbllangue
typedictionnairecategories: ???
codeappelobjet: ???
indexdictionnairecategories: ???
traductiondictionnairecategories: Traduction de la catégorie pour une clé
```

__Exemples__:
```json
{
  numdictionnairecategorie: 1,
  codelangue: 2,
  typedictionnairecategories: "lang",
  codeappelobjet: 2,
  indexdictionnairecategories: 1,
  traductiondictionnairecategories: "Français"
}
```

## tbljeuxsecteur

__Description__ :
```
???
```

__Champs__ :
```
numjeuxsecteur: Identifiant
codereference: foreign key vers tblreference
coderegion: foreign key vers tblregion
codesecteur: foreign key vers tblsecteur
```

__Exemples__:
```json
{
  numjeuxsecteurs: 1,
  codereference: 1320,
  coderegion: 2,
  codesecteur: 2
}
```

## tbljeuxtechno

__Description__ :
```
???
```

__Champs__ :
```
numjeuxtechno: Identifiant
codereference: foreign key vers tblreference
coderegion: foreign key vers tblregion
codesecteur: foreign key vers tbltechno
```

__Exemples__:
```json
{
  numjeuxsecteurs: 1,
  codereference: 2791,
  coderegion: 1,
  codetechno: 2
}
```

## tblfavoris

__Description__ :
```
Les favoris de l'utilisateur
```

__Champs__ :
```
numfavoris: Identifiant
typefavoris: Le type du favoris
codeappelobjet: ???
iduser: L'identifiant de l'utilisateur
```

__Exemples__:
```json
{
  numfavoris: 1,
  typefavoris: "ref",
  codeappelobjet: 2862,
  iduser: 1
}
```

## tblfinancement

__Description__ :
```
???
```

__Champs__ :
```
numfinancement: Identifiant
codemecanisme: foreign key vers tblmecanisme
codesimul: foreign key vers tblsimul
reffinancement: Référence à un financement
datedebutfinancement: Date du début du financement
datefinfinancement; Date de fin du financement
coderegion: foreign key vers tblregion
codeceetheme: foreign key vers tblceetheme
codearretecee: foreign key vers tblarretecee
codetravaux: ???
codereference: foreign key vers tblreference
newsfinancement: ???
codelicense: foreign key vers tbllicense
availablelangue: Langue disponible (foreign key vers tbllangue ?) 
```

__Exemples__:
```json
{
  numfinancement: 2,
  codemecanisme: 2,
  codesimul: 7,
  reffinancement: "AGRI-EQ-01",
  datedebutfinancement: 2007-11-22 00:00:00,
  datefinfinancement: null,
  coderegion: 2,
  codeceetheme: 2,
  codearretecee: 4,
  codetravaux: 4,
  codereference: 2,
  newsfinancement: 1,
  codelicense: 2,
  availablelangue: 2
}
```

## tblfinancementrex

__Description__ :
```
???
```

__Champs__ :
```
numfinancementrex: Identifiant
coderex: foreign key vers tblrex
codemecanisme: foreign key vers tblmecanisme
partfinancementrex: ???
valeurfinancementrex: ???
codemonnaiefinancementrex: foreign key vers tblmonnaie
montantfinancementrex: ???
codeunitemontantfinancementrex: ???
codelicense: foreign key vers tbllicense
```

__Exemples__:
```json
{
  numfinancementrex: 9,
  coderex: 424,
  codemecanisme: 2,
  partfinancementrex: 1,
  valeurfinancementrex: 48318,
  codemonnaiefinancementrex: 2,
  montantfinancementrex: 28422700,
  codeunitemontantfinancementrex: 6,
  codelicense: 3
}
```

## tblfinancementsolution

__Description__ :
```
???
```

__Champs__ :
```
numfinancementsolution: Identifiant
codesolution: foreignkey vers tblsolution
codefinancement: foreign key vers tblfinancement
codelicense: foreign key vers tbllicense
```

__Exemples__:
```json
{
  numfinancementsolution: 2,
  codesolution: 2,
  codefiancement: 101,
  codelicense: 2
}
```

## tblgainrex

__Description__ :
```
???
```

__Champs__ :
```

```

__Exemples__:
```json
{

}
```