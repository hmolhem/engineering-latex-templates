"""Starter analytical verification for the portfolio report template."""

from __future__ import annotations

from dataclasses import dataclass
from math import pi

C0_M_PER_S = 299_792_458.0


@dataclass(frozen=True)
class DesignCase:
    frequency_hz: float
    spacing_fraction: float
    steering_angle_deg: float

    def validate(self) -> None:
        if self.frequency_hz <= 0:
            raise ValueError("frequency_hz must be positive")
        if not 0 < self.spacing_fraction <= 1:
            raise ValueError("spacing_fraction must be in (0, 1]")
        if not -90 <= self.steering_angle_deg <= 90:
            raise ValueError("steering_angle_deg must be within [-90, 90]")


def calculate(case: DesignCase) -> dict[str, float]:
    case.validate()
    wavelength_m = C0_M_PER_S / case.frequency_hz
    spacing_m = case.spacing_fraction * wavelength_m
    steering_angle_rad = case.steering_angle_deg * pi / 180.0
    phase_rad = -2.0 * pi * spacing_m / wavelength_m * __import__("math").sin(
        steering_angle_rad
    )
    return {
        "wavelength_m": wavelength_m,
        "spacing_m": spacing_m,
        "phase_rad": phase_rad,
        "phase_deg": phase_rad * 180.0 / pi,
    }


def main() -> None:
    case = DesignCase(
        frequency_hz=2.50e9,
        spacing_fraction=0.50,
        steering_angle_deg=30.0,
    )
    result = calculate(case)
    print(f"Frequency: {case.frequency_hz / 1e9:.3f} GHz")
    print(f"Wavelength: {result['wavelength_m'] * 1e3:.3f} mm")
    print(f"Spacing: {result['spacing_m'] * 1e3:.3f} mm")
    print(f"Progressive phase: {result['phase_deg']:.3f} deg")


if __name__ == "__main__":
    main()
