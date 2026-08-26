# 🚀 Rocket Mission Control

> A beginner Python project that simulates a basic rocket mission readiness check using fundamental programming concepts.

## 📌 Overview

**Rocket Mission Control** is the first mini-project developed during my **Python in 30 Days** journey, following the first six days of learning.

The program collects basic rocket and mission data, calculates key parameters, performs a series of pre-launch checks, and determines whether the rocket is **ready for launch or the launch should be aborted**.

---

## 🧠 Concepts Applied

* Variables & data types
* User input
* Type conversion
* Arithmetic operations
* Expressions
* `if / else` statements
* Logical operators (`and`)
* `for` loops
* `range()`
* F-strings
* Basic program flow

---

## ⚙️ How It Works

The program asks the user for:

* 🚀 Rocket name
* ⚖️ Rocket mass
* ⛽ Fuel mass
* 🔥 Number of engines
* 🌍 Destination

It then calculates:

* **Dry Mass** — total rocket mass excluding fuel
* **Fuel Percentage** — percentage of the rocket's mass represented by fuel

The program then performs three basic tests:

```text
FUEL     → READY / ERROR
ENGINES  → READY / ERROR
MASS     → CHECKED / ERROR
```

If all three conditions are satisfied, the system gives the final status:

```text
STATUS: READY FOR LAUNCH
```

and starts a five-second countdown before displaying:

```text
LIFTOFF!
```

Otherwise:

```text
STATUS: LAUNCH ABORTED
```

---

## 💻 Example

```text
Rocket Name: Falcon
Rocket Mass: 500
Fuel Mass: 300
Number of Engines: 9
Destination: Orbit

ROCKET REPORT:
Rocket Name: Falcon
Rocket Mass: 500.0
Fuel Mass: 300.0
Number of Engines: 9
Destination: Orbit
Dry Mass: 200.0
Fuel Percentage: 60.0

ROCKET TESTS:

FUEL: READY
ENGINES: READY
MASS: CHECKED

STATUS: READY FOR LAUNCH

T 5
T 4
T 3
T 2
T 1

LIFTOFF!
```

---

## 🎯 Purpose

The purpose of this project was to combine the concepts learned during **Days 1–6** into a complete, working Python program.

It is a first step toward applying programming to **engineering and aerospace-related problems**.

---

### Python in 30 Days · Project 01

**Learn → Apply → Build → Improve**
