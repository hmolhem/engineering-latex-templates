"""Minimal reproducible calculation for the report-template example."""

from __future__ import annotations

import numpy as np


def steering_vector(angle_deg: float, sensors: int = 4, spacing_lambda: float = 0.5) -> np.ndarray:
    """Return a normalized ULA steering vector."""
    if sensors < 1:
        raise ValueError("sensors must be positive")
    angle_rad = np.deg2rad(angle_deg)
    phase = 2.0 * np.pi * spacing_lambda * np.sin(angle_rad)
    index = np.arange(sensors, dtype=float)
    return np.exp(1j * index * phase) / np.sqrt(sensors)


def main() -> None:
    angle_deg = 18.0
    vector = steering_vector(angle_deg)
    covariance = np.outer(vector, vector.conj())
    hermitian_error = np.linalg.norm(covariance - covariance.conj().T)

    print(f"Input angle: {angle_deg:.1f} deg")
    print(f"Sensor count: {vector.size}")
    print(f"Hermitian error: {hermitian_error:.3e}")
    print("Status: PASS" if hermitian_error < 1e-12 else "Status: FAIL")


if __name__ == "__main__":
    main()
