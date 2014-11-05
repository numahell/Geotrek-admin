SELECT create_schema_if_not_exist('zonage');

SELECT set_schema('f_v_commune', 'zonage');
SELECT set_schema('f_v_secteur', 'zonage');
SELECT set_schema('f_v_zonage', 'zonage');

SELECT set_schema_ft('lien_auto_troncon_couches_sig_d()', 'zonage');
SELECT set_schema_ft('nettoyage_auto_couches_sig_d()', 'zonage');
SELECT set_schema_ft('lien_auto_couches_sig_troncon_iu()', 'zonage');
SELECT set_schema_ft('lien_auto_troncon_couches_sig_iu()', 'zonage');
