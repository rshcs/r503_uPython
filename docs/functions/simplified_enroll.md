# `simplified_enroll`

Source: `r503u.py` (method `R503.simplified_enroll`)

## Summary

Simplified enrollment of fingerprints. 1. Checks if fingerprint already exists in the device memory. 2. If exists returns 0 3. If not exists then it finds the next available location in the device memory. 4. Enrolls the fingerprint at the memory location where identified by the previous step.

## Signature

```py
simplified_enroll(num_of_fps=4, buff_no=1, timeout=20)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `num_of_fps` | `int` | `4` | The number of times the  finger has to be placed on the sensor. |
| `buff_no` | `int` | `1` | The buffer number where fingerprint stored |
| `timeout` | `int` | `20` | The timeout in seconds for each step of the enrollment process. |

## Returns

- `0` on success (already exists or enrolled).
- Otherwise confirmation/error code (for example `9` no match before enrollment path, `99` timeout/error).

## Details

- 1. Checks if fingerprint already exists in the device memory.
- 2. If exists returns 0
- 3. If not exists then it finds the next available location in the device memory.
- 4. Enrolls the fingerprint at the memory location where identified by the previous step.

## Example

```py
from r503u import R503

fp = R503()
result = fp.simplified_enroll()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L496](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L496)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
