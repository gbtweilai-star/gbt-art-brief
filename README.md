# art_brief

**One capability bit from GBT V8, packaged standalone.** No. 11 of 341,
`creation` domain (Creation).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> **作品策划位**（人话一次问，四路知识同时到位 + 给出可直接照抄的出片命令）。四路： `ui_kit` **可渲件**（纯 HTML/CSS，能直接进渲染器）· `bits_kit` **参考件**（react-bits 的 React 实现，**只读来学**——许可禁止再分发/移植）· `motion_kit` **动效API**（anime.js 真 API，带签名与 `文件#L行号`）· `design_atlas` **技法节**（18 份手册里该读哪一节，带 `文件#L行号`）；出片交给 `art_chain`。常用说法：出作品 / 做个动效 / 一键出图 / 帮我策划一下 / 这个效果怎么做。op=status/where/plan/run：`plan` 走**四路零作用域的读**（命中 0 就是 0，**不拿别的路凑数**，缺哪一路就如实列出来）并给出 `art_chain` 的下一步命令；`run` 真出片，失败**停在原地**并原样带出`inner_*`（内层门缺什么）。铁律：每路都走既有门 `run_task`（不直连模块、不绕门、不重写任何一环）· 缺就如实报缺 · `bits_kit` 那一路只读来学、**不搬成品**。

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-art-brief.git
cd gbt-art-brief
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_art_brief info                  # capability card
python -m gbt_art_brief spec --json           # machine-readable contract
python -m gbt_art_brief check --payload '{}'
python -m gbt_art_brief run   --payload '{}'
```

Real `info` output from this machine:

```text
art_brief  (creation)  v1.0.0
----------------------------------------
**作品策划位**（人话一次问，四路知识同时到位 + 给出可直接照抄的出片命令）。四路： `ui_kit` **可渲件**（纯 HTML/CSS，能直接进渲染器）· `bits_kit` **参考件**（react-bits 的 React 实现，**只读来学**——许可禁止再分发/移植）· `motion_kit` **动效API**（anime.js 真 API，带签名与 `文件#L行号`）· `design_atlas` **技法节**（18 份手册里该读哪一节，带 `文件#L行号`）；出片交给 `art_chain`。常用说法：出作品 / 做个动效 / 一键出图 / 帮我策划一下 / 这个效果怎么做。op=status/where/plan/run：`plan` 走**四路零作用域的读**（命中 0 就是 0，**不拿别的路凑数**，缺哪一路就如实列出来）并给出 `art_chain` 的下一步命令；`run` 真出片，失败**停在原地**并原样带出`inner_*`（内层门缺什么）。铁律：每路都走既有门 `run_task`（不直连模块、不绕门、不重写任何一环）· 缺就如实报缺 · `bits_kit` 那一路只读来学、**不搬成品**。

gated      : True   <- needs explicit consent
external   : False
multi-op   : True
params     : (none)
values     : status, where, plan, run
```

Wire a real implementation:

```python
from gbt_art_brief import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（4 个）**：`status`、`where`、`plan`、`run`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Gated: this bit is marked `safe: false` in the registry — it can change state that no inverse action restores.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.11s
```

## Provenance

| field | value |
|---|---|
| capability | `art_brief` |
| domain | `creation` |
| handler | `art_brief` |
| safe | `False` (gated = `True`) |
| external | `False` |
| atlas page | [creation/art_brief](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/creation/art_brief.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
