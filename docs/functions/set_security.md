# `set_security`

Source: `r503u.py` (method `R503.set_security`)

## Summary

Set the security level of the fingerprint sensor. This function sets the security level to one of 5 levels: 1: Low 2: Medium 3: High (default) 4: Higher 5: Highest

## Signature

```py
set_security(lvl=3)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `lvl` | `int` | `3` | The desired security level, 1-5. Default is 3. |

## Returns

- conf_code (int): The confirmation code received after setting the
- security level. 0 means success.
- It checks if the security level is valid, sends the set security
- command with the level, and returns the confirmation code response.

## Details

- This function sets the security level to one of 5 levels:
- 1: Low
- 2: Medium
- 3: High (default)
- 4: Higher
- 5: Highest

## Example

```py
from r503u import R503

fp = R503()
result = fp.set_security()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L127](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L127)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
