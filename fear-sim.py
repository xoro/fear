#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-2-Clause
# Copyright (c) 2026, Timo Pallach (timo@pallach.de).

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass


@dataclass
class Environment:
    food_chance: float = 0.35
    water_chance: float = 0.30
    hazard_chance: float = 0.10
    safe_chance: float = 0.60

    def sample(self, rng: random.Random) -> dict[str, bool]:
        return {
            "food_available": rng.random() < self.food_chance,
            "water_available": rng.random() < self.water_chance,
            "hazard_present": rng.random() < self.hazard_chance,
            "safe_spot": rng.random() < self.safe_chance,
        }


@dataclass
class Creature:
    hunger: float = 10.0
    thirst: float = 10.0
    pain: float = 0.0
    reproduction_drive: float = 5.0
    fear: float = 0.0
    alive: bool = True

    def clamp(self) -> None:
        self.hunger = max(0.0, min(120.0, self.hunger))
        self.thirst = max(0.0, min(120.0, self.thirst))
        self.pain = max(0.0, min(120.0, self.pain))
        self.reproduction_drive = max(0.0, min(120.0, self.reproduction_drive))

    def update_internal_state(self) -> None:
        self.hunger += 4.0
        self.thirst += 5.0
        self.reproduction_drive += 2.0
        self.pain = max(0.0, self.pain - 1.5)
        self.clamp()

        if self.hunger >= 100.0 or self.thirst >= 100.0 or self.pain >= 100.0:
            self.alive = False

    def compute_fear(self, hazards: dict[str, bool]) -> float:
        hunger_threat = self.hunger / 100.0
        thirst_threat = self.thirst / 100.0
        pain_threat = self.pain / 100.0
        repro_threat = self.reproduction_drive / 120.0
        immediate_danger = 1.0 if hazards["hazard_present"] else 0.0

        # Fear prioritizes immediate danger and severe deficits.
        self.fear = max(
            immediate_danger,
            hunger_threat,
            thirst_threat,
            pain_threat,
            0.6 * repro_threat,
        )
        return self.fear

    def decide_action(self, hazards: dict[str, bool]) -> str:
        if hazards["hazard_present"]:
            return "avoid"

        threats = {
            "seek_water": self.thirst,
            "seek_food": self.hunger,
            "rest": self.pain * 0.9,
            "reproduce": self.reproduction_drive * 0.7,
        }
        return max(threats, key=threats.get)

    def act(self, action: str, hazards: dict[str, bool]) -> str:
        outcome = ""
        if action == "avoid":
            if hazards["safe_spot"]:
                self.pain = max(0.0, self.pain - 4.0)
                outcome = "Found safety; pain reduced."
            else:
                self.pain += 6.0
                outcome = "No safe spot; pain increased."
        elif action == "seek_food":
            if hazards["food_available"]:
                self.hunger = max(0.0, self.hunger - 30.0)
                outcome = "Found food; hunger reduced."
            else:
                self.hunger += 3.0
                outcome = "No food found; hunger increased."
        elif action == "seek_water":
            if hazards["water_available"]:
                self.thirst = max(0.0, self.thirst - 35.0)
                outcome = "Found water; thirst reduced."
            else:
                self.thirst += 4.0
                outcome = "No water found; thirst increased."
        elif action == "rest":
            if hazards["safe_spot"]:
                self.pain = max(0.0, self.pain - 6.0)
                outcome = "Rested safely; pain reduced."
            else:
                self.pain += 2.5
                outcome = "Rest interrupted; pain increased."
        elif action == "reproduce":
            if hazards["safe_spot"] and self.reproduction_drive >= 40.0:
                self.reproduction_drive = max(0.0, self.reproduction_drive - 25.0)
                outcome = "Reproductive effort succeeded."
            else:
                self.reproduction_drive += 3.0
                outcome = "Reproductive effort failed."
        else:
            outcome = "No action."

        self.clamp()
        return outcome


def simulate(steps: int, seed: int | None, verbose: bool) -> None:
    rng = random.Random(seed)
    env = Environment()
    creature = Creature()

    print("Fear-Driven Simulator (single creature)")
    if seed is not None:
        print(f"Seed: {seed}")
    print("-" * 60)

    for step in range(1, steps + 1):
        if not creature.alive:
            print(f"Step {step:03d}: Creature is no longer alive.")
            break

        hazards = env.sample(rng)
        creature.update_internal_state()
        fear = creature.compute_fear(hazards)
        action = creature.decide_action(hazards)
        outcome = creature.act(action, hazards)

        if verbose:
            print(
                f"Step {step:03d} | fear={fear:.2f} | "
                f"hunger={creature.hunger:.1f} thirst={creature.thirst:.1f} "
                f"pain={creature.pain:.1f} repro={creature.reproduction_drive:.1f} | "
                f"action={action} | {outcome}"
            )
        elif step % 5 == 0 or action == "avoid":
            print(
                f"Step {step:03d} | fear={fear:.2f} | "
                f"h={creature.hunger:.1f} t={creature.thirst:.1f} "
                f"p={creature.pain:.1f} r={creature.reproduction_drive:.1f} | "
                f"action={action}"
            )

    if creature.alive:
        print("Simulation complete: Creature survived.")
    else:
        print("Simulation complete: Creature did not survive.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Single-creature fear-driven simulator (console)."
    )
    parser.add_argument("--steps", type=int, default=50, help="Number of steps.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed.")
    parser.add_argument(
        "--verbose", action="store_true", help="Print every step with outcomes."
    )
    args = parser.parse_args()

    simulate(args.steps, args.seed, args.verbose)


if __name__ == "__main__":
    main()
