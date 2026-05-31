# `manual_enroll`

Source: `r503u.py` (method `R503.manual_enroll`)

## Summary

Manually enroll a fingerprint to the device memory. Process: Read the fingerprint image -> Generate character file from Image Buffer and store it in CharBuffers 1 to 6 -> Register a fingerprint -> Store fingerprint in the device memory * if the user set num_of_fps parameter higher than 6 then it'll be automatically set to 6.

## Signature

```py
manual_enroll(location, num_of_fps, timeout=20)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `location` | `int` | `required` | The memory location of the device to enroll (1 to 200). |
| `num_of_fps` | `int` | `required` | The number of fingerprints to enroll (1 to 6). Recommended to add at least 4 fingerprints |
| `timeout` | `int` | `20` | The timeout in seconds for each step of the enrollment process. Default is 20 seconds. |

## Returns

- 0 if enrollment was successful.
- 1 Failed.

## Details

- Process: Read the fingerprint image -> Generate character file from Image Buffer and store it in
- CharBuffers 1 to 6 -> Register a fingerprint -> Store fingerprint in the device memory
- * if the user set num_of_fps parameter higher than 6 then it'll be automatically set to 6.

## Example

```py
from r503u import R503

fp = R503()
result = fp.manual_enroll(location=<value>, num_of_fps=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L444](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L444)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
