# `read_prod_info`

Source: `r503u.py` (method `R503.read_prod_info`)

## Summary

Read product information from the fingerprint sensor. It sends the command, checks the confirmation code, and if successful, slices the info byte string into 9 parts: - Manufacturer name: - Model number: - Serial number: - Hardware version: - Sensor type: - Sensor image width: - Sensor image height: - Template size: - Fingerprint database size:

## Signature

```py
read_prod_info()
```

## Parameters

This method has no parameters.

## Returns

- Tuple of 9 info strings if successful, else 99

## Details

- It sends the command, checks the confirmation code, and if
- successful, slices the info byte string into 9 parts:
- - Manufacturer name:
- - Model number:
- - Serial number:
- - Hardware version:
- - Sensor type:
- - Sensor image width:
- - Sensor image height:
- - Template size:
- - Fingerprint database size:

## Example

```py
from r503u import R503

fp = R503()
result = fp.read_prod_info()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L640](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L640)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
