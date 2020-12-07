===============================
Modules de gestion des sentiers
===============================

Geotrek-admin comporte un certain nombre de modules de gestion des sentiers (tronçons, sentiers, statuts, aménagements, signalétique, interventions et chantiers).

Les tronçons sont les éléments de base sur lesquels s'appuient l'ensemble des objets des autres modules, en utilisant la segmentation dynamique (https://makina-corpus.com/blog/metier/2014/la-segmentation-dynamique).

Les modules signalétique et aménagement ont initialement été conçus dans une logique d’inventaire avec des possibilités de description basiques et génériques. Pour tout complément, il est possible d’attacher un ou plusieurs fichiers joints à chaque objet (photos, PDF, tableurs…).

Les modules interventions et chantiers ont été conçus de façon à permettre à la fois un inventaire et un suivi des travaux (prévisionnel, administratif et financier).

En termes de structuration, le choix initial a été de concevoir, sur le volet gestion, la gestion des valeurs des listes déroulantes structure par structure pour que chaque structure travaillant sur une même Geotrek-admin puisse avoir des typologies différentes (types de signalétique, d’aménagements, d’organismes...). Néanmoins depuis la version 2.20 de Geotrek-admin, il est possible de partager des typologies entre les différentes structures en ne renseignant pas ce champs. 

Lors de la saisie d'un objet sur la carte, il est possible d'afficher une couche SIG ou un relevé GPX sur la carte lors de la création d'un objet sur la carte pour pouvoir le visualiser et le localiser sur la carte (``Charger un fichier local (GPX, KML, GeoJSON)``).

Les tronçons
============

C'est le socle essentiel et central de Geotrek. Un tronçon est un objet linéaire, entre 2 intersections. Le mécanisme de ségmentation dynamique permet de ne pas devoir le recouper pour y rattacher des informations.

Il peuvent être numérisés dans Geotrek-admin, mais il est conseillé des les importer, directement en SQL dans la base de données ou depuis QGIS (https://makina-corpus.com/blog/metier/2014/importer-une-couche-de-troncons-dans-geotrek).

Si ils sont numérisés directement dans Geotrek-admin, il est possible d'afficher sur la carte un fichier GPX ou GeoJSON pour faciliter leur localisation.

Quand un nouveau tronçon intersecte un tronçon existant, ce dernier est découpé automatiquement à la nouvelle intersection. 

En plus de leur géométrie, quelques informations peuvent être associées à chaque tronçon (nom, départ, arrivée, confort, source, enjeu d'entretien, usage et réseaux). 

Comme pour les autres objets, les informations altimétriques sont calculées automatiquement grace au MNT présent dans la base de données. 

Idem pour les intersections automatiques avec les zonages (communes, secteurs, zonages réglementaires) et les objets des autres modules qui sont intersectés automatiquement à chaque ajout ou modification d'un objet.

Comme pour tous les modules, il est possible d'exporter la liste des tronçons affichés (CSV, SHP ou GPX) ou bien la fiche complète d'un tronçon (ODT, DOC ou PDF). 

Comme pour tous les modules, il est aussi possible d'attacher des documents à chaque tronçon depuis sa fiche détail (images, PDF, tableurs, ZIP...).

Enfin, toujours depuis la fiche détail d'un tronçon, il est possible d'en afficher l'historique des modifications.

Les sentiers
============

Il s'agit d'un ensemble linéaire composés d'un ou plusieurs tronçons (entiers ou partiels) grâce à la segmentation dynamique.

Les sentiers permettent d'avoir une vision de gestionnaire sur un linéaire plus complet que les tronçons (qui sont découpés à chaque intersection) pour en connaitre les statuts, la signalétique, les aménagements, les interventions ainsi que les itinéraires et POI. Il est d'ailleurs possible d'ajouter une intervention sur un sentier complet directement depuis la fiche détail d'un sentier.

A ne pas confondre avec le module Itinéraires qui permet de créer des randonnées publiées sur un portail Geotrek-rando. 

Les statuts
===========

Ils permettent de renseigner des informations sur le linéaire (type physique, statut foncier, organismes ayant la compétence sentiers, gestionnaires des travaux et de la signalétique) sans avoir à le faire tronçon par tronçon grâce à la segmentation dynamique qui permet de localiser le départ et l'arrivée sur un ou plusieurs tronçons. 

Les aménagements
================

Ils permettent d'inventorier les aménagements sur les sentiers (passerelles, mains courantes, cunettes, soutenements, bancs, parkings...) en les localisant, les typant, les décrivant, renseignant leur état et leur année d'implantation.

Les types d'aménagement sont découpés en 2 catégories (Ouvrages et Equipements). Ce découpage n'est utilisé que pour filtrer les aménagements.

Il est possible de créer une intervention directement depuis la fiche détail d'un aménagement. 

Comme pour les autres modules, il sont intersectés avec les autres modules pour en connaitre l'altimétrie, les zonages (communes, réglementation...), les statuts (fonciers, physique, gestionnaire), les interventions, les itinéraires...

Il est aussi possible de les exporter, de leur attacher des fichiers (images, PDF, tableurs, ZIP...) et d'en consulter l'historique des modifications.

La signalétique
===============

Ils sont construits de la même manière que les aménagements et sont actuellement stockés dans la même table (``gestion.a_t_amenagement`` avec ``gestion.a_b_amenagement.type = S``). Ils ont donc les mêmes informations et fonctionnalités. 

Les interventions
=================

Les interventions permettent d'inventorier et suivre les travaux réalisés sur les sentiers. Chaque intervention correspond à une action sur un tronçon, sentier, aménagement ou signalétique. 

Les interventions peuvent être localisées directement sur le linéaire de tronçon en les positionnant grâce à la segmentation dynamique. Ou bien ils peuvent correspondre à un sentier, un aménagement ou une signalétique en les créant depuis leur fiche détail.

Une intervention peut être souhaitée (demandée par un agent), planifiée (validée mais à réaliser) ou réalisée. 

Un enjeu peut être renseigné pour chaque intervention. Il est calculé automatiquement si un enjeu a été renseigné au niveau du tronçon auquel l'intervention se raccroche. 

Chaque intervention correspond à un type. On peut aussi renseigner si celle-ci est sous-traitée, les désordres qui en sont la cause, la largeur et la hauteur. La longueur est calculée automatiquement si il s'agit d'une intervention linéaire mais est saisie si il s'agit d'une intervention ponctuelle. 

Plusieurs interventions peuvent être rattachées à un même chantier pour avoir une vision globale de plusieurs interventions correspondant à une opération commune. 

L'onglet Avancé du formulaire permet de renseigner des informations financières sur chaque intervention (coût direct et indirect lié au nombre de jours/agents dissocié par fonction).

Les chantiers
=============

Les chantiers permettent de grouper plusieurs interventions pour en avoir une vision globale et d'y renseigner globalement des informations administratives (Contraintes, financeurs, prestatires, cout global, maitrise d'ouvrage...) et éventuellement d'y attacher des documents (cahier des charges, recette, plans...).

Leur géométrie est la somme des géométries des interventions qui les composent.
