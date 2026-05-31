# `down_image`

Source: `r503u.py` (method `R503.down_image`)

## Summary

** Not tested with MicroPython ** Download image from the upper computer to the image buffer

## Signature

```py
down_image(img_data)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `img_data` | `int/bytes/any` | `required` | See method description and examples. |

## Returns

- See method implementation for exact return structure.

## Details

- Download image from the upper computer to the image buffer

## Example

```py
from r503u import R503

fp = R503()
result = fp.down_image(img_data=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L302](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L302)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
