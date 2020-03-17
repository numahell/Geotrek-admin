-------------------------------------------------------------------------------
-- Keep dates up-to-date
-------------------------------------------------------------------------------

CREATE TRIGGER maintenance_intervention_date_insert_tgr
    BEFORE INSERT ON maintenance_intervention
    FOR EACH ROW EXECUTE PROCEDURE ft_date_insert();

CREATE TRIGGER maintenance_intervention_date_update_tgr
    BEFORE INSERT OR UPDATE ON maintenance_intervention
    FOR EACH ROW EXECUTE PROCEDURE ft_date_update();

CREATE TRIGGER maintenance_project_date_update_tgr
    BEFORE INSERT OR UPDATE ON maintenance_project
    FOR EACH ROW EXECUTE PROCEDURE ft_date_update();

-------------------------------------------------------------------------------
-- Delete related interventions when a topology is deleted
-------------------------------------------------------------------------------

CREATE FUNCTION {# geotrek.maintenance #}.delete_related_intervention() RETURNS trigger SECURITY DEFINER AS $$
BEGIN
    UPDATE maintenance_intervention SET deleted = NEW.deleted WHERE object_id = NEW.id;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER maintenance_topology_interventions_d_tgr
AFTER UPDATE OF deleted ON core_topology
FOR EACH ROW EXECUTE PROCEDURE delete_related_intervention();


-------------------------------------------------------------------------------
-- Denormalized altimetry information
-------------------------------------------------------------------------------

ALTER TABLE maintenance_intervention ALTER COLUMN "length" SET DEFAULT 0.0;
ALTER TABLE maintenance_intervention ALTER COLUMN slope SET DEFAULT 0.0;
ALTER TABLE maintenance_intervention ALTER COLUMN min_elevation SET DEFAULT 0;
ALTER TABLE maintenance_intervention ALTER COLUMN max_elevation SET DEFAULT 0;
ALTER TABLE maintenance_intervention ALTER COLUMN ascent SET DEFAULT 0;
ALTER TABLE maintenance_intervention ALTER COLUMN descent SET DEFAULT 0;

CREATE FUNCTION {# geotrek.maintenance #}.update_altimetry_topology_intervention() RETURNS trigger SECURITY DEFINER AS $$
BEGIN
    UPDATE maintenance_intervention SET
        length = CASE WHEN ST_GeometryType(NEW.geom) <> 'ST_Point' THEN NEW.length ELSE length END,
        slope = NEW.slope,
        min_elevation = NEW.min_elevation, max_elevation = NEW.max_elevation,
        ascent = NEW.ascent, descent = NEW.descent
     WHERE object_id = NEW.id;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER maintenance_topology_interventions_iu_tgr
AFTER UPDATE OF length, slope,
    min_elevation, max_elevation,
    ascent, descent ON core_topology
FOR EACH ROW EXECUTE PROCEDURE update_altimetry_topology_intervention();


CREATE FUNCTION {# geotrek.maintenance #}.update_altimetry_intervention() RETURNS trigger SECURITY DEFINER AS $$
DECLARE
    elevation elevation_infos;
BEGIN
    SELECT geom_3d, slope, min_elevation, max_elevation, ascent, descent
    FROM core_topology WHERE id = NEW.object_id INTO elevation;

    IF ST_GeometryType(elevation.draped) <> 'ST_Point' THEN
        NEW.length := ST_3DLength(elevation.draped);
    END IF;
    NEW.geom_3d := elevation.draped;
    NEW.slope := elevation.slope;
    NEW.min_elevation := elevation.min_elevation;
    NEW.max_elevation := elevation.max_elevation;
    NEW.ascent := elevation.positive_gain;
    NEW.descent := elevation.negative_gain;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER m_t_intervention_altimetry_iu_tgr
BEFORE INSERT OR UPDATE OF object_id ON maintenance_intervention
FOR EACH ROW EXECUTE PROCEDURE update_altimetry_intervention();


-------------------------------------------------------------------------------
-- Compute area
-------------------------------------------------------------------------------

CREATE FUNCTION {# geotrek.maintenance #}.update_area_intervention() RETURNS trigger SECURITY DEFINER AS $$
BEGIN
   NEW.area := NEW.width * NEW.length;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER maintenance_intervention_area_iu_tgr
BEFORE INSERT OR UPDATE OF width, height ON maintenance_intervention
FOR EACH ROW EXECUTE PROCEDURE update_area_intervention();
