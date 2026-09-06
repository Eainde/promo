# New Work — Coding Standards: Checkstyle & Spotless via Maven Mixins

## Overview
Identified that the business unit had no shared coding standards — no formatting rules, no static analysis enforcement. Built common Maven mixins that bundle Checkstyle (static rule enforcement) and Spotless (automatic code formatting), enabling any microservice to adopt consistent quality with minimal configuration. Now the standard across every microservice in the business unit.

## Problem
- No consistent code formatting across teams — every developer and team had their own style
- No static analysis rules enforced at build time
- Code reviews wasted time on style debates instead of logic
- No automated quality gates for code hygiene

## Solution
- Created shared **Maven mixins** — reusable build configuration modules that any microservice can inherit
- **Checkstyle mixin** — enforces static coding rules (naming conventions, code structure, complexity limits) at build time
- **Spotless mixin** — automatic code formatting on every build, eliminating style inconsistencies
- Teams adopt by adding a single parent/mixin reference — no per-project configuration needed

## Impact
- **Standard across every microservice in the business unit** — not optional, not partial, the standard
- Eliminated code style debates in reviews — formatting is automated
- Consistent codebase quality across all teams
- New joiners get immediate guardrails — code quality enforced from first commit
- Reduced review friction, faster onboarding

## Why This Matters for Promotion
- Demonstrates initiative — nobody asked for this, identified the gap independently
- Shows influence — drove adoption across the entire business unit
- Engineering quality leadership — raising the bar beyond own team
- Firmwide/division-wide contribution — exactly what panel flagged as weak last year

## ECDF Mapping

| ECDF Dimension | How This Maps |
|---|---|
| **Thinks** | Identified gap in engineering quality, created reusable solution |
| **Influences** | Drove adoption of standards across entire business unit |
| **Achieves** | Quality culture, continuous improvement — now the unit-wide standard |
| **Controls** | Engineering governance — automated quality enforcement |
| **Delivers** | Shipped reusable Maven mixins, zero-config adoption for teams |
