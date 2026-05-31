import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "r503u.py"
OUT_DIR = ROOT / "docs" / "functions"


def ast_signature(fn: ast.FunctionDef) -> tuple[str, list[dict]]:
    args = [a.arg for a in fn.args.args][1:]  # skip self
    defaults = fn.args.defaults
    default_pad = [None] * (len(args) - len(defaults)) + list(defaults)

    sig_parts = []
    params = []
    for name, default in zip(args, default_pad):
        if default is None:
            sig_parts.append(name)
            default_txt = "required"
        else:
            default_txt = ast.unparse(default)
            sig_parts.append(f"{name}={default_txt}")

        params.append(
            {
                "name": name,
                "default": default_txt,
            }
        )

    return f"{fn.name}({', '.join(sig_parts)})", params


def parse_doc_sections(doc: str) -> tuple[list[str], dict, list[str]]:
    lines = doc.splitlines()
    summary = []
    params = {}
    returns = []
    mode = "summary"

    re_param_typed = re.compile(r"^\s*([a-zA-Z0-9_]+)\s*\(([^\)]+)\)\s*:\s*(.+)$")
    re_param_plain = re.compile(r"^\s*([a-zA-Z0-9_]+)\s*:\s*(.+)$")

    for raw in lines:
        line = raw.rstrip()
        low = line.strip().lower()

        inline_split = re.split(r"\b(parameters|args|arguments|returns|return)\s*:\s*", line, flags=re.IGNORECASE)
        if len(inline_split) > 1 and mode == "summary":
            before = inline_split[0].strip()
            if before:
                summary.append(before)
            key = inline_split[1].lower()
            rest = inline_split[2].strip() if len(inline_split) > 2 else ""
            mode = "params" if key in {"parameters", "args", "arguments"} else "returns"
            if rest:
                if mode == "returns":
                    returns.append(rest)
                else:
                    m = re_param_typed.match(rest)
                    if m:
                        name, ptype, pdesc = m.groups()
                        params[name] = {"type": ptype, "desc": pdesc}
                    else:
                        m = re_param_plain.match(rest)
                        if m:
                            name, pdesc = m.groups()
                            if name != "self":
                                params[name] = {"type": "int/any", "desc": pdesc}
            continue

        if low in {"parameters:", "args:", "arguments:"}:
            mode = "params"
            continue
        if low in {"returns:", "return:"}:
            mode = "returns"
            continue

        if mode == "summary":
            if line.strip():
                summary.append(line.strip())
        elif mode == "params":
            if not line.strip():
                continue
            m = re_param_typed.match(line)
            if m:
                name, ptype, pdesc = m.groups()
                params[name] = {"type": ptype, "desc": pdesc}
                continue
            m = re_param_plain.match(line)
            if m:
                name, pdesc = m.groups()
                if name != "self":
                    params[name] = {"type": "int/any", "desc": pdesc}
                continue
        elif mode == "returns":
            if line.strip():
                returns.append(line.strip())

    return summary, params, returns


OVERRIDES = {
    "led_control": {
        "extra": [
            "`ctrl` mode values: `1` breathing, `2` flashing, `3` always on, `4` always off, `5` gradually on, `6` gradually off.",
            "`speed` range: `0..255`.",
            "`color` range: `0..7` (module-defined color code).",
            "`cycles` range: `0..255`.",
        ],
        "returns": ["Confirmation code integer from the module (`0` means success)."],
    },
    "soft_reset": {
        "extra": ["Performs software reset command (`0x3D`) and returns confirmation code."],
        "returns": ["Confirmation code integer (`0` means success)."],
    },
    "search": {
        "returns": [
            "Tuple `(status, template_number, match_score)`.",
            "`status=0` means match success, `status=9` means no matching fingerprint, `99` means timeout/no response.",
        ],
    },
    "read_index_table": {
        "returns": [
            "List of template indices stored in selected index page.",
            "Returns `99` when communication fails.",
        ]
    },
    "simplified_enroll": {
        "returns": [
            "`0` on success (already exists or enrolled).",
            "Otherwise confirmation/error code (for example `9` no match before enrollment path, `99` timeout/error).",
        ]
    },
    "read_sys_para_decode": {
        "returns": [
            "Dictionary of decoded module parameters (busy flags, library size, security level, address, packet size, baud).",
            "Returns `99` on communication failure.",
        ]
    },
    "read_prod_info_decode": {
        "returns": [
            "Dictionary with module type, serial information, sensor type, image size, template size, and database size.",
            "Returns `99` on communication failure.",
        ]
    },
}


def parameter_type(default_text: str, doc_type: str | None) -> str:
    if doc_type:
        return doc_type
    if default_text == "required":
        return "int/bytes/any"
    if default_text in {"True", "False"}:
        return "bool"
    if default_text.startswith("'") or default_text.startswith('"'):
        return "str"
    if default_text.startswith("b'") or default_text.startswith('b"'):
        return "bytes"
    if default_text.startswith("[") or default_text.startswith("("):
        return "list/tuple"
    if default_text.isdigit() or (default_text.startswith("-") and default_text[1:].isdigit()):
        return "int"
    return "int/any"


def write_function_page(fn: ast.FunctionDef) -> tuple[str, str, int, str]:
    sig, params_sig = ast_signature(fn)
    doc = ast.get_docstring(fn) or "No explicit docstring in source."
    summary_lines, doc_params, doc_returns = parse_doc_sections(doc)

    summary = " ".join(summary_lines).strip()
    summary = re.split(r"\b(parameters|args|arguments|returns|return)\s*:", summary, flags=re.IGNORECASE)[0].strip()
    if not summary:
        summary = "See source for behavior details."

    rows = []
    for p in params_sig:
        name = p["name"]
        dflt = p["default"]
        dmeta = doc_params.get(name, {})
        ptype = parameter_type(dflt, dmeta.get("type"))
        pdesc = dmeta.get("desc", "See method description and examples.")
        rows.append((name, ptype, dflt, pdesc))

    ret_lines = OVERRIDES.get(fn.name, {}).get("returns", []) or doc_returns
    if not ret_lines:
        ret_lines = ["See method implementation for exact return structure."]

    extra_lines = OVERRIDES.get(fn.name, {}).get("extra", [])

    title = fn.name
    out = [f"# `{title}`", "", f"Source: `r503u.py` (method `R503.{title}`)", ""]
    out += ["## Summary", "", summary, ""]
    out += ["## Signature", "", f"```py\n{sig}\n```", ""]

    out += ["## Parameters", ""]
    if rows:
        out += ["| Name | Type | Default | Description |", "| --- | --- | --- | --- |"]
        for r in rows:
            out += [f"| `{r[0]}` | `{r[1]}` | `{r[2]}` | {r[3]} |"]
    else:
        out += ["This method has no parameters."]
    out += [""]

    out += ["## Returns", ""]
    for line in ret_lines:
        out += [f"- {line}"]
    out += [""]

    out += ["## Details", ""]
    for line in summary_lines[1:]:
        out += [f"- {line}"]
    if extra_lines:
        for line in extra_lines:
            out += [f"- {line}"]
    if len(summary_lines) <= 1 and not extra_lines:
        out += ["- Refer to source implementation for packet-level details."]
    out += [""]

    out += ["## Example", "", "```py", "from r503u import R503", "", "fp = R503()"]
    call_args = []
    for p in params_sig:
        if p["default"] == "required":
            call_args.append(f"{p['name']}=<value>")
    if not call_args:
        out += [f"result = fp.{title}()"]
    else:
        out += [f"result = fp.{title}({', '.join(call_args)})"]
    out += ["print(result)", "```", ""]

    source_url = f"https://github.com/rshcs/r503_uPython/blob/main/r503u.py#L{fn.lineno}"
    ds1 = "https://github.com/rshcs/r503_uPython/blob/main/documents/R503_datasheet%20-%20v1.1.pdf"
    ds2 = "https://github.com/rshcs/r503_uPython/blob/main/documents/R503-Sensor-Dactilar-TTL-user-manual-V1.2.1-1.pdf"
    out += [
        "## References",
        "",
        f"- Source code: [{source_url}]({source_url})",
        f"- Datasheet: [{ds1}]({ds1})",
        f"- Datasheet: [{ds2}]({ds2})",
        "",
    ]

    page = "\n".join(out)
    path = OUT_DIR / f"{title}.md"
    path.write_text(page, encoding="utf-8")
    return title, str(path.relative_to(ROOT)), fn.lineno, summary


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    module = ast.parse(SRC.read_text(encoding="utf-8"))
    class_node = None
    for node in module.body:
        if isinstance(node, ast.ClassDef) and node.name == "R503":
            class_node = node
            break

    if class_node is None:
        raise RuntimeError("R503 class not found in r503u.py")

    generated = []
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            generated.append(write_function_page(node))

    generated.sort(key=lambda x: x[0].lower())

    index_lines = [
        "# Function Index",
        "",
        "Select a method to open comprehensive documentation.",
        "",
        "| Method | Description | Source line |",
        "| --- | --- | --- |",
    ]

    for name, rel_path, lineno, summary in generated:
        desc = summary.split(".")[0].strip()
        if desc:
            desc += "."
        else:
            desc = "Method documentation."
        desc = desc.replace("|", "\\|")
        index_lines.append(f"| [`{name}`]({name}.md) | {desc} | `r503u.py:{lineno}` |")

    (OUT_DIR / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"Generated {len(generated)} function pages and index.")


if __name__ == "__main__":
    main()
