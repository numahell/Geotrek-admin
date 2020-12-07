=========
CHANGELOG
=========

2.42.1.dev0
-------------------

**Bug fixes**

-


2.42.0 (2020-12-04)
-------------------

**New Feature**

- Minimal outdoor module (see documentation to enable)

**Bug fixes**

- Fix API v2 swagger


2.41.2 (2020-11-27)
-------------------

**Bug fixes**

- Do not create point edges on zone borders (fix some crash when adding paths)
- Enable postgis_raster extension when creating a new DB in Ubuntu 20.04 package

**WARNING!**

- Geotrek Ubuntu repository changed to managed two versions (18.04 and 20.04) in parallel.
  If you already installed Geotrek Ubuntu package before you should run once
  'sudo apt-get update  --allow-releaseinfo-change' to accept these changes.


2.41.1 (2020-11-25)
-------------------

**Bug fixes**

- Fix publish ubuntu 20.04/18.04


2.41.0 (2020-11-25)
-------------------

**New Feature**

- Allow to install geotrek on ubuntu 20.04 and 18.04

**Maintenance**

- Upgrade from Django 2.2 to Django 3.1

**Minor Changes**

- Names of file in shapefiles changed

**Bug fixes**

- Truncate attachment legend too long in AttachmentParserMixin


2.40.1 (2020-11-23)
-------------------

**Bug fixes**

- Fix dive pictogram (fix PDF crash)

**Minor Changes**

- Remove language from user profile. Now you can switch language from menu.
- More API v2 improvements (trek endpoint, new API_IS_PUBLIC setting)

**Doc improvements**

- Update translation


2.40.0 (2020-11-18)
-------------------

**New Features**

- Handle different file formats in loadpoi command (all formats supported by gdal)
- Improve API V2 filters and endpoints

**Bug fixes**

- Fix tooltip hidden on module bar (change layout mode to display flex)

**Doc improvements**

- Reorganize index
- Add sphinx container for dev mode
- Improve custom dist to give right templates of values in parameters


2.39.1 (2020-10-28)
-------------------

**Bug fixes**

- Fix delete draft permission should allow use delete button


2.39.0 (2020-10-27)
-------------------

**New Features**

- Modification of API V2 routes
- Add some filtering on Treks in API V2

**Doc improvements**

- Fix doc development command line
- Improving docs : advanced configuration / synchronisation


2.38.6 (2020-10-20)
-------------------

**Bug fixes**

- Fix middleware interfaces without ipv4

**Minor Changes**

- Pictogram for trek's label is optional


2.38.5 (2020-10-20)
-------------------

**New Features**

- Create new label for trekking, move inside_park to this label


2.38.4 (2020-10-16)
-------------------

**New Features**

- Add relation between a Report and a Trek
- Change Report mail template to link the related Report in admin

**Minor Changes**

- Handle Z coordinates on GPX files
- Force size pictograms in admin

**Doc improvements**

- Add info about what's new in 2.33
- Change commands and so according to 2.33 [camillemonchicourt]
- Fix doc about spatial extent setting


2.38.3 (2020-10-05)
-------------------

**Bug fixes**

- Fix diving levels display on lists
- Fix scrollable leaflet right control layer
- Fix lists in csv (#2286)

**Doc improvements**

- Add doc for translating
- Update synchronization with sync_rando options (Thanks JeanLenormand)

**New Feature**

- Show booklet pdf version on detail view


2.38.2 (2020-09-24)
-------------------

**Bug fixes**

- Fix APIDAE parser when there is no element
- Fix booklet generation with pdfimpose

2.38.1 (2020-09-22)
-------------------

**Bug fixes**

- Fix USE_BOOKLET_PDF setting


2.38.0 (2020-09-21)
-------------------

**New Feature**

- Add facebook informations on target Portals
- Add description and title on target Portals
- Synchronize multiple meta informations with target portals.
- Add booklet pdfs with setting USE_BOOKLET_PDF

**Bug fixes**

- Fix stake deletion list
- Fix generation of stake automatically created with factories

**Minor changes**

- Fix use of screamshotter and convertit for development
- Use official postgis docker image
- Change of legend size on pdfs

**Doc fixes**

- Update suricate configuration doc
- Update anonymize report documentation


2.37.0 (2020-09-16)
-------------------

**Bug fixes**

- Fix script install

**New Feature**

- Add second external id api v2 for treks


2.36.1 (2020-09-04)
-------------------

**Bug fixes**

- Fix crash in json DEM generation if the topology is a point


2.36.0 (2020-09-01)
-------------------

**New Feature**

- Allow to (un)publish some cities/district/areas on Geotrek-rando/mobile


2.35.1 (2020-08-24)
-------------------

**Bug fixes**

- Really add an id field to each SQL view


2.35.0 (2020-08-21)
-------------------

**New Feature**

- Allow for custom SQL to be run at install/upgrade

**Bug fixes**

- Add an id field to each SQL view to allow QGIS to open them


2.34.0 (2020-07-10)
-------------------

**New Feature**

- Add reservation system/id fields to treks to allow itinerancy online booking
- Add category code (used in Geotrek-rando) to categories list in admin

**Minor changes**

- Add install scripts for Ubuntu packages

**Bug fixes**

- Fix icons display in categories list in admin


2.33.13 (2020-07-01)
--------------------

**New Feature**

- Add fields to reports for Suricate support
- Add helper to send report to Suricate API on save, if setting `SURICATE_REPORT_ENABLED` is `True`


2.33.12 (2020-06-23)
--------------------

**Bug fixes**

- Change doc flatpages-flatpages.jpg to png
- Fix line topologies create path
- Fix svg's fixtures wich cannot be tranform as png with cairosvg
- Fix duration's filter mobile
- Fix report email OSM coords

**New Feature**

- Synchro mobile get only used practice, themes, networks ...


2.33.11 (2020-06-05)
--------------------

**Bug fixes**

- Fix long attachments name synchro


2.33.10 (2020-06-02)
--------------------

**Bug fixes**

- Fix migration is_image 0011_attachment_add_is_image

**New Feature**

- Allow to clean attachments not used anymore (clean_attachments)


2.33.9 (2020-06-02)
-------------------

**Bug fixes**

- Fix small treks profile


2.33.8 (2020-05-22)
-------------------

**Bug fixes**

- Fix package install if geotrek user already exists
- Attachment download error breaks global import


2.33.7 (2020-05-18)
-------------------

**Bug fixes**

- Show blades without line in signage detail page
- Fix information desks editing
- Fix trek and POI filtering


2.33.6 (2020-05-14)
-------------------

**Bug fixes**

- Don't overwrite initial data in existing database on first install


2.33.5 (2020-05-13)
-------------------

**Bug fixes**

- Add a scrollbar to signage and blade forms
- Fix city affectation for looping paths
- Fix attachment download with redirection
- Fix logout next page
- Fix blade/line creation crash
- Fix lines layout in blade detail page

**Upgrade notes**

If you installed version 2.33.3 before (no matter if you upgrade directly or from 2.33.4),
you should get errors like "django.db.utils.ProgrammingError: column "deleted" of relation signage_blade".
To fix them, run ``sudo geotrek migrate --fake signage 0016;``.


2.33.4 (2020-05-04)
-------------------

**Minor changes**

- Improve blade CSV export

**Bug fixes**

- Fix ordering of blades
- Fix empty attachment link in admin list
- Fix some french translations
- Fix redirections when downloading attachments in parsers
- Fix migrations when DB contains a deleted blade
- Fix stdout flush in sync commands

**Maintenance**

- Upgrade from Django 2.0 to Django 2.2
- Fix deprecation warnings


2.33.3 (2020-04-28)
-------------------

No changes. Just force a new build in CI


2.33.2 (2020-04-28)
-------------------

No changes. Just force a new build in CI


2.33.1 (2020-04-28)
-------------------

No changes. Just force a new build in CI


2.33.0 (2020-04-28)
-------------------

**BREAKING CHANGES**

- New installation method (Ubuntu packaging)
- Alternative installation method (Docker, for experts only)
- Remove name field from feedback report, to be GDPR compliant
- Rename functions, triggers and sequences in database

**Bug fixes**

- Fix timeout when saving long treks (increase computation performances)
- Fix mecanism to put tables in postgresql schemas
- Better download errors handling in parsers
- Make sure signage and related blade have the same related structure

**Maintenance**

- Upgrade from Django 1.11 to Django 2.0

**New features**

- Allow to attach interventions to blades, paths, trails, treks, POIs and services in addition to infrastructures and signages
- Allow to merge dropdown list items in admin. Check them in list view and choose "Action: Merge"
- Add a django command to erase email from feedback reports after 365 days

**Upgrade notes**

- The installation method has been totally rewritten with an Ubuntu packaging (``apt install geotrek-admin``), only available for Ubuntu 18.04 actually. 
- If you upgrade from Geotrek-admin <= 2.32, then apply the dedicated migration script. See https://geotrek.readthedocs.io/en/master/installation.html#upgrade-from-geotrek-admin-2-32. 
- Geotrek-admin is now automatically installed in ``/opt/geotrek-admin/`` directory and the advanced configuration file moved to ``/opt/geotrek-admin/var/conf/custom.py``. See advanced configuration documentation for details. 
- The automatic NGINX configuration can be overriden in ``/opt/geotrek-admin/var/conf/nginx.conf.in`` file. See NGINX configuration documentation for details.


2.32.11 (2020-03-17)
--------------------

**Minor changes**

- Add UML digrams of data model to documentation
- Remove URL in weblinks dropdown
- Move ambiance after description teaser

**Bug fixes**

- Fix a WeasyPrint warning
- Fix zoning filters on path


2.32.10 (2020-03-11)
--------------------

**Bug fixes**

- Fix POI, touristic contents and touristic events sort in mobile v3 API
- Change Lambert93 signage coordinates format
- Fix TourInSoftparser with # inside <MoyenDeCom> values
- Show File and URL fields as required in attachement form
- Do not show Function field as required in Intervention form
- Do not show Amount and Organism fields as required in Project form


2.32.9 (2020-03-06)
-------------------

**Bug fixes**

- Fix "upper bound of FOR loop cannot be null" crash in SQL triggers


2.32.8 (2020-03-05)
-------------------

**Minor changes**

- Allow to choose Touristic content ordering in API
- Add external ID to projects and interventions

**Bug fixes**

- Fix the modification of the published field without the "Can publish…" permission


2.32.7 (2020-03-02)
-------------------

**BREAKING CHANGES**

- Rename tables and fields in database

**Minor changes**

- Retry on HTTP 503 errors in parsers

**Bug fixes**

- Fix install on Xenial (again)
- Fix video embed url https
- Fix "Only LINESTRING and MULTILINESTRING are supported" crash in SQL triggers


2.32.6 (2020-02-28)
-------------------

**DO NOT USE IT!**


2.32.5 (2020-02-18)
-------------------

**Bug fixes**

- Fix filters sort in mobile v3 API


2.32.4 (2020-02-12)
-------------------

**Bug fixes**

- Fix install on Xenial


2.32.3 (2020-01-27)
-------------------

**Bug fixes**

- Fix review, publish do not display after resave a published or without permission to publish
- Fix attachment asterisks and crispy form
- Display only one time the same path when on trail detail


2.32.2 (2020-01-09)
-------------------

**Bug fixes**

- Upgrade WeasyPrint


2.32.1 (2019-12-20)
-------------------

**Bug fixes**

- Fix a crash in stake computation when adding an intervention
- Fix a crash in project list when one of them has no end year
- Fix drapping with no-data DEM values
- Fix nav pills to choose language in forms


2.32.0 (2019-12-13)
-------------------

**New features**

- Add DISPLAY_SRID into settings to allow user to choose it's own format for GPS coordinates
- Make some fields optional (class Trail, Intervention, Project, OrdererdTrekChild, POI)
- Sort dropdown lists
- Document settings


2.31.0 (2019-12-06)
-------------------

**New features**

- Sync mobile data from web UI
- The SHOW_LABELS setting allows to hide status labels on map


2.30.0 (2019-11-26)
-------------------

**Breaking changes**

- Remove support of Ubuntu 14.04 Trusty

**Maintenance**

- Move from Python 2 to Python 3

**Bug fixes**

- Fix PDF generation for not published treks


2.29.15 (2019-11-12)
--------------------

**Bug fixes**

- Fix install (use a version of venusian that is compatible with Python 2)


2.29.14 (2019-11-04)
--------------------

**Bug fixes**

- Do not check structure for excluded POIs


2.29.13 (2019-10-30)
--------------------

**Minor changes**

- Do not set structure by default when creating elements in dropdown lists.
- Trek duration is now optional
- Automatically disable empty filters in API for mobile v3
- Add support for Tourinsoft v3 in addition to v2
- Add more links form/to sensitive areas
- Add more unit tests

**Bug fixes**

- Fix SEO for static page titles
- Fix TouristicContentParser deletion having type1/2 with same values
- Fix serialization of MultiPolygon sensitive areas


2.29.12 (2019-10-23)
--------------------

**Minor changes**

- Show completeness on dive detail page
- Add practice field to trek and dive completeness

**Bug fixes**

- Fix multiple sensitive areas on treks with settings SENSITIVE_AREA_INTERSECTION_MARGIN = 0
- Fix multiple sensitive areas on dives


2.29.11 (2019-10-17)
--------------------

**Bug fixes**

- Fix filter still available after come back to list
- Add settings allowing to change permission on voluminous datas. Voluminous datas are not stocked at the same place


2.29.10 (2019-10-08)
--------------------

**Minor changes**

- Do not set username as attachment author by default

**Bug fixes**

- Don't crash sync_rando with PIL.Image.DecompressionBombError
- Fix mode selection when adding/editing an attachment
- Fix authenticated parsers


2.29.9 (2019-10-02)
-------------------

**Bug fixes**

- Fix sync_rando : sensitive area with multi polygons


2.29.8 (2019-09-26)
-------------------

**Minor Changes**

- Increase path name field length

**Bug fixes**

- Fix csv_display signage with not ascii character


2.29.7 (2019-09-25)
-------------------

**Minor Changes**

- Add pois services tourism on sync_rando
- Add endpoints api for diving

**Bug fixes**

- Fix is_public() call checking if the object is ppublic or not.
- Remove duplicate description detail diving


2.29.6 (2019-09-19)
-------------------

**Bug fixes**

- Fix sync_rando command with diving


2.29.5 (2019-09-13)
-------------------

**Bug fixes**

- Sync POIs related to dives
- Fix sync of manual PDF (again)


2.29.4 (2019-09-09)
-------------------

**Minor Changes**

- Add reviews in dives module

**Bug fixes**

- Fix length should be length_2d in pdfs


2.29.3 (2019-08-28)
-------------------

**Minor Changes**

- Allow to override nginx port in etc/settings.ini

**Bug fixes**

- Fix sync of manual PDF


2.29.2 (2019-08-28)
-------------------

**Minor Changes**

- Add a command to import dives

**Bug Fixes**

- Fix crash when a dive is not a point


2.29.1 (2019-08-26)
-------------------

**Minor Changes**

- Show treks related to dives

**Bug fixes**

- Fix retrieval of content-length of attachments with HTTPS
- Fix detection of hardcoded SRID in migrations
- Fix Est/West swap in diving module
- Fix version of more-itertools
- Fix missing difficulty and technical levels in dive detail page and PDF


2.29.0 (2019-08-20)
-------------------

**New features**

- Diving module (optional, see manual to enable)

**Minor Changes**

- Improve mobile sync
- Do not automatically zoom over level 16

**Bug fixes**

- Fix black map screenshots (after a manual cache deletion)
- Fix related POI order with dynamic segmentation disabled


2.28.0 (2019-08-09)
-------------------

**New features**

- Geotrek without dynamic segmentation is back

**Minor Changes**

- Add a settings allowing to remove certain items from the left menu
- Serve attachment with 'Topoguide' type as public PDF

**Bug fixes**

- Fix missing pictograms for mobile app
- Translate feedback acknoledgment email
- Fix sync_mobile command for itinerancy


2.27.12 (2019-07-22)
--------------------

**Minor Changes**

- Add itinerancy mobile


2.27.11 (2019-07-17)
--------------------

**Minor Changes**

- Change condition's on_delete for SET_NULL
- Add the possibility to add Multipoint with one Point on commands loadinfrastructure/loadsignage

**Bug fixes**

- Fix choices fields, should only take in account existing (not deleted) elements
- Fix delete Organism
- Fix sensitivity parser with MultiPolygon
- Fix profile and languages


2.27.10 (2019-07-10)
--------------------

**Minor Changes**

- Set OpenTopoMap as default map background
- Resize information desk type pictograms in mobile API

**Bug fixes**

- Fix delete intervention type


2.27.9 (2019-07-01)
-------------------

**Minor Changes**

- Add ambiance field to trek detail endpoint in mobile API


2.27.8 (2019-06-28)
-------------------

**Minor Changes**

- Add primary color setting for PDF
- Allow to override practices pictogram color in custom trek PDF template


2.27.7 (2019-06-26)
-------------------

**Bug fixes**

- Fix public PDF overflow
- Resize category and POI pictograms for mobile app
- Convert pictograms from SVG to PNG for mobile app
- Fix structure (or not) related scrolldowns validation
- Remove unvisible paths in remove_duplicate_paths command
- Fix list of additional layers in layer selector
- Don't reset excluded POIs when saving treks

**Minor Changes**

- Allow to merge multiple comment columns when importing paths
- Add color field to touristic contents categories (for mobile app only)
- Handle invalid geometries when importing districts


2.27.6 (2019-06-04)
-------------------

**Bug fixes**

- Fix mobile API


2.27.5 (2019-05-29)
-------------------

**Bug fixes**

- Fix regulatory sensitive area parser
- Fix handling of parser errors


2.27.4 (2019-05-27)
-------------------

**Bug fixes**

- Fix crash with --srid option of loadpaths command
- Add option portal in sync_mobile for the treks
- Fix encoding error on watermarks
- Fix bad references to sync_mobile in sync_rando command


2.27.3 (2019-05-23)
-------------------

**New features**

- Allow to set order of filters in mobile API
- Add ascent and district filters to mobile API

**Minor Changes**

- Replace text by an id in url of pictures with watermarks
- Change default settings watermark

**Documentation**

- Add PDF overriding section


2.27.2 (2019-05-14)
-------------------

**Minor Changes**

- Add points_reference by treks in api mobile

**Bug fixes**

- Remove public pdf poi
- Fix filter cities without paths


2.27.1 (2019-05-06)
-------------------

**Bug fixes**

- Fix api mobile with only sensitivity app


2.27.0 (2019-05-02)
-------------------

**New features**

- Add watermark on pictures
- Allow to change structure of an object with permission by_pass_structure

**Bug fixes**

- Fix a floating point computation problem in SQL trigger
- Fix trails in detail of intervention and opposite
- Fix color on restricted area


2.26.5 (2019-04-19)
-------------------

**Bug fixes**

- Add slug to mobile API
- Fix crash with empty images


2.26.4 (2019-04-18)
-------------------

**Bug fixes**

- Fix migration tourism 0004


2.26.3 (2019-04-12)
-------------------

**Bug fixes**

- Fix parsers delete datas

**Minor Changes**

- Add command loaddistrict, loadcities, loadpaths


2.26.2 (2019-04-10)
-------------------

**Bug fixes**

- Fix sync_rando command (BadZipfile exception)
- Fix nginx and Django conf when SSL is enabled
- Fix restricted area layers


2.26.1 (2019-04-03)
-------------------

**Bug fixes**

- Fix blade form
- Fix sync_mobile, sync_rando with url https and http


2.26.0 (2019-04-01)
-------------------

**New features**

- New API for mobile app v3

**Bug fixes**

- Fix signage type pictograms
- Some cosmetics on tourism detail pages (clickable links)
- Fix Tourinsoft opening period parsing (multiple periods)
- Fix Bad Status Line exception


2.25.3 (2019-03-26)
-------------------

**Bug fixes**

- Fix Tourinsoft parsers one time again (practical info for events)


2.25.2 (2019-03-26)
-------------------

**Bug fixes**

- Fix Tourinsoft parsers again (postal address)


2.25.1 (2019-03-25)
-------------------

**Bug fixes**

- Fix Tourinsoft parsers


2.25.0 (2019-03-25)
-------------------

**New features / Performances**

- Add the possibility to load layers (do not load them automatically)

**Minor changes**

- Add Touristic Content TourInSoft Parser
- Add tool testing ign keys without ggp3

**Documentation**

- How to update IGN urls


2.24.8 (2019-03-15)
-------------------

**Bug fixes**

- Fix bug parsers filetype not related with structure


2.24.7 (2019-03-13)
-------------------

**Minor changes**

- Add elevation on sensible areas

**Bug fixes**

- Fix retry sync_rando tiles when tiles does not exist (landez 2.4.1)


2.24.6 (2019-03-07)
-------------------

**Bug fixes**

- When updating interventions, stake field is no more required
- Fix duplicates in year filters in intervention module
- Configurable blade code
- Allow letters in blade number
- Improve signage templates
- Add "On signage/infrastructure" filter on intervention list


2.24.5 (2019-03-06)
-------------------

**Performances**

- Add index to date_update columns


2.24.4 (2019-03-01)
-------------------

**Bug fixes**

- Fix get attachments with crop


2.24.3 (2019-02-28)
-------------------

**Bug fixes**

- Fix get attachments using generic foreign and not url
- Fix merge path


2.24.2 (2019-02-26)
-------------------

**Bug fixes**

- Fix attachments and history linked with signage and infrastructure


2.24.1 (2019-02-12)
-------------------

**Bug fixes**

- Fix install.sh (pin cairocffi version)
- Fix routing on paths with sharp angles
- Fix loadrestrictedareas command
- Fix altimetry on straight portions of paths
- Various signage fixes

**Performances**

- Allow client side caching with systematic revalidation for Layer, JsonList and graph views
- Remove validation of history bar
- Don't bringToFront() every single feature on map
- Do not show bullets at path extremities anymore by default.
  Set SHOW_EXTREMITIES setting to True in custom.py enable them.
- Remove networks and trails columns in path list


2.24.0 (2019-01-28)
-------------------

**New features**

- Bulk path deletion


2.23.0 (2019-01-24)
-------------------

**New features**

- Signage blades management
- Add gpx and kml export for path detail view
- Allow to load local GPX/Geojson file in list views

**Bug fixes**

- Fix sensitive areas API v2
- Fix migrations if infrastructure app not is not installed


2.22.10 (2019-01-09)
--------------------

**Bug fixes**

- Fix duplicated results in API v2 with sensitive area filters


2.22.9 (2019-01-09)
-------------------

**Minor changes**

- Separate Infrastructure and Signage models
- Create parser touristic event for apidae
- Refactor ApidaeParser

**Bug fixes**

- Add italian translations that are visible on Geotrek-rando
- Fix permissions attachments paperclip

**Performances**

- Improve map's performances


2.22.8 (2019-01-03)
-------------------

**Minor changes**

- Now, empty portal field means "all portals" instead of "no portal"


2.22.7 (2019-01-03)
-------------------

**Bug fixes**

- Fix command loadinfrastructure


2.22.6 (2019-01-02)
-------------------

**Minor changes**

- Index path draft field
- Add eid field to load_infrastructure command
- Add loadrestrictedarea command
- Install postgis package


2.22.5 (2018-12-19)
-------------------

**Bug fixes**

- Fix DB migration


2.22.4 (2018-12-19)
-------------------

**Bug fixes**

- Replace \u2028 and \u2029 by \n in synced (geo)json files (fix Geotrek-mobile crash)

**Minor changes**

- Add EID field to all models and increase its length


2.22.3 (2018-12-14)
-------------------

**Bug fixes**

- Don't publish deleted infrastructures/signages
- Add default pictograms to published infrastructures/signages


2.22.2 (2018-12-10)
-------------------

**Bug fixes**

- Fix bugs with HTTPS access
- Fix for some modules to edit attributes and not the geometry

**Minor changes**

- add options to sync signages and infrastructures
- sync global signages and infrastructures


2.22.1 (2018-11-27)
-------------------

**Bug fixes**

- Fix trekking form with pois_excluded
- Give the possibility to get type of infrastructures and signages without structure


2.22.0 (2018-11-27)
-------------------

**New features**

- Allow to publish signage and infrastructure
- Allow to exclude POIs from a trek
- New access rights to edit draft path
- New access rights to edit attributes and not the geometry
- Allow to remove duplicate path in database : command remove_duplicate_paths

**Bug fixes**

- Fix snap on crossing point : take all paths easier
- Fix a clash between current url and SYNC_RANDO_OPTIONS
- Fix screamshotter when SSL is enabled


2.21.1 (2018-09-18)
-------------------

**Breaking changes**

- Remove type1 from trek API when SPLIT_TREKS_CATEGORIES_BY_PRACTICE is not set
- Rename Trek category label to Hike in API. You can override this in
  geotrek/locale/<language code>/LC_MESSAGES/django.po files

**Bug fixes**

- Fix crash in log entries view

**Minor changes**

- Save column sort by module
- Rename SITRA to APIDAE


2.21.0 (2018-09-04)
-------------------

**New features**

* Path deletion warning page now shows linked topologies
* Allow to add Dailymotion video attachments
* Add a command to unset structure in lists of choices and group choices
  with the same name

**Bug fixes**

* Fix Sync_rando View
* Fix loaddem
* Fix creation of Youtube/Soundcloud attachments
* Fix cancellation when editing geometries
* Show which structure choices are related to
* Add confort and stake filters to path list
* Fix sync of touristic contents for mobile app


2.20.1 (2018-07-16)
-------------------

**Bug fixes**

* Fix Completed Filter in Touristic Event

2.20.0 (2018-06-27)
-------------------

**New features**

* Allow to share glossaries between structure (just keep structure field empty)
* Allow to import infrastructures, not only signages
* Allow to split treks by itinerancy
* Path deletion does not delete the related point topologies anymore. Instead point topologies are linked to the nearest
  remaining path.
* Keep inode and mtime when synced file don't change

**Minor changes**

* Optional img-responsive class on flatpage images

**Bug fixes**

* Fix virtualenv install
* Upgrade celery to 4.1.1
* Fix the bug which remove a path when we merge 2 paths with a 3rd path on the point of merge. (ref  #1747)


2.19.1 (2018-05-28)
-------------------

**Bug fixes**

* Update APIDAE API URL
* Fix filename encoding errors in import


2.19.0 (2018-05-22)
-------------------

**Minor changes**

* Allow to specify encoding when importing data


2.18.5 (2018-05-07)
-------------------

**Bug fixes**

* Fix related structure when creating new objects

**Minor changes**

* Show related structure on all detail pages


2.18.4 (2018-05-02)
-------------------

**Bug fixes**

* Fix sync of deleted sensitive areas
* Fix touristiccontents.geojson crash when reservation_system is None

**Minor changes**

* Add Ubuntu 18.04 Bionic Beaver support


2.18.3 (2018-04-27)
-------------------

**Bug fixes**

* Fix imports when enabling only sensitivity app


2.18.2 (2018-04-27)
-------------------

**Preventive maintainance**

* Upgrade to Django 1.11
* Upgrade several python dependencies

**Minor changes**

* Allow user with can_bypass_structure permission to set or update the related
  structure on sensitive areas

**Bug fixes**

* Put back filter widgets in two columns (#1663)
* Do not include (possibly forged) structure field in post requests
* Fix geojson format in sensitive areas API
* Fix filtering by practices in sensitive areas API
* Fix sync_rando when sensitivity app is not enabled
* Adapt BiodivParser to API modifications
* Order sensitive areas by decreasing area in API to be able to clic on each of them
* Set ownership in parsers depending on logged user
* Pagination requires ordering in v2 API


2.18.1 (2018-03-26)
-------------------

**Bug fixes**

* Fix distribution of tables in schemas
* Allow to reset type1/type2 in TouristicContentSitraParser

**Minor changes**

* Do not truncate install.log


2.18.0 (2018-03-22)
-------------------

**Breaking changes**

* Drop support of Ubuntu Precise 12.04, please upgrade to
  Trusty 14.04 or Xenial 16.04 before upgrading Geotrek-admin

**Preventive maintainance**

* Upgrade to Django 1.9
* Upgrade several python dependencies

**Bug fixes**

* Fix path duplication in path split trigger

**Minor changes**

* Show total path length in path list


2.17.3 (2018-03-23)
-------------------

** Bug fixes **

* Fix install


2.17.2 (2018-02-07)
-------------------

**Minor changes**

* Use id rather than french name for practices and structure in sensitive areas API
* Add permission to import sensitive areas


2.17.1 (2018-02-02)
-------------------

**Minor changes**

* Implantation year on signages and infrastructures is now a filter with current existing values
* Trek form field 'practice' is moved to first panel
* Add sensitive areas to public trek PDF
* Do not show paths on PDF
* Add SENSITIVE_AREA_INTERSECTION_MARGIN setting

**Bug fixes**

* Fix snapping
* Fix import of sensitive areas when languages lists do not match
* Fix trail links in project detail view
* Add 'approved' field in touristic content and event exports
* Fix service type with specials character in trek detail
* Fix bbox filtering in sensitive areas API
* Add CORS header to sensitive areas API
* Filter on spatial extent when importing from Biodiv'sport
* Fix celery task runner version


2.17.0 (2018-01-15)
-------------------

**New features**

* Sensitive Areas


2.16.1 (2018-01-10)
-------------------

**Bug fixes**

* Fix encoding errors while generating static versions of rando pages
* SEO for static versions of rando pages
* Disable template caching (fix ODT generation)


2.16.0 (2017-12-21)
-------------------

**New features**

* Create static versions of rando pages with opengraph data (Facebook)
* Add external id field to POI form

**Bug fixes**

* Fix download of python packages for pypi.python.org (SSL is now required)
* API v2 : Fix full URL pictures in nested serializers
* Fix network SVG (add viewbox) to make them visible in Geotrek-rando
* Hide file parsers form if no one is available


2.15.2 (2017-09-28)
-------------------

**Bug fixes**

* Fix existing path split in particular cases where postgis doesn't see real intersections.
* Fix project and intervention detail template.
* Fix synchronization of POI media other than images
* Include pois, parking and reference points to compute PDF map zoom


2.15.1 (2017-08-23)
-------------------

**New features**

* Add es translation for PDF
* Add mailssl setting

**Bug fixes**

* Fix APIDAE import illustrations
* Fix double import parsers
* Fix cirkwi export
* Select only published POIs in GPX and KML files
* Remove deprecated experimental setting
* Fix HTML tags & entities in feedback email


2.15.0 (2017-07-13)
-------------------

**New features**

* API v2 Beta 1. Optimized multilingual filtered endpoints for paths, treks, tours and pois.
* See HTML doc and examples in /api/v2/. Authentication with Basic HTTP (https://en.wikipedia.org/wiki/Basic_access_authentication).
* Don't use it in production without HTTPS

**Bug fixes**

* Fix pdf default public templates (weasyprint)
* Fix screamshotter standalone install (map screenshots)


2.14.3 (2017-07-03)
-------------------

**Bug fixes**

* Cirkwi export fixes and improvements


2.14.2 (2017-06-21)
-------------------

**Bug fixes**

* Fix attachments edition


2.14.1 (2017-06-22)
-------------------

**Bug fixes**

* Refactor signals pre / post migrate according Django 1.8
* Update translations
* Fix path splitting
* Fix AutoLogin Middleware with mapentity 3.1.4


2.14.0
------

**WARNING!**

* Upgrade to version 2.14.0 is only possible from version 2.13.0

**New features**

* Upgrade to Django 1.8. This is a big step, migrations are reset, please backup before upgrade.
* Ability to skip attachment download in parsers and use external links.

**Minor changes**

* Possibility to exclude pois in cirkwi xml export by adding ?withoutpois=1 to url (http://XXXXX/api/cirkwi/circuits.xml?withoutpois=1
* Add MOBILE_TILES_EXTENSION setting (for compatibility with old mobile apps, set it to 'png')
* API optimization
* Disable auto size for service icon in trek description.

**Bug fixes**

* Fix topologies and cities intersections


2.13.0 (2017-03-02)
-------------------

**Minor changes**

* MOBILE_TILES_URL settings is now a list which can be used to merge
  different layers in mobile application


2.12.0 (2017-02-16)
-------------------

**New features**

* add loadsignage command

**Minor changes**

* add field implantation_year to model BaseInfrastructure
* add field owner to model LandEdge
* add field agreement to model LandEdge


2.11.5 (2017-02-06)
-------------------

**Bug fixes**

* Fix topologies and cities intersections


2.11.4 (2017-02-01)
-------------------

**Bug fixes**

* Remove deprecated datasource (replaced by import parsers)
* Stop install.sh if make update or wget fails
* Create database with right owner if user exists but database does not
* Make sure supervisor service is started after install
* Fix HTML entities in feedback email
* Fix cirkwi export for treks with multilinestring geom

**Minor changes**

* Add filter usages on paths
* Add filters name and description on infrastructures and signages
* Add picture to PDF for feedback reports (only in Weasyprint mode)


2.11.3 (2016-11-15)
-------------------

**Bug fixes**

* Upgrade mapentity (fix map centering in PDF exports)
* Fix cirkwi export when trek geom is not a linestring


2.11.2 (2016-09-15)
-------------------

**Bug fixes**

* Do not synchronize not-published treks with published but deleted parents
* Allow to specify portal in touristic content parsers
* Fix import of type1 in HebergementsSitraParser
* Fix source and portal missing in shapefile exports

**Performances**

* Improve performances of DEM computation for huge treks


2.11.1 (2016-08-17)
-------------------

**Minor changes**

* Fix slug URL for "oe" ligature
* Improve zoom of map captures in PDF


2.11.0 (2016-08-02)
-------------------

**Bug fixes**

* Fix weasyprint install
* Fix label displayed twice with Sitra Parser

**Minor changes**

* Update translations
* Update import documentation
* Record source is no nore structure related

**New features**

* ability to filter synchronized content with different portals


2.10.4 (2016-05-19)
-------------------

**Breaking changes**

* Deprecate MAPENTITY_WEASYPRINT setting. Now public PDF use Weasyprint HTML templates and private PDF use legacy
  ODT template.

**Minor changes**

* Improve altitude profile computation (increase smoothing)
* Improve HTML templates for public exports
* Improve SITRA parser
* Allow to use source variable in PDF templates

**Bug fixes**

* Fix comparison of zip files to keep mtime when nothing changed
* Upgrade simplekml lib (should fix KML exports)


2.10.3 (2016-05-11)
-------------------

**Minor changes**

* Update default pictograms for touristic content categories
* Update default pictograms for themes

**Bug fixes**

* Workaround a bun in supervisor init script
* Fix multilinestring instead of linestring in trek shapefile parser


2.10.2 (2016-04-12)
-------------------

**Minor changes**

* Add source filter to touristic contents/events
* Allow installation as root (not recommended, use with caution)

**Bug fixes**

* Restore contents deleted and then created again in EspritParcParser
* Add a warning if type1/type2 is not created in EspritParcParser
* Replace input by textarea in flatpage form


2.10.1 (2016-03-17)
-------------------

**Bug fixes**

* Allow access to information desks in API (and so to map capture and PDF) for unpublished treks

**Minor changes**

* Parsers improvements


2.10.0 (2016-03-03)
-------------------

**New features**

* Add support for Ubuntu 15.04 Vivid

**Breaking changes**

* Remove TileCache service (you should set up tiles source with LEAFLET_CONFIG variable in `geotrek/settings/custom.py` now)
* Run supervisor as root (you should now run `sudo supervisorctl` instead of `./bin/supervisor`)
* Move nginx and supervisor logs to system dir `/var/log/`

**Minor changes**

* Update default pictograms for difficulty levels

**Bug fixes**

* Fix sync_rando after deleting a trek with children


2.9.3 (2016-02-25)
------------------

**Bug fixes**

* Fix line break at start of contact in EspritParcParser

**Minor changes**

* Add parameters.json and themes.json files to API


2.9.2 (2016-02-17)
------------------

**Minor changes**

* Increase web link size

**Bug fixes**

* Fix path split
* Fix attachment parsing with same document type for several structures


2.9.1 (2016-02-10)
------------------

**Bug fixes**

* Don't forget to sync touristic contents/events media when skipping PDF
* Don't delete attachments of other objects when importing
* Don't delete other objects when constant fields are set in parsers


2.9.0 (2016-02-04)
------------------

**New features**

* Add parser for brand "Esprit Parc National"

**Bug fixes**

* Set user structure as related structure for all new objects


2.8.1 (2016-01-29)
------------------

**Bug fixes**

* Synchronize information desk thumbnails


2.8.0 (2016-01-28)
------------------

**New features**

* Use POI pictures in PDF if the trek has no picture itself
* Use a placeholder in PDF if there is no picture
* Parser to import touristic contents from SITRA
* Add list of all information desks to API

**Bug fixes**

* Allow NULL values for id_externe fields in database
* Fix missing elements (eg. POI enumeration) on trek map capture
* Prevent overlaping controls at bottom of list view
* Translation of column names in shapefiles export
* UTF-8 and truncated alerts in shapefile export


2.7.2 (2016-01-26)
------------------

**Bug fixes**

* Synchronize touristic events with no end date
* Fix PDF synchronization (eg. missing list of POI)


2.7.1 (2016-01-18)
------------------

**Bug fixes**

* Fix random z-index on forced layer polygon
* Fix pretty duration


2.7.0 (2016-01-14)
------------------

**New features**

* New button to add Youtube videos in flat pages

**Bug fixes**

* Fix iframe inclusion in flatpages.
* Fix double column buttons in gridmanager.
* Fix validation on flatpages for combo external_url + content.
* Fix responsive layout for provided templates in flatpages.
* Fix event link to closest visible path only
* Do not log anymore an error when submitting a form with an empty geometry


2.6.0 (2015-12-30)
------------------

**New features**

* Customization of practices ordering

**Bug fixes**

* Synchronize record source pictograms
* Add buttons to attachment update form
* Fix timestamps in database when connection with timezone other than UTC


2.5.2 (2015-12-29)
------------------

**Bug fixes**

* Fix hyphenation language in public PDF templates
* Add parents to trek public PDF template
* Fix numbering style in trek public PDF template
* Show points of reference over other features on trek detail map


2.5.1 (2015-12-18)
------------------

**Bug fixes**

* Trek public PDF fixes (size of service pictos, style of numbered lists, stages)


2.5.0 (2015-12-08)
------------------

**New features**

* Order has been added to flatpages which is reflected in the export for geotrek-rando frontend.
* Added 2 templates buttons for flatpages creating two layouts
* Option to add pois pictures to trek ones in Geotrek-Rando

**Bug fixes**

* Generate tiles zip files for all children of published treks
* Fix URL of video/audio media in API
* Fix default filtering of past touristic events in UI


2.4.4 (2015-12-02)
------------------

**Bug fixes**

* Show pending import/sync tasks

2.4.3 (2015-11-27)
------------------

**Bug fixes**

* Fix filtering by source in sync_rando for flatpages and tiles too


2.4.2 (2015-11-26)
------------------

**Bug fixes**

* Fix permissions of sync rando output directory
* Fix filtering by source in sync_rando


2.4.1 (2015-11-25)
------------------

**Bug fixes**

* Condition field of infrastructures is no more required
* Fix zipfile detection at import.
* Fix error handling at import (raise exception to browser).


2.4.0 (2015-11-18)
------------------

**New features**

* Paths can be merged
* Add trek parents to API
* Allow to sync public web site from web interface
* Add begin and end dates to touristic events list
* Filter conmpleted touristic events by default

**Bug fixes**

* Prevent concurrent imports and/or synchronization
* Fix rendering of HTML markup in weasyprint templates
* Fix missing publication field in some cases


2.3.0 (2015-11-09)
------------------

**New features**

* Sync rando now synchronizes touristic contents and events.
* Sync rando now exports only future events based on current date.
* Sync rando now synchronizes touristic content categories.

**Bug fixes**

* Added a custom validation to accept url only contribution in flatpages without content.
* Sync rando now handles crashes when it calls django views.


2.2.0 (2015-10-09)
------------------

**New features**

* Added normalisation for altimetry's json export
* Clarify 2D/3D lengths (fixes #1400)

**Bug fixes**

* Change plural on accessibility label for admin filter


2.1.0 (2015-09-29)
------------------

**Breaking changes**

* Instead of storing the parent of a trek, Geotrek now stores the children of a trek.
  This allows to use the same trek in several parents and to order them.
  WARNING! Existing parent/child relation are lost. You will have to set them
  again after upgrade. Fixes #1479

**New features**

* Add trek infos (aka services for now)
* Add email sent to reporting user after submit
* Handle multiple reservation systems (fixes #1488)
* Add an option to sync_rando to filter by source (fixes #1480)
* Add add condition field to infrastructure table (fixes #1494)
* New Geotrek logo

**Bug fixes**

* Reload supervisor configuration after Geotrek upgrade
* Fix projection of waypoints in GPX exports
* Prevent unnecessary save for geom fields if they are not updated.
  This prevents triggering geom recalculation in postgres.
* Fix crash in case of missing or invalid picture
* Fix feedback API
* Unzip eggs to fix templates not found error
* Various parsers (import system) fixes and improvements

**Documentation**

* Document server migration


2.0.0 (2015-07-20)
------------------

**Breaking changes**

* Rework API URL schemas

**New features**

* Static API to disconnect Geotrek-rando from Geotrek-Admin (fixes #1428)
* Build zip files for mobile application
* Trek / Touristic content association distance depending on trek practice
* Option to hide published treks nearby topologies
* Add previous/next treks and category slugs to geojson API
* Add external id in trekking/tourism detail pages and exports
* Zip touristic contents as POI for mobile app v1
* Add external id field on Path
* Order intersections in Geotrek light mode
* Add reservation id field for touristic contents
* Integration of WeasyPrint to generate PDF from HTML/CSS instead of ODT

**Bug fixes**

* Remove HTTP calls to SoundCloud API at serialization
* Allow DEM to partially cover spatial extent


0.35.1 (2015-07-17)
-------------------

**Bug fixes**

* Fix installation on ubuntu 12.04 with recent updates


0.35.0 (2015-07-10)
-------------------

**New features**

* Add an import framework

**Bug fixes**

* Fix a crash in appy pod (PDF generation)
* Fix login with restricted access to some contents
* Fix buildout bootstrap arguments


0.34.0 (2015-05-20)
-------------------

**New features**

* Itinerancy (parent/children treks)
* Allow to choose ordering of categories for Geotrek-Rando
* Bootstrap grid editor for flatpages
* Approved touristic contents and events
* Option to split trek category by practice or accessibility

**Bug fixes**

* Fix duration notation
* Flatten altimetry profiles

**Bug fixes**

* Show accessibility in trek detail page (fixes #1399)


0.33.4 (2015-04-07)
-------------------

**Bug fixes**

* Ensure trek duration is a positive number
* Fix cirkwi exports (second try)
* Fix public PDF templates


0.33.3 (2015-04-01)
-------------------

**Bug fixes**

* Fix systematic crash in PDF conversions


0.33.2 (2015-04-01)
-------------------

**Bug fixes**

* Remove italian from fixtures
* Fix crash when generating two PDF in parallel


0.33.1 (2015-03-25)
-------------------

**Bug fixes**

* Fix flat pages crash
* N to N source field (rel #1354)


0.33.0 (2015-03-25)
-------------------

**Breaking changes**

* A new permission "Can publish ..." is required to publish treks, pois,
  touristic contents and touristic events. Grant it to your users and groups if
  need be
* DB table ``l_b_source`` is renamed as ``l_b_source_troncon``

**New features**

* Publication workflow (fixes #1018)
* Allow to add links to Youtube or Soundcloud media as attachment
* Make pictograms optional in some places when not required by Geotrek-Rando
* Add source for treks, touristic contents and touristic events (fixes #1354)
* Add external id field for treks, pois, touristic contents and touristic events
* Group cirkwi matchings in admin site (fixes #1402)

**Bug fixes**

* Fix projection of OSM link in feedback email
* Fix language in cirkwi exports


0.32.2 (2015-03-06)
-------------------

**Bug fixes**

* Home now redirects to treks list in light version (without topologies)
* Fix Cirkwi export in light version
* Fix SRID in database migrations
* Add signage type filter again (fixes #1352)
* Add missing date filters to touristic events list


0.32.1 (2015-03-04)
-------------------

**Bug fixes**

* Fix creation of a loop topology with two paths (fixes #1026)


0.32.0 (2015-03-04)
-------------------

**New features**

* Export to cirkwi/espace loisirs IGN. After upgrade, run
  ``bin/django loaddata cirkwi`` to load data cirkwi tags and categories
* Wysiwyg editor for static web pages

**Bug fixes**

* Hide not published static pages in public REST API


0.31.0 (2015-03-02)
-------------------

**New features**

* Add support of Ubuntu 14.04 to installer
* Public PDF for touristic contents/events (fixes #1206)
* Add treks close to other treks in REST API
* Add pictograms for trek accessibilities, touristic content types and
  touristic event types

**Bug fixes**

* Show edit button when having bypass structure permission
* Export missing fields in list exports (fixes #1167)
* Fix formating of float and boolean values in list exports (fixes #1366, #1380)
* Fix french translation
* Allow anonymous access to altimetry API for public objects
* Hide not published and deleted items in public REST API


0.30.0 (2015-02-19)
-------------------

**Breaking changes**

* Trek practice (formerly usage) is no single valued so if a trek has multiple
  usages only one will be kept after upgrade. Others will be **lost**!
* After upgrade, run ``make load_data`` to load fixtures for accessibilities or
  create them by hand. You should clean-up the list of practices by hand.
* Don't forget to set up permissions to administrate practices and
  accessibilities.

**New features**

* Split trek usage field into practice and accessibility
* Treks and POIs are now structure related
* Allow anonymous access to media related to published items
* Check model read permission to give access to media
* Add a settings to set up CORS (cross-origin resource sharing)
* Allow to get POIs for a specific trek in REST API
* Consistent REST API (type1, type2, category for treks, touristic contents and
  touristic events)

**Bug fixes**

* Ensure path snapping is done on the closest point and is idempotent
* Fix language of PNG elevation charts
* Fix logo on login page
* Fix logs rotation
* Fix permissions creation


0.29.0 (2015-02-04)
-------------------

**New features**

* GeoJSON API with all properties for Trek and Tourism

**Bug fixes**

* Fix permissions required to sync static Web pages
* Fix geom computation on line topologies with offset


0.28.8 (2014-12-22)
-------------------

**Bug fixes**

* Fix altimetry sampling for segment with 0 length (rel #1337)


0.28.7 (2014-12-22)
-------------------

**Bug fixes**

* Fix altimetry trigger when TREKKING_TOPOLOGY_ENABLED is set to False


0.28.6 (2014-12-18)
-------------------

**Bug fixes**

* Fix 3D length shorter than 2D length (run sql command ``UPDATE l_t_troncon SET geom=geom;`` after upgrade to update altimetry informations of existing geometries)
* Fix translation of "Information desks" in public trek PDF
* Fix prepare_map_images and prepare_elevation_charts commands failing for deleted objects and for objects without geom


0.28.5 (2014-12-09)
-------------------

**Bug fixes**

* Fix DEM optimizations when minimum elevation is zero (fixes #1291)
* Fix regression for translations of tourism (fixes #1315)
* Fix duplicate entries with year filter (fixes #1324)

**Documentation**

* French user manual first step about general interface

**New features**

* Set PostgreSQL search_path at user level (fixes #1311)
* Show 3D and 2D length in detail pages (fixes #1101)
* Show length and elevation infos in trail and all statuts detail pages (fixes #1222)
* Show trail length in list and exports (fixes #1282)
* Replace stake by length in path list (fixes #956, fixes #1281)
* Add subcontracting in intervention filter (fixes #1144)
* Add missing fields in project filter (fixes #219, fixes #910)
* Show status in interventions table among detail pages (fixes #1193)
* Add missing field in projects exports (ref #1167)
* Add length column to land module lists
* Number of workers and request timeout can be now configured in ``settings.ini``
* Various improvements on trek public template, by Camille Monchicourt


0.28.4 (2014-11-21)
-------------------

**Bug fixes**

* Fix mouse position indicator on ``/tools/extents/`` page when map tiles have Google projection
* Fix missing filters in trails list (fixes #1297)
* Fix infrastructure main type filter (fixes #1096)
* Fix flatpage creation without external url in adminsite
* Fix path detail page where deleted objects were shown (fixes #1302)
* Fix position of POIs on trek detail maps (fixes #1209)
* Fix TinyMCE not preserving colors (fixes #1170)
* Raise validation error instead of crashing when submitted topology is empty (fixes #1272)

**Documentation**

* Fix mention of MAP_STYLES (ref #1226)

**Changes in experimental features**

* Renamed *usage* to *type* in touristic events (fixes #1289)


0.28.3 (2014-11-12)
-------------------

**Bug fixes**

* Fix upload form author/legend format (fixes #1293)
* Fixes history list (ref #1276)
* Prevent email to be sent twice on conversion error. Use info instead.
* Fix paperclip translations missing (fixes #1294)
* Fix filetypes not being filtered by structure (fixes #1292)
* Fix apparence of multiple-choices in forms (fixes #1295)


0.28.2 (2014-11-05)
-------------------

**Bug fixes**

* Fix upgrade of django-leaflet to 0.15.0 (overlay layers)
* Fix apparence of overlay layers for tourism when experimental features are disabled
* Fix plural in tourism translation
* Fix unit tests
* Run this command to set the default information desk type with the original pictogram
  (or select a pictogram from the adminsite)

::

    cd Geotrek-0.28.2/

    curl "https://raw.githubusercontent.com/makinacorpus/Geotrek/v0.27.2/geotrek/trekking/static/trekking/information_desk.svg" > var/media/upload/desktype-info.svg


0.28.1 (2014-11-05)
-------------------

**Bug fixes**

* Fix deployment when tourism is not enabled
* Fix default duration when invalid value is filled (fixes #1279)
* Fix year filters for intervention, infrastructure and project (fixes #1287)
* Fix list filters not being restored (fixes #1236)


0.28.0 (2014-11-04)
-------------------

**Breaking changes**

* Before running install, run this SQL command to add a column for file attachments :

::

    ALTER TABLE fl_t_fichier ADD COLUMN marque boolean DEFAULT false;


**New features**

* Information desks now have a type (*Maison du parc*, *Tourist office*, ...)
  with the ability to set dedicated pictograms (fixes #1192).
* Ability to control which picture will be used in trek, using clicks on
  stars in attachments list (fixes #1117)
* Ability to edit attachments from detail pages directly (fixes #177, the 5th oldest issue!)
* Add missing columns in intervention exports (fixes #1167)
* Add ability (for super-admin) to add/change/delete zoning objects in Adminsite (ref #1246)
* Add ability to have paths records in database that will not appear in Geotrek
  lists and maps. Just set column ``visible`` to false in ``l_t_troncon`` table.
* Add ability to add external overlay tile layers (fixes #1203)

**Bug fixes**

* Fix position of attachment upload form on small screens
* Clearer action message in object history table
* Prevent image ratio warning from disappearing (fixes #1225)
* Touristic contents
* Touristic events

**Internal changes**

* Upgraded Chosen library for dropdown form fields
* Set ``valide`` column default value to false on paths table ``l_t_troncon`` (fixes #1217)
* All information desks are now available in GeoJSON (*will be useful to show them
  all at once on Geotrek-rando*).
* All tables and functions are now stored in different schemas. It allows to
  distinguish Geotrek objects from *postgreSQL* and *PostGIS*, and to grant user privileges
  by schema. It is also easier to browse objects in *pgAdmin* and *QGis*.

  **Caution**: if you created additional database users, you may have to change their ``search_path``
  and/or their ``USAGE`` privilege.

**Experimental features**

* We introduced models for touristic contents and events. In order to load
  example values for categories and types, run the following commands:

::

    bin/django loaddata geotrek/tourism/fixtures/basic.json
    cp geotrek/tourism/fixtures/upload/* var/media/upload/

* We introduced models for static pages, allowing edition of public static Web pages
  from Geotrek adminsite.

In order to enable those features under construction, add ``experimental = True`` in
``etc/settings.ini``. Note that none of them are used in *Geotrek-rando* yet.

:notes:

    Give related permissions to the managers group in order to allow edition
    (``add_flatpage``, ``change_flatpage``, ``delete_flatpage``,
    ``add_touristiccontent`` ...).


0.27.2 (2010-10-14)
-------------------

**Bug fixes**

* Fix elevation info not being computed when intervention is created (ref #1221)
* Fix list of values for infrastructure and signage types (fixes #1223)
* Signages can now be lines if setting SIGNAGE_LINE_ENABLED is True (fixes #1141)
* Fix HTML tags in PDF exports (fixes #1235)
* Fix regression with Geotrek light


0.27.1 (2010-10-13)
-------------------

**Bug fixes**

* Fix problems in forms, prevent Javascript errors


0.27.0 (2010-10-09)
-------------------

**Breaking changes**

* Attribute for single information desk was removed (was used in **Geotrek-rando** < 1.29)
* Renamed setting ``TREK_PUBLISHED_BY_LANG`` to ``PUBLISHED_BY_LANG``
* Renamed setting ``TREK_EXPORT_MAP_IMAGE_SIZE`` to ``EXPORT_MAP_IMAGE_SIZE``,
  ``TREK_EXPORT_HEADER_IMAGE_SIZE`` to ``EXPORT_HEADER_IMAGE_SIZE``
  and ``TREK_COMPLETENESS_FIELDS`` to ``COMPLETENESS_FIELDS``.
  They are now a dictionnary by object type (`see example <https://github.com/makinacorpus/Geotrek/blob/v0.27dev0/geotrek/settings/base.py#L443-L449>`_)

**New features**

* POI publication is now controlled like treks
* POI now have a public PDF too
* Introduced ``VIEWPORT_MARGIN`` setting to control list page viewport margin
  around spatial extent from ``settings.ini`` (default: 0.1 degree)

:notes:

    After upgrading, mark all POIs as published in the languages of your choice ::

        UPDATE o_t_poi SET public_fr = TRUE;
        UPDATE o_t_poi SET date_publication = now();

**Bug fixes**

* Add missing credit for main picture in trek PDF (fixes #1178)
* Paths module is now removed from user interface in *Geotrek-light* mode.
  (i.e. with ``TREKKING_TOPOLOGY_ENABLED = False``)
* Make sure text fields are cleared (fixes #1207)
* Intervention subcontracting was missing in detail pages (fixes #1201)
* Make sure TLS is disabled when ``mailtls`` is False in settings
* Fix list of POIs in path detail pages (fixes #1213)
* Fix highlight from map for project list page (fixes #1180)

**Internal changes**

* Extracted the trek publication to a generic and reusable notion
* Complete refactor of Trek JSON API, now taking advantage of Django REST framework
  instead of custom code
* Added read/write REST API on all entities
* Refactored URLs declaration for altimetry and publishable entities
* Change editable status of topology paths in Django forms, since it was
  posing problems with Django-rest-framework
* Add elevation profile SVG URL in trek detail JSON (fixes #1205)
* Simplified upgrade commands for ``etc/`` and ``var/``, and mention advanced
  configuration file


0.26.3 (2014-09-15)
-------------------

**Bug fixes**

* Fix pretty trek duration when duration is between 24 and 48H (fixes #1188)
* Invalidate projet maps captures when interventions change, and treks maps
  when POIs change (fixes #1181)


0.26.2 (2014-08-22)
-------------------

**Bug fixes**

* Fix search among attached files in Adminsite (fixes #1172)


0.26.1 (2014-08-21)
-------------------

**Bug fixes**

* Upgrade *django-mapentity* for bug fix in ODT export and list of values in
  detail pages


0.26.0 (2014-08-21)
-------------------

**New features**

* Interventions in project detail page is now shown as a simple table (ref #214)
* A generic system for interaction between objects attributes and details map
  was developped. It works with project interactions, topologies paths, etc. (ref #214)
* Show enumeration of interventions in project PDF exports (fixes #960)
* Number of POIs in now limited to 14 items in trek export (ref #1120)
* Number of information desks in now limited to 2 items in trek export (ref #1120).
  See settings ``TREK_EXPORT_INFORMATION_DESK_LIST_LIMIT`` and ``TREK_EXPORT_POI_LIST_LIMIT``
* Justify texts of POIs in trek export, now converted to plain text.
* Trek export geometries are now translucid red by default (see ``MAP_STYLES`` setting) (ref #1120)
* Paths apparence in trek exports are now controlled by MAP_STYLES setting too.
* Images attachments are now resized to 800x800 for publication (instead of 500x500)
* Clarify intervention cost by function and mandays (fixes #1169)

**Bug fixes**

* Fix paths layer not being shown in detail pages (fixes #1161)
* Fix position of point topologies when closest path is not perpendicular (fixes #1156)
* Prevent parking to be cropped on map exports (fixes #1006)

**Upgrades notes**

Since the map export have changed, empty the cache :

::

    rm -rf var/media/maps/*


0.25.2 (2014-08-14)
-------------------

**Bug fixes**

* Fix translation of Job in intervention form (fixes #1090)
* Fix form error when no geometry is provided (fixes #1082)
* Show attachments in adminsite (fixes #1162)
* Fix JSON formatting of object attachment lists in API


0.25.1 (2014-08-01)
-------------------

**Bug fixes**

* Fix Geotrek CSS not being deployed properly
* Fix trek relationships causing errors for PDF export


0.25.0 (2014-08-01)
-------------------

**New features**

* Added projection file EPSG:32622 (fixes #1150)
* Now log addition and suppression of attachments in history
* Added notion of points of reference for treks (fixes #1105).
  (Can be disabled with ``TREK_POINTS_OF_REFERENCE_ENABLED = False``)
* Edit the parking location directly on the trek map (ref #387)
* Show enumeration of POIs in trek PDF exports (fixes #871)

**BUG fixes**

* Fix permission check to see attachments (fixes #1147, ref #1146)
* Fix grouping of interventions in detail pages (fixes #1145)
* Fix project total intervention cost (fixes #958)
* Fix history entries not being saved when using formsets (fixes #1139)
* Fix postal code being saved as integer (fixes #1138). Existing records
  will have a leading zero when shorter than 5 charaters.
* Fix bug when form of intervention on infrastracture is not valid
* Limit height of layer switcher on small screens (fixes #1136)
* Get rid of next parameter when redirecting to login when permission missing (fixes #1142)
* Fix apparence of main menu when permissions are missing to view logbook and admin (ref #1142)

**Internal changes**

* Rework display of lists in detail pages, better factorization
* Removed links in logbook list for certain models
* Display messages in login page too (useful for redirections)
* Support edition of several fields on the same map, via django-leaflet new feature (fixes #53)


0.24.3 (2014-06-27)
-------------------

**BUG fixes**

* Fix cursor not removed when terminating topology (fixes #1134)
* Fix information desk geometry hard-coded SRID


0.24.2 (2014-06-27)
-------------------

**BUG fixes**

* Fix EPSG:32620 projection file
* Fix JS error when path layer is not on map
* Fix start and end markers not shown as snapped on path edition (fixes #1116)
* Fix groups not shown in Adminsite with external authent (fixes #1118)
* Use markers as mouse icons for topology creation, use resize cursors as
  fallback only (fixes #1100)
* Minor changes in trek print template (ref #1120)


0.24.1 (2014-06-26)
-------------------

**BUG fixes**

* Fix SVG files for difficulty pictograms
* Fix group fixtures for "Rédacteurs" (fixes #1128)
* Fix tab "None" in list view (fixes #1127)
* Fix external datasources icons in Admin (fixes #1132)
* Fix information desk maps in Admin forms (fixes #1130)
* Fix topology edition when two forced passages on same path (fixes #1131)

**Minor changes**

* Ordered log entries by date descending (ref #1123)
* Renamed "Data sources" by "External data sources" (fixes #1125)
* Renamed "Foncier" to "Statuts" (fixes #1126)


0.24.0 (2014-06-23)
-------------------

** Breaking changes **

* POI icons shall now have a solid background, since no background is added
  in trek detail map anymore.

* Pictograms fields were added to trek difficulty, route, network. You can use
  the images provided in the ``trekking/fixtures/upload/`` folder.

:notes:

    Just before upgrading, delete the following folders ::

        rm -rf lib/src/django-modeltranslation

    After upgrading, mark all treks as published in the languages of your choice ::

        UPDATE o_t_itineraire SET public_fr = TRUE;
        UPDATE o_t_itineraire SET date_publication = now();


**New features**

* Public TREK export - hide block label if value is empty (fixes #873)
* Add POIs on trek GPX (fixes #774)
* Close list filter when click outside (fixes #916)
* Rename recurrent field to subcontracting on intervention (fixes #911)
* Rename comments field to description on intervention (fixes #927)
* Show object type in ODT export (fixes #1000)
* Show paths extremities on map (fixes #355)
* Ability to reuse topology when adding objects from detail pages (fixes #574, fixes #998)
* Command to generate all elevation charts (fixes #799)
* SITRA support in Tourism datasources (fixes #1064)
* Added status field on feedback reports (fixes #1075)
* Show restricted areas by type in layer switcher (fixes #961)
* Publication status is now controlled by language (fixes #1003). Previous
  behaviour can restored by setting ``TREK_PUBLISHED_BY_LANG``` to False.
* Added publication date on trek (ref #1003)
* Ability to see a trek in the different published languages (ref #1003)
* A trek can now have several information desks (fixes #1001)
* Information desks are now shown in trek detail map (fixes #1001)
* Information desks now have optional photo and position, as well as some
  additional fields (fixes #1001)
* Disabled marker cluster in trek detail map
* Remove background and halo effect on POI icons
* Added 3 new settings to control trek detail map icons size
  (``TREK_ICON_SIZE_POI``, ``TREK_ICON_SIZE_PARKING``, ``TREK_ICON_SIZE_INFORMATION_DESK``)

**Minor features**

* Intervention disorders is not mandatory anymore (fixes #661)
* Improved details in trek form, use Chosen for many-to-many widgets
* Documented the configuration of map layers apparence
* Show layers colors in layer switcher
* Detail page : replace "Maintenance" by "Works" (fixes #889)
* Detail page : interventions on paths are now grouped together,
  and a small icon is shown (fixes #735)
* Detail page : show intervention costs (ref #958, fixes #764)
* Show project intervention total costs (fixes #958)
* Allow to override the Trek public document template
  (see *advanced configuration* in docs)
* Close calendar after date choice in intervention form (fixes #928)
* Renamed Attachment submit button (fixes #925)
* Added a new setting ``PATH_SNAPPING_DISTANCE`` to control paths snapping distance
  in database (default: 1m)
* Allow to disable trails notion (fixes #997)
  (see *advanced configuration* in docs)
* Show POI name on hover instead of category in trek detail pages (fixes #1004)
* Form tabs are now always visible while scrolling (fixes #926)
* New URL to obtain the attached filelist of an object
* Remove float notation in altimetry altitude labels
* Control altimetry profiles font using ``ALTIMETRIC_PROFILE_FONT`` setting
* Add pictograms to routes and networks (fixes #1102)

**Bug fixes**

* Fixed Signage and Infrastructure year filter label (fixes #293)
* Fixed paths layers not always shown below other layers (fixes #912)
* Clarify legend and title for attachments (fixes #888)
* Fixed cannot clear trek fields in database (fixes #1095)
* Fixed missing translation of "Load local file" (fixes #1085)
* POI types are displayed as such in adminsite
* Fix duplicate authors in history list in detail pages

**Internal changes**

* Added pictogram on difficulty, useful for *Geotrek-mobile* (fixes #1109)
* Added experimental *Geotrek-light* support (ref #1019)


0.23.5 (2014-06-19)
-------------------

**Bug fixes**

* Fix crash when TourInFrance has malformed website or phone
* Fix translations not being installed


0.23.4 (2014-06-18)
-------------------

**Bug fixes**

* Fix massive upgrade bug, where new migrations were ignored. Due to migration
  operation introduction in 0.22 installation script.

Special thanks to Noël Martinon, Félix Merzeau, Gil Deluermoz and Camille Montchicourt for their patience on this.


0.23.3 (2014-06-18)
-------------------

** Bug fixes **

* Fix static files compression when using Google Mercator projection in maps
* Fix intermediary points order in topology de/serialization, and remove useless
  topology serialization optimizations (fixes #1031)


0.23.2 (2014-06-13)
-------------------

** Bug fixes **

* Fixed land records not shown in detail pages
* Fixed JSON DEM area extent for treks
* Fixed targets list for tourism datasources (fixes #1091)
* Cache tourism datasources for one day (setting ``CACHE_TIMEOUT_TOURISM_DATASOURCES``)
* Fix crashes with TourInFrance sources
* Add link to OSM in feedback email (fixes #1089, #1093)
* Fix feedback email translation (fixes #1087)
* Fix problem with permission check "read attachment" in detail page (fixes #1092)
* Fix measure control appearing twice in forms (fixes #1078)
* Fix 404 on download buttons from list views
* Fix POI translated fields not tabbed (fixes #1065)
* Fix missing translation of "Add a new POI" (fixes #1086)
* Fix invalid snapping when save path without editing geometry (fixes #1099)
* Add missing properties in feedback report detail page.
* Hide all modules information in report detail page.
* Add missing translations of feedback module.
* Show object type in ODT export (fixes #1000)


** Internal changes **

* Upgraded to Mapentity 1.4.0
* Upgraded to Leaflet 0.7.3

** Installation **

* Fixed content types migration of land to zoning apps (Thanks Noël Martinon)

* UbuntuGIS stable maintainers have *upgraded* (sic) GDAL to 1.10.0.
  Upgrading GDAL is painful, and PostGIS packages may have to be reinstalled
  (data shouldn't be lost though). *Remember it was recommended to run PostGIS
  on a different server*.

:notes:

    On June 2th 2014, the Ubuntu GIS stable repository switched from ``libgdal1``
    to ``libgdal1h``. It broke the deployment script of many projects, including
    *Geotrek*.

    It is a good thing, since it paves the way for the last Ubuntu LTS release (14.04). However, it breaks the *Long Term Support* philosophy of the previous one (12.04), supposed to be supported until 2019.

    **Morality** : we cannot trust the *Ubuntu GIS stable* repository anymore.

    Regarding *Geotrek*, such upgrades of Ubuntu packages is not supposed to be covered
    by its installation script. If you face any problems, please refer to the
    community or commercial support (such as *Makina Corpus* for example).


0.23.1 (2014-05-22)
-------------------

** Bug fixes **

* Fixed regression when editing topologies without modification
* Fixed widget for Trails to allow linear topologies only


0.23 (2014-05-22)
-----------------

** Breaking changes **

Read all release notes carefully.

* Trails are now managed as topologies (fixes #370).
  Existing trails geometries are likely to be **LOST** (*see below*)
* Rename ``mailadmin`` to ``mailadmins`` in ``etc/settings.ini``
* Permission systems has been refactored (*see below*)

** Bug fixes **

* Force browser cache revalidation of geojson data (fixes #843)
* Force browser cache revalidation for path graph (fixes #1029)
* Fix deletion porblems in AdminSite (fixes #1008)
* Trek advised parking and public transport are translatable (fixes #1024)
* Fix missing translation "no filters" and "current criterias" (fixes #884)
* Fix PDF versions of documents not being translated (fixes #1028)

** New features **

* Command to import shapefile with points into POI as topologies (fixes #952)
* Add views to serve DEM on object area as JSON (*Geotrek-Rando 3D*)
* New tourism module : external datasources can be configured from Adminsite (*GeoJSON, TourInFrance, ...*)
  and added to maps (by module, or published on *Geotrek-rando*...)
* Show number of attached files in tab (fixes #743)
* New permission to control download of attachments
* New permission to allow users or groups to bypass structure restrictions
* Add a setting to serve attached files as download (default: True) (fixes #976)
* Track objects creations, changes and deletions (fixes #300)
* Added a reader group (fixes #495)
* Topologies are not recreated if user did not edit field (fixes #833)
* Added static file for projection EPSG:32620
* Show land objects in menu (fixes #942)
* Documented configuration of custom projections (fixes #1037)
* Buttons in the list menu to add new objects easily
* Add fullscreen button on maps (fixes #904)
* Add all controls on detail map (fixes #907)
* Add a button to close filters (fixes #424)
* Added new sections in documention : *FAQ*, *User-manal* and *Advanced configuration*

** Internal changes **

* Enabled database connection pooling in production
* An error is raised if SRID has not unit in meters (fixes #921)
* Zoning and land modules are now splitted (fixes #954)
* Complete refactor of geographical form fields. Now uses *django-mapentity*
  from its own repository instead of internal orphan branch.
* Complete refactor of maps initialization, without inline preprocessed JavaScript
* Rely on Django permissions to control access to detail, list and exports (fixes #675)
* Core and altimetry modules are now splitted (fixes #996)
* Renamed treks POIs GeoJSON properties

:notes:

    * Before upgrading, backup your trail records and geometries, using pgAdmin ::

        CREATE TABLE backup_sentiers AS SELECT * FROM l_v_sentier;
        CREATE TABLE backup_troncons_sentiers AS (
          SELECT l_t_troncon.id AS troncon, l_t_sentier.id, l_t_sentier.nom
          FROM l_t_troncon, l_t_sentier
          WHERE l_t_sentier.id = l_t_troncon.sentier
        );

    * Before upgrade, rename ``mailadmin`` to ``mailadmins`` and add
      a new line ``mailmanagers`` in ``etc/settings.ini``. See *Email settings*
      section in documentation.

    * Just before upgrading, delete the following folders  ::

        rm -rf lib/src/django-modeltranslation lib/src/mapentity

:notes:

    * After upgrading, load the default permissions of the previous groups, otherwise
      users won't have access to their modules ::

        bin/django loaddata geotrek/authent/fixtures/minimal.json
        bin/django loaddata geotrek/authent/fixtures/basic.json

    * After upgrading, make sure *Active* is checked for the user *__internal__*
      otherwise screenshotting won't work.

    * After upgrading, load basic data for the new module ::

        bin/django loaddata geotrek/feedback/fixtures/basic.json

    * After upgrading, make sure the user specified in *Geotrek-rando* is
      in the group *Geotrek-rando*, or has at least the following permissions
      in the AdminSite :

      - ``paperclip | attachment | Can read attachments``
      - ``trekking | Trek | Can read Trek``
      - ``trekking | Trek | Can export Trek``
      - ``trekking | POI | Can read POI``
      - ``trekking | POI | Can export POI``
      - ``feedback | Report | Can add report``

    * After upgrading, compare visually the resulting migrated trails using QGis,
      by opening both layers ``l_v_sentier`` and ``backup_sentiers``.


0.22.6 (2014-04-27)
-------------------

* Remove hard-coded mentions of EPSG:2154 in database initial
  migrations (fixes #1020)
* Fix version download and unzip in installation script.

Thanks Noël Martinon, from Guadeloupe National Park, for reporting both issues.


0.22.5 (2014-03-19)
-------------------

* Fix compilation of translations (ref #970)
* Fix distinction between languages and translated languages (fixes #968)
* Fix history tabs not being shown after upgrade to Django 1.6 (fixes #975)
* Fix regression on land layer label colors (fixes #980)
* Fix attached files not shown after file upload/delete (fixes #933)
* Fix links being removed from trek descriptions (fixes #981)
* Fix missing thumbnail in trek and POI detail pages
* Fix black background on map captures (fixes #979)
* Increased scale text size on map captures (fixes #850)
* Show map attributions on map captures (fixes #852)
* Fix aspect ratios of map in trek public documents (fixes #849)
* Fix objects list not being filtered on map extent (fixes #982)
* Fix coherence of map layer when text search in objects list (fixes #702)
* Fix number of results not refresh on text search (fixes #865)

* Added north arrow in map image exports (fixes #851)
* Removed darker effect on backgrounds for map image exports, and added internal
  advanced setting ``MAPENTITY_CONFIG['MAP_BACKGROUND_FOGGED'] = True``


0.22.4 (2014-03-06)
-------------------

* Fix install.sh not compiling locale messages (fixes #965)
* Moved trek completeness fields to setting `TREK_COMPLETENESS_FIELDS`. Duration
  and difficulty were added, arrival was removed (fixes #967)
* Fix regression about source locale messages (fixes #970)
* Fix regression link `Back to application` lost from adminsite (fixes #971)
* Serve uploaded files as attachments (fixes #972)
* Remove help texts being shown from filter forms (fixes #966)
* Fix form pills for translated languages (fixes #968)

0.22.3 (2014-02-17)
-------------------

* Fix install.sh help not being shown
* Fix screenshots being empty if deployed behind reverse proxy with rool url (fixes #687)
* Fix GPX file layer circle marker size (fixes #930)
* Remove JS libraries from login page
* Fix install.log being removed during installation
* Fix execution characters being shown during DB backup prompt
* Fix PhantomJS and CasperJS installation and deployment
* Added more automatic frontend tests
* Default allowed hosts is now `*`

0.22.2 (2014-02-14)
-------------------

* Fix secured media URLs when using a non empty `rooturl` setting
* Fix proxy errors by disabling keep-alive (fixes #906)

0.22.1 (2014-02-13)
-------------------

* Prevent install script to delete existing media files from disk
  in some situations.

0.22 (2014-02-12)
-----------------

**Before upgrade**

* Backup your database.
* If you upgrade in the same application folder, first delete the `geotrek`
  sub-folder.
* Use `install.sh` to upgrade (`make deploy` won't be enough)
* After upgrade, make sure the following query returns only ~23 results:

    SELECT COUNT(*) FROM south_migrationhistory;


**BREAKING changes**

* For upgrades, Geotrek 0.21 is required.
* Uploaded files are now restricted to authenticated users (fixes #729)

:notes:

    *Geotrek-rando* 1.23 or higher is required to synchronize content.

**NEW features**

* In list view, click on map brings to detail page, mouse over highlights in list.
* Show path icon if intervention is not on infrastructure (fixes #909)
* Add spanish translation
* Add photographie into default attachments filetype
* Map location combobox (Cities, Districts, Areas) are not shown if empty or disabled.
* Several database views have been created (fixes #934)
* Remove dots from path icon (fixes #939)
* Intervention, infrastructure and project filters list of years is now dynamic (fixes #948)
* Application available languages (*english*, *french*, *italian*, *spanish*) are now
  distinct from translated content languages (`languages` value in :file:`settings.ini`)

Minor changes

* Improved apparence of map controls
* Improved apparence of path intermediary points
* Improved apparence of form validation buttons
* Add auto-generated docs at /admin/doc/
* Nicer installation script output

Installation script

* Scan and ortho attributions can now be set using `scan_attributions` and
* Propose to backup DB before Geotrek upgrade (fixes #804)
* Settings edition prompt only happens at first install
  `ortho_attributions` in *settings.ini*.

**BUG fixes**

* Fix convert urls behind reverse proxy with prefix
* Fix deployment problem if ``layercolor_others`` not overidden in settings.ini
* Fix topology kinds to be 'INTERVENTION' for intervention without signage/infrastructure
* Fix restricted areas types display in admin (fixes #943)
* Fix list ordering of trek relationships and web links (fixes #929)
* Fix nginx log files being already empty after logrotate (fixes #932)
* Fix project add button when no permission

:notes:

  List of restricted areas is not shown on map by default anymore. Restore
  previous behaviour with advanced setting `LAND_BBOX_AREAS_ENABLED` as True.

**Internal changes**

* Upgrade to Django 1.6 (fixes #938)
* Upgrade to Leaflet 0.7
* Upgrade a great number to python and JavaScript libraries
* An internal user (with login permission) is used to authenticate the Conversion
  and Capture services.
* Installation script is modular (standalone, geotrek only, ...)
* Developement server now listens on all interfaces by default
* Database migrations were resetted, no postgres `FATAL ERROR` message will
  be emitted on fresh install anymore (fixes #937). See *Troubleshooting* in documentation.


0.21.2 (2014-02-04)
-------------------

**BUG fixes**

* Warn on tiling landscape/portrait spatial extent only if map with local projection
* Safety check on thumbnailing if images are missing from disk (*useful for troubleshooting,
  when importing existing dumps*).
* Fix overlapping filter if no records present (fixes #931)


0.21.1 (2013-12-11)
-------------------

**Improvements**

* Smooth DEM drapping, improving altimetric information and profiles (fixes #840, ref #776)

**BUG fixes**

* Signage forms are now restricted by structure (fixes #917)
* Fix geometries computation when path split occurs on return topology (fixes #899)
* Add title on links in list views (fixes #913)
* Prevent horizontal scroll on forms, caused by textareas (fixes #914)
* Fix empty 3d geometry of point topologies with offset (fixes #918)

:notes:

    In order to recompute all paths topologies altimetry information, you can perform
    the following queries:

       ``UPDATE l_t_troncon SET geom = geom;``
       ``UPDATE e_t_evenement SET decallage = decallage;``

    Reading information from rasters is costly. Be prepared to wait for a while.


0.21 (2013-11-28)
-----------------

**Improvements**

* Increase height of multiple select (fixes #891)
* Add project field in intervention filter (fixes #896)
* Many minor improvements for infrastructures in adminsite (fixes #886)
* Add category in intervention filter (fixes #887)

**BUG fixes**

* Fix KML coordinates not being in 3D.
* GPX now has trek description (fixes #775)
* Order overlapping topologies by order of progression (fixes #777)
* Improved TinyMCE configuration, for resize and cleanup (fixes #351, #711)
* Changed trek duration interval for notion of days (fixes #880)
* Show city departure in trek public export (fixes #881)
* Document customization of TinyMCE config (fixes #882)
* Fix 404 error on path delete (fixes #900)
* Fix project constraints not being displayed in details (fixes #893)
* Fix organism translation in project form (fixes #892)
* Fix apparence of forms on small screen (fixes #744, #902)
* Fix modify button being hidden to editors (fixes #901)
* Fix overlap between map controls and label (fixes #883)
* Fix translation of district in list filters (fixes #890)
* Fix integrity error on land intersection on path update (fixes #897)
* Fix form layout problems (fixes #712, #879)

0.20.9 (2013-10-30)
-------------------

* Fix altimetric profile if topology geometry is wrong (fixes #875)
* Fix apparence of creation button in intervention list (fixes #877)
* Fix topology geometries that were sampled like paths 3D geometry (fixes #878)
* Fix topology lines geometries join in some situations (ref #722)
* Fix topology not well displayed if start/end on intersection (fixes #874)

0.20.8 (2013-10-22)
-------------------

* Public trek export : Fix various layout regressions (ref #848)
* Public trek export : Show POI theme pictogram (fixes #858)
* Public trek export : full width for information desk frame (fixes #856)
* Public trek export : add footer with trek title and page numbers (fixes #861)
* Public trek export : add floating picture in POI detail (fixes #860)
* Public trek export : fix POI thumbnails missing (fixes #869)
* Fix point offset lost on path update (fixes #867)
* Fix reconnect point topologies with offset to closest path (fixes #868)

0.20.7 (2013-10-16)
-------------------

* Fix topology geometry 3D being draped twice (fixes #863)
* Altimetric profile : Show max distance and round values (fixes #853)
* Altimetric profile : Add settings for colors (fixes #854)
* Public trek export : POIs list in two columns (fixes #855)
* Public trek export : POIs details without column break (fixes #857)
* Public trek export : Show pictures attributions (fixes #859)
* Public trek export : Use 10pt fonts in every text blocks (fixes #848)

:notes:

    # Empty profiles cache
    rm -rf var/media/profiles/*


0.20.6 (2013-10-14)
-------------------

* Remove 3D from JS WKT serializer
* Safety check if path is less than 1m
* Remove mentions of 2154 projection in schema migrations
* Fix performance issues in altimetric JSON (fixes #845)
* Fix filter forms missing from Trek and POI lists (fixes #847)
* Fix empty Nginx log files (fixes #846)


0.20.5 (2013-10-09)
-------------------

* Fix migration of draping utility function

0.20.4 (2013-10-09)
-------------------

* Fix sort stake by id (level) (fixes #835)
* Rename stake to maintenance stake (fixes #834)
* Add validity to path filter (fixes #836)
* Do not redrape topology geometries, use path 3D geometry (fixes #832)
* Fix document export of Trail objects (fixes #839)
* Fix trail helpers for land layers (fixes #838, ref #842)
* Fix install on fresh folder, missing folder ``lib/src`` (fixes #844)


0.20.3 (2013-09-30)
-------------------

**BUG fixes**

* Fix typo in french translation of Properties (fixes #815)
* Fix missing description from infrastructure/signage detail page (fixes #816)
* Fix Cities / Districts / Restricted Areas in project detail page (fixes #817)
* Fix only deleted topology can have geom = NULL (fixes #818)
* Fix geometries not editable in QGis by switching path and topologies
  geometries to 2D (fixes #688)
* Fix altimetric sampling precision setting not taken in account in SQL (ref #776)


0.20.2 (2013-08-27)
-------------------

* Fix convert urls behind reverse proxy with prefix
* Fix Trek public print conversion
* Fix display of trek length in public document (one decimal only)
* Fix altimetric graph delaying map display in detail pages

:notes:

    # Empty maps captures cache
    rm -rf var/media/maps/trek-*


0.20.1 (2013-08-26)
-------------------

* Add DB index for start and end columns
* Merge gunicorn logs with respective applications logs
* Lower logging level in production (WARNING -> INFO)

**BUG fixes**

* Fix deployment error with application's TITLE
* Fix deployment errors with mandatory external authent values
* Fix trek export layout: fit map image and altimetric profile in one page.


0.20 (2013-08-23)
-----------------

* Edit difficulty id in Admin site, mainly used to order difficulty levels (fixes #771)
* Use explicit list of fields in forms, instead of excluding model fields (fixes #736).
  Issue #712 was closed too, since most suspected cause was field listings. Please re-open
  if problem re-appears.
* Fix timeout on POI Shapefile and CSV exports (fixes #672)
* Altimetric profiles are now computed in PostGIS (fixes #778, #779)
* Positive and negative ascents are now computed using more DEM resolution (fixes #776)

:notes:

    Setting ``PROFILE_MAXSIZE`` was replaced by ``ALTIMETRIC_PROFILE_PRECISION`` which
    controls sampling precision in meters (default: 20 meters)

* Altimetric profiles were removed from object map images
* Altimetric profiles are now plotted using SVG
* Altimetric profiles are now inserted into path documents and trek public printouts (ref #626)
* Fix deletion of associated interventions when editing infrastructures (fixes #783)
* Latest record is updated (*touch*) when a DELETE is performed on table (refreshs cache) (fixes #698)

* Reworked settings mechanism to follow Django best practices

:notes:

    Replace all computed values from ``etc/settings.ini``. For example, replace "60 * 60"
    by 3600. (You can increase this value to several hours by the way)

* Allow server host to capture pages (fixes #733)
* Adjust map capture according to geometry aspect ratio (fixes #627)
* Always show path layer in detail pages (fixes #781)
* Fix restore of topology on loop paths (fixes #760)
* Fix topology construction when loop is formed by two convergent paths (fixes #768)
* Added small tool page at ``/tools/extents/`` to visualize configured extents (ref #732)
* Removed setting ``spatial_extent_wgs84``, now computed automatically from ``spatial_extent``,
  with a padding of 10%.

:notes:

    Have a look at ``conf/settings.ini.sample`` to clean-up unnecessary values from your
    settings file.

* Fix paths offset for portrait spatial extent (fixes #732)
* Rely on Tilecache default max resolution formulae (fixes #732)
* Due to bug in Leaflet/Proj4Leaflet (https://github.com/kartena/Proj4Leaflet/issues/37)
  landscape spatial extents are not supported. Please adjust spatial_extent to be a portrait or square,
  or application will raise *ImproperlyConfiguredError*.
* Reload map objects on zoom out too (fixes #435)
* Fix computation of *min_elevation* for point topologies (fixes #808)

:notes:

    In order to recompute all paths topologies altimetry information, you can perform
    the following query: ``UPDATE e_t_evenement SET decallage = decallage;``.
    Reading information from rasters is costly. Be prepared to wait for a while.


0.19.1 (2013-07-15)
-------------------

* Restore ``pk`` property in Trek GeoJSON layer


0.19 (2013-07-12)
-----------------

* Intervention length field (readonly if geometry is line)
* Fix apparence bug if no rights to add treks and pois (fixes #713)
* Fix extremities snapping (fixes #718)
* Show information desk in trek detail page (fixes #719)
* Fix topology adjustments after path split (fixes #720)
* On edition show global line orientation instead of individual paths (fixes #679)
* Fix invalid topology if trek goes twice on same path (fixes #671)
* Overlapping is now more precise (fixes #710)
* Reworked trek print layout
* Fix topology building if paths are taken twice (fixes #722)
* Fix tiling offset with horizontal bboxes
* Fix display of POI layer by default on list (fixes #696)
* Fix translation of not validated paths (fixes #730)
* Fix error if topology is required and empty (fixes #745)
* Fix duplication of N-N relations on path split (fixes #738)
* Fix project map in detail page (fixes #734)
* Fix project listed deleted interventions (fixes #739)
* Fix project listed infrastructures through interventions (fixes #740)
* Fix saving intervention form on infrastructure
* Repair serializing of properties after upgrade of django-geojson (fixes #755)
* Added ``public_transport`` and ``advised_parking`` to trek JSON detail API (fixes #758)
* Repair land layers colors after upgrade of django-geojson
* Upgraded to django-geojson 2.0
* Upgraded to Django 1.5

:notes:

    Specify allowed host (server IP) in ``etc/settings.ini`` (*for example*):
    * ``host = 45.56.78.90``
    Empty object caches:
    * ``sudo /etc/init.d/memcached restart``
    * ``rm -rf ./var/cache/*``


0.18 (2013-06-06)
-----------------

* Add pretty trek duration in JSON
* Add information desk field in Trek (fixes #624)


0.17 (2013-05-17)
-----------------

* Show trek duration as human readable in minutes, hours and days (fixes #471, #683)
* Fix hover on paths that interfered with clic for topology creation (fixes #680)
* Run API urls on different workers (ref #672)
* Fix redirect to root url after logout (fixes #264)
* Fix redirect to next after login (fixes #381)
* Switch to Memcached instead of local memory in production
* Move secret key to settings.ini
* Relate paperclip FileType to Structure (fixes #256)
* Relate PhysicalTypes to Structure (fixes #255)
* Relate Organisms to Structure (fixes #263)
* Compute max_resolution automatically
* Fix creation and edition of interventions on infrastructures (fixes #678)
* Change default objects color to yellow
* Restored Italian translations
* Fix regex for RAISE NOTICE (fixes #673)
* Initial public version

See project history in `docs/history.rst` (French).
