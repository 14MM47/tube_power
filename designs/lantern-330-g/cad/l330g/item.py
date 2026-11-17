"""The Item: one named, coloured part (or a set of identical fasteners) in the assembly."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any

from .materials import LEGEND


@dataclass
class Item:
    """One part of the assembly.

    ``shape`` is a build123d shape in frame-A coordinates at theta = 0, beta = 0
    (SPEC section 1) until ``assembly.build`` poses it. ``frame`` says which
    frame it moves with: 'A' (head), 'S' (swinging) or 'P' (pitching).
    """

    id: str
    name: str
    shape: Any
    material_key: str
    frame: str
    printed: bool = False
    bought: bool = False
    group: str = ""
    tag: str = ""                 # instance tag shown in labels, e.g. "-X"
    placeholder: bool = False     # stand-in envelope for a missing part
    carriage: bool = False        # moves along the lever with the spring carriage
    pose_dependent: bool = False  # rebuilt per pose (belt, springs, rollers)
    count: int = 1                # identical parts drawn in this one item
    bom: bool = True              # False: counted under another item (bearing inner rings)
    material_label: str | None = None
    module: str = ""              # printed-part module name
    note: str = ""
    tol: float = 0.1              # tessellation tolerance (mm)
    extra: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.frame not in ("A", "S", "P"):
            raise ValueError(f"{self.id} {self.name}: frame must be A, S or P, not {self.frame!r}")
        if self.material_key not in LEGEND:
            raise ValueError(f"{self.id} {self.name}: unknown material {self.material_key!r}")

    @property
    def material(self):
        return LEGEND[self.material_key]

    @property
    def mat_label(self) -> str:
        if self.material_label:
            return self.material_label
        m = self.material
        return m.short if m.printed else m.label

    @property
    def label(self) -> str:
        """Node label, e.g. 'P03 belt_arc [PAHT-CF, printed]' or 'M10 Cheek -X [Aluminium 6082-T6]'."""
        tags = [self.mat_label]
        if self.printed:
            tags.append("printed")
        if self.bought:
            tags.append("bought")
        if self.placeholder:
            tags.append("PLACEHOLDER")
        name = f"{self.name} {self.tag}".strip()
        return f"{self.id} {name} [{', '.join(tags)}]"

    @property
    def key(self) -> str:
        """Unique key within one assembly: id, name and tag."""
        return f"{self.id}|{self.name}|{self.tag}"

    def copy(self, **kw) -> "Item":
        return replace(self, **kw)
