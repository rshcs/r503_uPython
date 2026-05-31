# `down_packet`

Source: `r503u.py` (method `R503.down_packet`)

## Summary

** Not tested with MicroPython ** Send a downlink data packet to the sensor module.

## Signature

```py
down_packet(img_pkt, end=False)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `img_pkt` | `bytes` | `required` | The image packet data to send. |
| `end` | `bool` | `False` | Whether this packet indicates the end of the image. |

## Returns

- None

## Details

- Send a downlink data packet to the sensor module.

## Example

```py
from r503u import R503

fp = R503()
result = fp.down_packet(img_pkt=<value>)
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L317](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L317)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
