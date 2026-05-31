# `read_sys_para`

Source: `r503u.py` (method `R503.read_sys_para`)

## Summary

Status register and other basic configuration parameters

## Signature

```py
read_sys_para()
```

## Parameters

This method has no parameters.

## Returns

- (list) status_reg, sys_id_code, finger_lib_size, security_lvl, device_addr, data_packet_size, baud_rate

## Details

- Refer to source implementation for packet-level details.

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_sys_para()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L181](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L181)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
