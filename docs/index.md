# r503_uPython Documentation

Comprehensive documentation for the `R503` MicroPython driver (`r503u.py`) used with R503 fingerprint modules.

## What You Get

- API reference for every public method in `R503`.
- Parameter and return value details in a standard documentation format.
- Wiring diagram and electrical notes for MicroPython devices (for example ESP32).
- Operation flow for enrollment and fingerprint matching.
- GitHub Pages hosting guide.

## Quick Navigation

- [Function Index](functions/index.md)
- [GitHub Pages Hosting Guide](github-pages.md)
- [Project README](https://github.com/rshcs/r503_uPython/blob/main/README.md)

## Wiring Diagram

![R503 to MicroPython device wiring](wiring.svg)

## Operation Principle

### Fingerprint Enrollment

1. Capture image using `get_image_ex()`.
2. Convert image to a character file with `img2tz()`.
3. Repeat the capture/convert process for multiple samples (1 to 6).
4. Merge samples with `reg_model()` to create a template.
5. Save template into flash memory with `store()`.

### Check Whether a Fingerprint Exists in Device Memory

1. Capture image using `get_image_ex()`.
2. Convert image to character data with `img2tz()`.
3. Search the library using `search()`.
4. Match result returns:
   - `0` when a match is found.
   - `9` when no match is found.
   - Template number and match score in the returned tuple.

## Electrical and Pin Note

!!! warning
    Some ESP32 pins are not usable as general GPIO even if they appear labeled as GPIO.
    For example GPIO 6 to 11 are connected to integrated SPI flash.
    See the [ESP32 pinout reference](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/) before wiring.
