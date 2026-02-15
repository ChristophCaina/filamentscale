# ⚖️ ESPHome Filament Spool Scale & Winder

This project is an intelligent filament scale based on an ESP32. It offers precise weight measurement for 3D printing spools, an integrated spool database, and control for an optional winder add-on.

## ✨ Features
* **Precise Measurement:** Integration of an HX711 load cell for real-time weight monitoring.
* **Smart UI:** Menu-driven ST7920 display with pagination.
* **Winder Mode:** Automatic detection of a stepper add-on for filament winding or unloading.
* **Potentiometer Control:** Stepless speed control of the stepper motor via analog potentiometer.
* **Modular Design:** Thanks to ESPHome "Packages," the logic is strictly separated from the hardware configuration.

---

## 🛠 Hardware & Pinout

Configuration is handled via `substitutions` in the local YAML file. The following pins are assigned by default:

| Component | Pin | Description |
| :--- | :--- | :--- |
| **Status LED** | GPIO02 | System status indicator |
| **Display (SPI)** | GPIO18 (CLK), GPIO23 (MOSI), GPIO17 (CS) | ST7920 128x64 LCD |
| **Rotary Encoder** | GPIO32 (A), GPIO33 (B), GPIO19 (BTN) | Navigation & Selection |
| **Buzzer** | GPIO16 | Acoustic feedback |
| **HX711 (Scale)** | GPIO21 (DT), GPIO22 (SCK) | Load cell interface |
| **I2C Interface** | GPIO13 (SDA), GPIO14 (SCL) | Extensions |
| **Stepper Motor** | GPIO25 (STEP), GPIO26 (DIR) | Winder drive |
| **Filament Sensor** | GPIO27 | Runout detection |
| **Speed** | GPIO34 (Analog) | Potentiometer (0 - 3.3V) |
| **Add-on Detection**| GPIO05 (Inp. Pullup) | Detects plugged-in winder module |

---

## 🚀 Installation & Setup

To use this project on your hardware, follow these steps:

1. Create a **new device** in your ESPHome dashboard.
2. Copy the content of the [example_config.yaml](example_config.yaml) file from this repository.
3. Replace the content of your local configuration in the ESPHome dashboard with the copied text.
4. **Customization:** * Enter your WiFi credentials (`ssid` & `password`).
    * API and OTA keys are usually generated automatically by ESPHome when creating the device – ensure these are kept or regenerated.
    * Check the `substitutions` section to ensure the pinout matches your hardware.
5. **Compile & Install:** Click "Install" (USB or OTA).
6. **First Start:** After booting, zero the scale once via the menu item `1. Tare`.

### Spoolman configuration
To configure Spoolman, change the substitution in the example_config with your Spoolman IP:
`spoolman_ip: "192.168.0.1:7912"`
