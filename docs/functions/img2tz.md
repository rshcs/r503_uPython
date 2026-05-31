# `img2tz`

Source: `r503u.py` (method `R503.img2tz`)

## Summary

Generate character file from the original image in Image Buffer and store the file in CharBuffer 1 to 6 parameter: (int) buffer_id, 1 to 6

## Signature

```py
img2tz(buffer_id)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `buffer_id` | `int/bytes/any` | `required` | See method description and examples. |

## Returns

- (int) confirmation code

## Details

- parameter: (int) buffer_id, 1 to 6

## Example

```py
from r503u import R503

fp = R503()
result = fp.img2tz(buffer_id=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L411](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L411)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
