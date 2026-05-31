# R503 Fingerprint Reader MicroPython Driver

[![MicroPython - ESP32](https://img.shields.io/badge/MicroPython-ESP32-brightgreen)](https://micropython.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/rshcs/r503_uPython)](https://github.com/rshcs/r503_uPython/commits/main)

Pure Python implementation: https://github.com/rshcs/Grow-R503-Finger-Print

---

MicroPython library for the R503 fingerprint sensor module running on ESP32.

![R503](docs/r503.jpg)

Image ref: aliexpress[dot]com

## Overview

- Compact MicroPython driver (`r503u.py`) implementing the R503 binary protocol over UART.
- Helper functions for enrollment, search, device info and basic device management.
- Target: ESP32 running MicroPython (defaults: UART1 TX=21, RX=17, wakeup_pin=4, baud=57600).

## Features

- Simplified and manual fingerprint enrollment flows.
- Search and match fingerprints (returns matched template index and score).
- Read and decode system parameters and product information.
- Read/write fingerprint index and library management (delete, empty, read count).
- LED control for module status indications.
- Utility functions for baud/security/package-size configuration.
- Wakeup pin support (configured as input). Interrupt-driven behavior is left to the user.

## Operation Principle

### Fingerprint Enrollment

1. Read fingerprint image from sensor and place it in the image buffer using `get_image_ex()`.
2. Generate a character file from that image and store it in one character buffer using `img2tz()`.
3. Repeat steps 1 and 2 for the user-defined sample count (1 to 6).
4. Generate a final fingerprint template using `reg_model()`.
5. Store the generated template in permanent module memory using `store()`.

### Check Whether a Fingerprint Exists in Device Memory

1. Read fingerprint image into image buffer using `get_image_ex()`.
2. Generate character file and store in character buffer using `img2tz()`.
3. Search fingerprint library for a matching template using `search()`.
4. Return values:
   - `0` when a match is found.
   - `9` when no match is found.
   - Matching template number and match score are also returned.

## Interfacing

### Wiring Diagram

![R503 to MicroPython device wiring](docs/wiring.svg)

### Wiring Connections

| No. | Sensor Side | MicroPython Device Side | Signal | Sensor side wire color    | Notes                           |
| --- | --- | --- | --- |---------------------------|---------------------------------|
| 1 | VCC | 3V3 | Power supply | Red                       | Main sensor supply              |
| 2 | GND | GND | Ground | Black                     | Common ground required          |
| 3 | TX | RX (GPIO17, UART1) | UART TX -> RX            | Yellow                    | Sensor TX connects to device RX |
| 4 | RX | TX (GPIO21, UART1) | UART RX <- TX            | Maroon  or Green or Brown | Sensor RX connects to device TX |
| 5 | Wakeup pin | GPIO4 | Wakeup signal | Blue                      | Can be used as interrupt source |
| 6 | Touch induction power | 3V3 | Auxiliary power | White                     | Tie to 3.3V                     |

> [!WARNING]
> **Note:** Some pins on the ESP32 are not usable even though they are labeled as GPIO pins. For example, GPIO 6 to 11 are not usable for general-purpose I/O because they are connected to integrated SPI flash. See [ESP32 pinout](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) for details.

## Voltages and Logic

- Power the sensor with 3.3V.
- Do NOT use 5V for logic lines.
- ESP32 logic is 3.3V and can be connected directly.

## Installation

Files to upload to your MicroPython device:

- `main.py` (your application)
- `r503u.py`
- `confirmation_codes.py`

### Using mpremote (CLI)

```bash
mpremote cp r503u.py :r503u.py
mpremote cp confirmation_codes.py :confirmation_codes.py
mpremote cp main.py :main.py
mpremote run main.py
```

### Alternative: Thonny IDE

- Select the MicroPython (ESP32) interpreter.
- Connect your board.
- Use the Files pane to upload `main.py`, `r503u.py` and `confirmation_codes.py`.

## Usage Examples

These are simple examples for REPL or `main.py`.

### Setup

```py
from r503u import R503
fp = R503()  # defaults: baud=57600, tx_pin=21, rx_pin=17, wakeup_pin=4
```

---

### 1) `fp.simplified_enroll()`

**Purpose:**
Enroll a fingerprint with a guided, blocking flow. It checks whether the fingerprint already exists and otherwise enrolls into the next free location.

```py
from r503u import R503

fp = R503()
res = fp.simplified_enroll()  # Defaults: num_of_fps=4, buff_no=1, timeout=20
print(res)
```

**Expected output (example):**
- Existing fingerprint: prints `Fingerprint found in the memory, location: 5`, returns `0`.
- New enrollment: prints prompts (`Place your finger...`, `Character file generation successful...`) and returns `0` on success.

---

### 2) `fp.read_index_table()`

**Purpose:**
Read the template index bitmap and return all occupied memory indices on a given index page.

```py
from r503u import R503

fp = R503()
idx = fp.read_index_table()
print(idx)
```

**Expected output (example):**
- `[0, 3, 5, 12]` (stored template positions)
- Returns `99` on communication timeout/error.

---

### 3) `fp.search()`

**Purpose:**
Capture a fingerprint, generate a template in buffer, and search the configured library range.

```py
from r503u import R503

fp = R503()
res = fp.search(buff_num=1, start_id=0, para=200, timeout=10)
print(res)
```

**Expected output (example):**
- Console: `Place your finger on the sensor...`, then `Searching...`
- Return: `(0, 12, 78)` = `(confirmation_code, template_index, match_score)`
- No match example: `(9, 0, 0)` where `9` means no matching finger found.

---

### 4) `fp.read_valid_template_num()`

**Purpose:**
Get total number of currently valid fingerprint templates in sensor memory.

```py
from r503u import R503

fp = R503()
print(fp.read_valid_template_num())
```

**Expected output (example):**
- `5`

---

### 5) `fp.delete_char()`

**Purpose:**
Delete one or more templates starting at a given page index.

```py
from r503u import R503

fp = R503()
rc = fp.delete_char(page_num=3, num_of_temps_to_del=1)
print(rc, fp.confirmation_decode(rc))
```

**Expected output (example):**
- `0 00h: command execution complete`

---

### 6) `fp.empty_finger_lib()`

**Purpose:**
Erase all stored fingerprint templates from the module.

```py
from r503u import R503

fp = R503()
rc = fp.empty_finger_lib()
print(rc, fp.confirmation_decode(rc))
```

**Expected output (example):**
- `0 00h: command execution complete`

---

### 7) `fp.read_sys_para_decode()`

**Purpose:**
Read and decode module system parameters into a human-readable dictionary.

```py
from r503u import R503

fp = R503()
print(fp.read_sys_para_decode())
```

**Expected output (example):**

```py
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

---

### 8) `fp.read_prod_info_decode()`

**Purpose:**
Read and decode manufacturer/module product information.

```py
from r503u import R503

fp = R503()
print(fp.read_prod_info_decode())
```

**Expected output (example):**

```py
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

Returns `99` on communication/read failure.

---

### 9) `fp.led_control()`

**Purpose:**
Control the onboard LED mode (always on/off, breathing, flashing, etc.).

```py
from r503u import R503

fp = R503()
rc = fp.led_control(ctrl=3, speed=0, color=1, cycles=0)
print(rc, fp.confirmation_decode(rc))
```

**Method details:**

- Signature: `fp.led_control(ctrl=0x03, speed=0, color=0x01, cycles=0)`
- `ctrl` modes:
  - `1`: breathing light
  - `2`: flashing light
  - `3`: always on
  - `4`: always off
  - `5`: gradually on
  - `6`: gradually off
- `speed`: `0` to `255` (effect speed)
- `color`: `0` to `7` (module LED color code)
- `cycles`: `0` to `255` (effect repetition count, mode-dependent)
- Return value: confirmation code (`0` means command execution complete)

---

### 10) `fp.soft_reset()`

**Purpose:**
Perform a software reset of the R503 module.

```py
from r503u import R503

fp = R503()
rc = fp.soft_reset()
print(rc, fp.confirmation_decode(rc))
```

**Expected output (example):**
- `0 00h: command execution complete`
- After reset, you may need to wait briefly before sending the next command.

---

## Wakeup Pin / Interrupts

- The class configures a wakeup pin (default GPIO4) and exposes `wakeup_pin_status()`.
- The repository does not include an interrupt-driven API. If needed, attach interrupts in your application.

```py
from machine import Pin

wu = Pin(4, Pin.IN)

def on_wakeup(pin):
    print('Wakeup event', pin.value())

wu.irq(handler=on_wakeup, trigger=Pin.IRQ_FALLING)
```
