# WitMotion Sensors for Home Assistant (`witmotion-ha`)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/default)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A native Home Assistant integration for **WitMotion Bluetooth BLE** and **RS-485 Modbus** high-precision motion, tilt, and structural vibration sensors.

Supports:
- **WT901BLECL 5.0 / WT9011DCL:** 9-Axis AHRS (Roll, Pitch, Yaw, Acceleration $g$, Angular Velocity $^\circ$/s).
- **WTVB01-BT 5.0:** Structural & Industrial Vibration (Displacement in $\mu$m, Frequency in Hz, Velocity RMS in mm/s, Temperature).
- **HWT9053-485 / HWT905:** Industrial RS-485 Modbus Inclinometer (Sub-millidegree precision, Kalman filtering).

---

## Features
- **Native Bluetooth BLE Integration:** Connects directly via Home Assistant's built-in `bluetooth` stack and ESPHome Bluetooth Proxies. Zero proprietary USB dongles required.
- **Micro-Displacement Tracking:** Decodes structural micro-movement down to $1\,\mu\text{m}$.
- **Rate-Throttled Engine:** Protects Home Assistant's event bus and database from event flooding while preserving high-precision motion calculations.
- **Plug-and-Play Dashboard:** Includes complete Lovelace configuration for live readouts and 24-hour historical trend curves.

---

## Installation via HACS

1. In Home Assistant, open **HACS** $\rightarrow$ **Integrations**.
2. Click the three dots in the top-right corner $\rightarrow$ select **Custom repositories**.
3. Add repository URL: `https://github.com/maslen-io/witmotion-ha` with category **Integration**.
4. Click **Download**, then restart Home Assistant.

---

## HWT9053-485 Modbus Setup (USB / RS-485)

For industrial wired Modbus sensors like the **HWT9053-485**:
1. Copy `modbus_hwt9053.yaml` to your Home Assistant `/config/` directory.
2. Include it in your `/config/configuration.yaml`:
   ```yaml
   modbus: !include modbus_hwt9053.yaml
   ```
3. Update the `port:` path if your serial identifier differs (recommended: use `/dev/serial/by-id/...`).
4. Restart Home Assistant Core. All sensors automatically populate with signed 16-bit engineering scaling and true `unavailable` disconnect handling.

---

## License
MIT License. Created by [maslen-io](https://github.com/maslen-io).
