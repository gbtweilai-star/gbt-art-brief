"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "art_brief",
 "domain": "creation",
 "desc": "**作品策划位**（人话一次问，四路知识同时到位 + 给出可直接照抄的出片命令）。四路： `ui_kit` **可渲件**（纯 HTML/CSS，能直接进渲染器）· `bits_kit` **参考件**（react-bits 的 React 实现，**只读来学**——许可禁止再分发/移植）· `motion_kit` **动效API**（anime.js 真 API，带签名与 `文件#L行号`）· `design_atlas` **技法节**（18 份手册里该读哪一节，带 `文件#L行号`）；出片交给 `art_chain`。常用说法：出作品 / 做个动效 / 一键出图 / 帮我策划一下 / 这个效果怎么做。op=status/where/plan/run：`plan` 走**四路零作用域的读**（命中 0 就是 0，**不拿别的路凑数**，缺哪一路就如实列出来）并给出 `art_chain` 的下一步命令；`run` 真出片，失败**停在原地**并原样带出`inner_*`（内层门缺什么）。铁律：每路都走既有门 `run_task`（不直连模块、不绕门、不重写任何一环）· 缺就如实报缺 · `bits_kit` 那一路只读来学、**不搬成品**。",
 "handler": "art_brief",
 "safe": false,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "status",
  "where",
  "plan",
  "run"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
