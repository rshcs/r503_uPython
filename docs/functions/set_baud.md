# `set_baud`

Source: `r503u.py` (method `R503.set_baud`)

## Summary

Set the baud rate for serial communication. This function sets the baud rate for serial communication to one of the allowed values: 9600, 19200, 38400, 57600 (default), 115200.

## Signature

```py
set_baud(baud=57600)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `baud` | `int` | `57600` | The desired baud rate. Default is 57600. |

## Returns

- conf_code (int): The confirmation code received after setting
- the baud rate. 0 means success.
- It calculates the baud rate divisor, checks if it is valid, sends the
- set baud rate command, updates the self.ser.baudrate if successful,
- and returns the confirmation code.

## Details

- This function sets the baud rate for serial communication to one of
- the allowed values: 9600, 19200, 38400, 57600 (default), 115200.

## Example

```py
from r503u import R503

fp = R503()
result = fp.set_baud()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L99](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L99)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
