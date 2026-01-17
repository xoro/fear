<!--
SPDX-License-Identifier: BSD-2-Clause
Copyright (c) 2026, Timo Pallach (timo@pallach.de).
-->

# Fear-Driven Simulator

A simulation that models fear as an overarching motivational system for species preservation.

See `FEAR.md` for the theoretical background across neurology, psychology, sociology, and philosophy.

## Definition of Fear

In this project, **fear** encompasses a broad spectrum of emotional and physiological responses to perceived threats or uncertainty. This ranges from:

- **Mild unease**: A subtle strange feeling in the stomach, a sense that something isn't quite right
- **Anxiety**: Persistent, future-oriented worry about potential or uncertain threats
- **Dread**: Intense anticipatory apprehension about something expected or looming, involving a sense of inevitability
- **Acute fear**: Immediate emotional response to a clear, present danger
- **Panic**: Sudden, overwhelming fear reaction with strong physiological symptoms, often without a clearly defined external trigger
- **Terror**: Extreme, catastrophic fear state at the moment of peak threat or confrontation
- **Phobia**: Intense, often irrational fear of specific objects, situations, or outcomes

Fear is not limited to extreme reactions. It includes all levels of threat perception and discomfort that motivate organisms to take protective or preventive action. This definition acknowledges that fear operates on a continuum, from barely noticeable bodily sensations to overwhelming psychological states that can dominate behavior.

## Concept: Fear as an Overarching System

### The Two Main Drivers of Species Preservation

1. **Fear (self-preservation drive)** - Protects the individual from danger
2. **Reproductive drive** - Ensures the continuation of genes

### Fear as a Central Motivational System

Fear is not just one drive among many, but an **overarching system** that monitors and amplifies all other basic needs:

#### Fear as a Reaction to Threats Against Basic Needs

- **Hunger → Fear**: "What if I can't find food?" → motivates intensive food-seeking
- **Thirst → Fear**: "What if I can't find water?" → motivates intensive water-seeking
- **Pain → Fear**: "What if the injury gets worse?" → amplifies pain avoidance
- **Reproduction → Fear**: "What if my genes aren't passed on?" → motivates reproductive behavior

### Fear as a Motivation Amplifier

**Without fear:**
- Hunger → mild discomfort
- Thirst → mild discomfort

**With fear:**
- Hunger → existential threat → urgent search
- Thirst → existential threat → urgent search

Fear increases urgency and prioritizes behavior.

## Other Important Drives

### Primary Drives (Critical for Survival)
- **Hunger/food drive**: Energy for bodily functions
- **Thirst**: Water balance, often more urgent than hunger
- **Pain avoidance**: Protection from injury
- **Sleep/rest need**: Recovery and energy conservation

### Reproductive Drives
- **Reproductive drive**: Passing on genes
- **Caregiving drive**: Investment in offspring

### Social Drives
- **Social drive**: Group belonging and protection
- **Aggression/competition drive**: Defense of resources
- **Territoriality**: Securing resources

### Developmental/Learning Drives
- **Curiosity/learning**: Exploration and adaptation
- **Play drive**: Skill development

## Hierarchy of Drives

### Fear as an Overarching System

```
Fear (overarching)
  ├─ Fear of hunger → food-seeking
  ├─ Fear of thirst → water-seeking
  ├─ Fear of pain → avoidance
  ├─ Fear of death → self-preservation
  └─ Fear of extinction → reproduction
```

### Prioritization

**Critical for survival (immediate):**
- Breathing
- Pain avoidance
- Escape from immediate danger

**Short-term (days):**
- Thirst
- Hunger
- Sleep

**Medium-term (weeks/months):**
- Reproduction
- Social bonds
- Territory

**Long-term (years/generations):**
- Learning and adaptation
- Innovation
- Evolutionary change

## Interactions and Conflicts

Different drives can conflict:

- **Hunger vs. fear**: Seek food despite danger?
- **Reproduction vs. self-preservation**: Risk for a mate?
- **Social drive vs. competition**: Cooperation or conflict?
- **Curiosity vs. fear**: Explore or avoid?

## Modeling for the Simulation

### Fear as a Central System

```
Fear-Level = f(
  Hunger-Threat,
  Thirst-Threat,
  Pain-Threat,
  Reproductive-Threat,
  Social-Threat
)

Behavior = f(Fear-Level, specific drive)
```

### Fear as an Amplifier

```
Motivation = BaseDrive × (1 + Fear-Multiplier)
```

### Fear as a Prioritizer

Fear evaluates all threats, selects the greatest one, and activates corresponding behavior.

## Scientific Foundations

- **Evolutionary psychology**: These drives are shaped by natural selection
- **Behavioral ecology**: Cost-benefit trade-offs between survival and reproduction
- **Life history theory**: Trade-offs between investment in survival vs. reproduction

## Neurobiological Mapping (High-Level)

This project uses behavioral abstractions. A neurobiological mapping would relate those abstractions to brain systems and signals:

- **Threat detection / fear**: amygdala, periaqueductal gray, and the HPA axis (stress response)
- **Homeostatic needs (hunger, thirst)**: hypothalamus, brainstem nuclei, and hormonal signals (e.g., ghrelin, vasopressin)
- **Pain avoidance**: spinal nociceptive pathways, thalamus, anterior cingulate cortex
- **Motivation / reward**: dopamine systems (ventral tegmental area, nucleus accumbens)
- **Social and caregiving drives**: oxytocin/vasopressin systems, limbic circuits

These are simplified associations to guide future extensions of the model.

## Conclusion

Fear can be understood as an overarching system that:
1. Detects threats to basic needs
2. Amplifies urgency
3. Prioritizes behavior
4. Triggers emergency responses

The two main drivers are therefore:
1. **Fear** (overarching motivational system)
2. **Reproductive drive** (a distinct drive, also amplified by fear)
