# `read_prod_info_decode`

Source: `r503u.py` (method `R503.read_prod_info_decode`)

## Summary

Decode raw product info into a human-readable dictionary. This calls read_prod_info() to get the raw info bytes. If it returns 99 (error), this returns 99. Otherwise, it decodes the raw bytes into a dictionary: - module_type: ASCII string - batch_number: ASCII string - serial_number: ASCII string - hw_main_version: Integer - hw_sub_version: Integer - sensor_type: ASCII string - image_width: Integer - image_height: Integer - template_size: Integer - fp_database_size: Integer

## Signature

```py
read_prod_info_decode()
```

## Parameters

This method has no parameters.

## Returns

- Dictionary with module type, serial information, sensor type, image size, template size, and database size.
- Returns `99` on communication failure.

## Details

- This calls read_prod_info() to get the raw info bytes.
- If it returns 99 (error), this returns 99.
- Otherwise, it decodes the raw bytes into a dictionary:
- - module_type: ASCII string
- - batch_number: ASCII string
- - serial_number: ASCII string
- - hw_main_version: Integer
- - hw_sub_version: Integer
- - sensor_type: ASCII string
- - image_width: Integer
- - image_height: Integer
- - template_size: Integer
- - fp_database_size: Integer

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_prod_info_decode()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L669](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L669)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
