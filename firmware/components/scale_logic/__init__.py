import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID
import logging
import os

# Logger initialisieren
_LOGGER = logging.getLogger(__name__)

# Namespace-Definition
scale_logic_ns = cg.esphome_ns.namespace('scale_logic')
ScaleLogic = scale_logic_ns.class_('ScaleLogic', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ScaleLogic),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    # DYNAMISCHE PFADERMITTLUNG
    current_dir = os.path.dirname(__file__)
    header_path = os.path.join(current_dir, "scale_logic.h")
    
    # Debug-Ausgabe im ESPHome Log (während des Kompilierens)
    _LOGGER.info("🔍 Scale Logic Debug:")
    _LOGGER.info("   Pfad: %s", current_dir)
    
    if os.path.exists(header_path):
        _LOGGER.info("   ✅ scale_logic.h wurde im Ordner gefunden!")
    else:
        _LOGGER.error("   ❌ FEHLER: scale_logic.h wurde NICHT im Ordner gefunden!")
        _LOGGER.error("   Inhalt des Ordners: %s", os.listdir(current_dir))
    
    # Dem Compiler den Pfad mitteilen
    cg.add_build_flag(f"-I{current_dir}")
