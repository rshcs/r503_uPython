# `led_control`

Source: `r503u.py` (method `R503.led_control`)

## Summary

ctrl: (int) 1 to 6 1: breathing light, 2: flashing light, 3: always on, 4: always off, 5: gradually on, 6: gradually off speed: (int) 0 to 255 color: (int) 0 to 7 cycles: (int) 0 to 255

## Signature

```py
led_control(ctrl=3, speed=0, color=1, cycles=0)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `ctrl` | `int` | `3` | See method description and examples. |
| `speed` | `int` | `0` | See method description and examples. |
| `color` | `int` | `1` | See method description and examples. |
| `cycles` | `int` | `0` | See method description and examples. |

## Returns

- Confirmation code integer from the module (`0` means success).

## Details

- 1: breathing light, 2: flashing light, 3: always on, 4: always off, 5: gradually on, 6: gradually off
- speed: (int) 0 to 255
- color: (int) 0 to 7
- cycles: (int) 0 to 255
- `ctrl` mode values: `1` breathing, `2` flashing, `3` always on, `4` always off, `5` gradually on, `6` gradually off.
- `speed` range: `0..255`.
- `color` range: `0..7` (module-defined color code).
- `cycles` range: `0..255`.

## Example

```py
from r503u import R503

fp = R503()
result = fp.led_control()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L87](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L87)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
