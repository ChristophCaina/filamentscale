#ifndef SCALE_LOGIC_H
#define SCALE_LOGIC_H

#include "esphome.h"

namespace esphome {
namespace scale_logic {

enum AppState {
    STATE_MAIN = 0,
    STATE_MENU_MAIN = 1,
    STATE_SUB_NEW_SPOOL = 2,
    STATE_INFO = 3,
    STATE_WINDER = 4
};

static AppState _appState = STATE_MAIN;

inline bool isMenuState(int s) {
    return s >= 1; 
}

class ScaleLogic : public Component {
 public:
  void setup() override {
    ESP_LOGI("scale_logic", "Logik initialisiert");
  }
};

} // namespace scale_logic
} // namespace esphome

#endif
