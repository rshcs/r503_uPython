# `up_image`

Source: `r503u.py` (method `R503.up_image`)

## Summary

** Not tested with MicroPython ** Upload the image in Img_Buffer to upper computer every image contains the data around 20kilo bytes parameter: (int) timeout: timeout could vary if you change the baud rate, for 57600baud 5seconds is sufficient If you use a lower baud rate timeout may have to be increased.

## Signature

```py
up_image(timeout=5, raw=False)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `timeout` | `int` | `5` | See method description and examples. |
| `raw` | `bool` | `False` | See method description and examples. |

## Returns

- (bytesarray) if raw == True
- else (list of lists)
- In raw mode returns the data with all headers (address byte, status bytes etc.)
- raw == False mode only returns the image data [all other header bytes are filtered out]

## Details

- Upload the image in Img_Buffer to upper computer
- every image contains the data around 20kilo bytes
- parameter: (int) timeout: timeout could vary if you change the baud rate, for 57600baud 5seconds is sufficient
- If you use a lower baud rate timeout may have to be increased.

## Example

```py
from r503u import R503

fp = R503()
result = fp.up_image()
print(result)
```

## References

- Source code: [https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L277](https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L277)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf)
- Datasheet: [https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf](https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf)
