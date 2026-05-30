# r503_uPython

[![MicroPython - ESP32](https://img.shields.io/badge/MicroPython-ESP32-brightgreen)](https://micropython.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

MicroPython library for the R503 fingerprint sensor module running on ESP32.

Overview
- Compact MicroPython driver (r503u.py) implementing the R503 binary protocol over UART.
- Helper functions for enrollment, search, device info and basic device management.
- Target: ESP32 running MicroPython (defaults: UART1 TX=21, RX=17, wakeup_pin=4, baud=57600).

Features
- Simplified and manual fingerprint enrollment flows.
- Search and match fingerprints (returns matched template index and score).
- Read and decode system parameters and product information.
- Read/write fingerprint index and library management (delete, empty, read count).
- LED control for module status indications.
- Utility functions for baud/security/package-size configuration.
- Wakeup pin support (configured as input). Interrupt-driven behavior is left to the user.

Interface

Diagram (sensor left, ESP32 right):

Sensor (R503)                ESP32 (DevKit)
+----------------+           +---------------------+
| [1] VCC  3.3V  |-----------| 3.3V                |
| [2] GND        |-----------| GND                 |
| [3] TX         |---(3)---->| RX (GPIO17) UART1   |
| [4] RX         |---(4)---->| TX (GPIO21) UART1   |
| [5] Wakeup     |---(5)---->| GPIO4 (input)       |
+----------------+           +---------------------+

Wiring table
1. VCC (Sensor) -> 3.3V (ESP32 3V3)
2. GND (Sensor) -> GND (ESP32)
3. Sensor TX -> ESP32 RX (GPIO17) — sensor TX goes to ESP32 RX
4. Sensor RX -> ESP32 TX (GPIO21) — sensor RX goes to ESP32 TX
5. Sensor Wakeup -> ESP32 GPIO4 (configured as input by class)

Voltages and logic
- Power the sensor with 3.3V. Do NOT use 5V for logic lines. The library assumes 3.3V power and logic.
- ESP32 logic is 3.3V and can be connected directly.

Wakeup pin / interrupts
- The class configures a wakeup Pin (default GPIO4) and exposes `wakeup_pin_status()`.
- The repository does not include an interrupt-driven API. If you need interrupts, attach them in your application. Example on device:

```py
from machine import Pin

wu = Pin(4, Pin.IN)

def on_wakeup(pin):
    print('Wakeup event', pin.value())

wu.irq(handler=on_wakeup, trigger=Pin.IRQ_FALLING)
```

Installation
Files to upload to your MicroPython device:
- `main.py` (your application)
- `r503u.py`
- `confirmation_codes.py`

Using mpremote (CLI)
- Copy files (example for Windows COM3):

```
mpremote connect COM3 cp r503u.py :
mpremote connect COM3 cp confirmation_codes.py :
mpremote connect COM3 cp main.py :
mpremote connect COM3 run main.py
```

Alternative: Thonny IDE
- Select the MicroPython (ESP32) interpreter, connect to your board and use the Files pane to upload the files.

Usage examples (very simple)
Place these calls in REPL or `main.py`. Create the object first:

```py
from r503u import R503
fp = R503()  # defaults: baud=57600, tx_pin=21, rx_pin=17, wakeup_pin=4
```

1) fp.simplified_enroll()

```py
# Blocking helper that handles enrollment flow interactively via prints
res = fp.simplified_enroll(num_of_fps=4, buff_no=1, timeout=20)
print(res)
```
Expected outputs (examples):
- If fingerprint already exists: prints `Fingerprint found in the memory, location: 5` and returns `0`.
- If enrolling: prints prompts (`Place your finger...`, `Character file generation successful: 1`, etc.) and returns `0` on success.

2) fp.read_index_table()

```py
idx = fp.read_index_table(0)
print(idx)
```
Expected output: a Python list of stored template indices, e.g. `[0, 3, 5, 12]`. On comms error returns `99`.

3) fp.search()

```py
res = fp.search(buff_num=1, start_id=0, para=200, timeout=10)
print(res)
```
Console shows `Place your finger on the sensor. Timeout: 10 seconds` then `Searching...`.
Expected return example: `(0, 12, 78)` -> (confirmation_code, template_index, match_score). `9` as first element means "no match".

4) fp.read_valid_template_num()

```py
print(fp.read_valid_template_num())
```
Expected output: an integer like `5` indicating number of valid templates stored.

5) fp.delete_char()

```py
rc = fp.delete_char(page_num=3, num_of_temps_to_del=1)
print(rc, fp.confirmation_decode(rc))
```
Expected output: `0 00h: command execution complete` on success.

6) fp.empty_finger_lib()

```py
rc = fp.empty_finger_lib()
print(rc, fp.confirmation_decode(rc))
```
Expected output: `0 00h: command execution complete` on success.

7) fp.read_sys_para_decode()

```py
print(fp.read_sys_para_decode())
```
Expected output (example dict):

```
{
  'system_busy': False,
  'matching_finger_found': False,
  'pw_verified': False,
  'valid_image_in_buffer': False,
  'system_id_code': 257,
  'finger_library_size': 200,
  'security_level': 3,
  'device_address': '0xffffffff',
  'data_packet_size': 128,
  'baud_rate': 57600
}
```

8) fp.read_prod_info_decode()

```py
print(fp.read_prod_info_decode())
```
Expected output (example dict) or `99` on error. Example:

```
{
  'module type': 'GT-521F32',
  'batch number': 'AB12',
  'serial number': '00001234',
  'hw main version': 1,
  'hw sub version': 0,
  'sensor type': 'optical',
  'image width': 256,
  'image height': 288,
  'template size': 512,
  'fp database size': 200
}
```

9) fp.led_control()

```py
rc = fp.led_control(ctrl=3, speed=0, color=1, cycles=0)
print(rc, fp.confirmation_decode(rc))
```
Expected output: `0 00h: command execution complete` (0 = always on in this example).
