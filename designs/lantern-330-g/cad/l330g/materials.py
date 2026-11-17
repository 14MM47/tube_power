"""Material legend for the Lantern 330-G assembly (SPEC section 8).

Each key carries the label and sRGB colour from SPEC section 8, whether the
material is 3D printed, and a density used only for the BOM mass estimate.
Some densities are effective values for a solid drawn in place of a hollow or
mixed part: the sandwich panels (0.46 kg/m² at 10 mm), PP twin-wall,
bought electrical parts and the battery box.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Material:
    key: str
    label: str
    hex: str
    printed: bool
    density: float  # g/cm³ (effective where noted)
    short: str      # short label for part names, e.g. "PAHT-CF"

    @property
    def rgb(self) -> tuple[float, float, float]:
        h = self.hex.lstrip("#")
        return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


LEGEND: dict[str, Material] = {m.key: m for m in [
    Material("asa", "ASA, 3D printed", "#F28C28", True, 1.07, "ASA"),
    Material("paht_cf", "PAHT-CF, 3D printed", "#7A3FB0", True, 1.06, "PAHT-CF"),
    Material("tpu", "TPU 95A, 3D printed", "#19A7A0", True, 1.22, "TPU 95A"),
    Material("sandwich", "GFRP-faced XPS sandwich", "#EDE6D3", False, 0.046, "GFRP/XPS sandwich"),
    Material("cfrp", "CFRP tube", "#2B2B2B", False, 1.55, "CFRP"),
    Material("alu", "Aluminium 6082-T6 / 6063-T6", "#B9C0C8", False, 2.70, "Aluminium"),
    Material("stainless", "Stainless steel 316", "#8E99A3", False, 8.0, "Stainless 316"),
    Material("steel", "Steel S355, galvanised", "#6D7B88", False, 7.85, "Steel S355 galv."),
    Material("bearing", "Bearings (bought)", "#4E5964", False, 7.8, "Bearing steel"),
    Material("spring", "Spring steel", "#3E5A78", False, 7.85, "Spring steel"),
    Material("belt", "GT2 belt (neoprene, glass cord)", "#3A2A20", False, 1.3, "GT2 belt"),
    Material("bronze", "Bronze / brass (worm wheel)", "#B0793B", False, 8.8, "Bronze"),
    Material("bought_elec", "Motors, sensors, slip ring (bought)", "#3B3F45", False, 3.0, "Bought electrical"),
    Material("pcb", "FR-4 PCB", "#2E7D32", False, 1.85, "FR-4"),
    Material("pp", "PP twin-wall (vane)", "#F5F5F2", False, 0.35, "PP twin-wall"),
    Material("battery", "Battery box (bought)", "#556B2F", False, 2.0, "Battery box"),
]}

#: PRINT['material'] strings used by the 3dprint part modules -> legend key.
PRINT_MATERIAL_TO_KEY = {
    "asa": "asa",
    "paht-cf": "paht_cf",
    "paht_cf": "paht_cf",
    "pa12-cf": "paht_cf",
    "tpu-95a": "tpu",
    "tpu95a": "tpu",
    "tpu 95a": "tpu",
    "tpu": "tpu",
}

#: Finer labels for aluminium parts (6063-T6 tubes vs 6082-T6 plate).
ALU_6063 = "Aluminium 6063-T6"
ALU_6082 = "Aluminium 6082-T6"


def material(key: str) -> Material:
    return LEGEND[key]


def key_for_print_material(name: str) -> str:
    """Map a PRINT['material'] value (e.g. 'ASA', 'PAHT-CF', 'TPU-95A') to a legend key."""
    k = str(name).strip().lower()
    if k in PRINT_MATERIAL_TO_KEY:
        return PRINT_MATERIAL_TO_KEY[k]
    for frag, key in (("paht", "paht_cf"), ("cf", "paht_cf"), ("tpu", "tpu"), ("asa", "asa")):
        if frag in k:
            return key
    raise KeyError(f"unknown print material {name!r}")
