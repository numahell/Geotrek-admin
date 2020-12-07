========
OVERVIEW
========

Interface
=========

Modules
-------

Geotrek est composé de différents modules.

**Gestion des sentiers** :

* Tronçons (linéaire entre 2 intersections)
* Sentiers (groupe de tronçons)
* Statuts (physique, foncier, organismes ayant la compétence sentiers, gestionnaires des travaux et de la signalétique)
* Aménagements (ouvrages et équipements)
* Signalétique
* Interventions (travaux)
* Chantiers (groupe d'interventions)

**Valorisation de l'offre touristique** :

* Itinéraires (randonnées)
* POI (points d'intérêt patrimoniaux)
* Services (informations pratiques comme les points d'eau, passages délicats... selon la typologie que vous souhaitez)
* Contenus touristiques (hébergements, restaurants, services, activités de pleine nature, musées, produits labellisés... Vous pouvez créer les catégories que vous souhaitez)
* Evènements touristiques (animations, expositions, sorties...)
* Signalements (problèmes signalés par les internautes sur un itinéraire depuis Geotrek-rando)
* Zones de sensibilité (module non activé par défaut permettant de gérer des zones de sensibilité de la faune sauvage pour les afficher sur Geotrek-rando ou les diffuser avec l'API de Geotrek-admin)

Chaque module est accessible depuis le bandeau vertical. 

Tous les modules sont construits de la même façon : 

* une liste paginée des objets du module
* la possibilité de filtrer la liste ou de faire une recherche libre
* la possibilité d'exporter les résultats en CSV (pour EXCEL ou CALC), en SHAPEFILE (pour QGIS ou ArcGIS) et en GPX (pour l'importer dans un GPS)
* une carte dans laquelle il est possible de naviguer (déplacer, zoomer), d'afficher en plein écran, de mesurer une longueur, d'exporter une image de la carte, de réinitialiser l'étendue, de zommer sur une commune ou un secteur et de choisir les couches à afficher

.. image :: /images/user-manual/01-liste-fr.jpg

Au survol d'un objet dans la liste, celui-ci est mis en surbrillance sur la carte. 

Au survol d'un objet sur la carte, celui-ci est mis en évidence dans la liste.

La liste des résultats est filtrée en fonction de l'étendue de la carte affichée.

C'est aussi depuis un module qu'il est possible d'ajouter de nouveaux objets.

Un clic sur un objet dans la liste ou la carte permet d'accéder à la fiche détaillée de celui-ci.

Fiches détails
--------------

A partir de chaque module, il est possible d'afficher la fiche détail d'un objet en cliquant sur celui-ci dans la liste ou la carte du module. Les objets de chaque module peuvent ainsi être affichés individuellement dans une fiche détail pour en consulter tous les attributs, tous les objets des autres modules qui intersectent l'objet, les fichiers qui y sont attachés et l'historique des modifications de l'objet. 

Depuis la fiche détail d'un objet, il est aussi possible d'exporter celui-ci au format ODT, DOC ou PDF. 

Selon les droits dont dispose l'utilisateur connecté, il peut alors modifier l'objet. 

Pictogrammes
============

Les pictogrammes contribués dans Geotrek doivent être au format :

* SVG (de préférence, cela permet de conserver la qualité en cas de redimensionnement) ou PNG,
* SVG pour les thèmes (afin de permettre un changement de couleur pour les thèmes sélectionnés),

Il doivent :

* Avoir un viewport carré afin de ne pas être déformés sur le portail,
* Ne pas déborder du cercle inscrit pour les pratiques et les catégories de contenus touristiques, en prévoyant une
  marge si nécessaire.
* Avoir une dimension minimale de 56x56 pixels en ce qui concerne les PNG

Si vous utilisez Inkscape, vous devez définir une viewBox. Voir http://wiki.inkscape.org/wiki/index.php/Tricks_and_tips#Scaling_images_to_fit_in_webpages.2FHTML

Afin de s'intégrer au mieux dans le design standard, les couleurs suivantes sont recommandées :

* Blanc sur fond transparent pour les pratiques et les catégories de contenus touristiques,
* Gris sur fond transparent pour les thèmes,
* Blanc sur fond orange pour les types de POI.
