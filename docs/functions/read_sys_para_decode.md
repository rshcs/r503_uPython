# `read_sys_para_decode`

Source: `r503u.py` (method `R503.read_sys_para_decode`)

## Summary

Get system parameters in a decoded, human-readable format. Otherwise, it returns a dictionary with the parameters decoded: - system_busy: boolean - matching_finger_found: boolean - pw_verified: boolean - valid_image_in_buffer: boolean - system_id_code: int - finger_library_size: int - security_level: int - device_address: int - data_packet_size: int - baud_rate: int

## Signature

```py
read_sys_para_decode()
```

## Parameters

This method has no parameters.

## Returns

- Dictionary of decoded module parameters (busy flags, library size, security level, address, packet size, baud).
- Returns `99` on communication failure.

## Details

- Otherwise, it returns a dictionary with the parameters decoded:
- - system_busy: boolean
- - matching_finger_found: boolean
- - pw_verified: boolean
- - valid_image_in_buffer: boolean
- - system_id_code: int
- - finger_library_size: int
- - security_level: int
- - device_address: int
- - data_packet_size: int
- - baud_rate: int

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_sys_para_decode()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L189](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L189)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
