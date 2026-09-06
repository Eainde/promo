# New Work — PromptLint: Static Quality Analyzer for LLM Prompts

## Overview
A Java library that statically analyzes LLM prompt quality **without making any LLM calls**. Scores prompts across 8 quality dimensions, flags issues by severity, produces detailed reports. Runs in milliseconds, integrates into CI, and catches prompt regressions before they hit production.

Created as part of the Nexus AI ecosystem to ensure quality assurance for AI prompts across dbCLM.

## Core Philosophy
"Prompts are code." They define how LLM agents behave, what they extract, what format they return. Yet unlike application code, prompts have no linting, no static analysis, and no automated quality gates. In practice, prompts silently degrade over time. Someone adds vague language, removes the output schema, or introduces contradictory rules. The LLM starts hallucinating or returning malformed output, and nobody can pinpoint when the regression happened because nobody was testing the prompt.

PromptLint brings the discipline of static analysis to LLM prompts.

## Key Benefits
- **Rule-based, deterministic analysis** — no LLM calls, no API keys, no latency
- **8 orthogonal quality dimensions** — from clarity and specificity to injection resistance
- **Weighted scoring by agent type** — extraction agents weight groundedness higher, formatters weight output contract higher
- **CI integration** — set a quality threshold, run on every commit, fail the build on regressions
- **JUnit assertion API** — test prompts the same way you test code
- Analysis runs in **milliseconds**. No network calls, no API keys, no flaky tests. The same prompt always produces the same score, fully deterministic

## 8 Quality Dimensions

| Dimension | Code | What it Checks |
|---|---|---|
| **Clarity** | CLR | Role definition, task statement, imperative verbs, vague language detection, output format section, task-before-rules ordering |
| **Specificity** | SPC | Numbered rules, concrete examples, quantified thresholds, boundary conditions, enum constraints |
| **Groundedness** | GND | Source-grounding phrases, anti-hallucination guards, evidence requirements, citation instructions |
| **Output Contract** | OUT | JSON examples present and valid, field-level documentation, schema completeness |
| + 4 more dimensions | | Additional quality checks covering other aspects of prompt quality |

Each dimension analyzer produces a score between 0.0 and 1.0. The overall score is a **weighted average** of all dimension scores, where the weights come from the selected agent type profile.

## Architecture — Key Components

| Component | Responsibility |
|---|---|
| **PromptUnderTest** | Wraps the prompt with metadata: system/user text, declared inputs/outputs, agent profile |
| **PromptQualityAnalyzer** | Orchestrates all dimension analyzers, aggregates scores using profile weights |
| **PromptTypeProfile** | Defines weights per agent type (EXTRACTION, CLASSIFICATION, FORMATTING, REVIEW, DEFAULT) |
| **PromptQualityReport** | Holds overall score, per-dimension scores, and all findings |
| **PromptQualityReportRenderer** | Renders reports as formatted console output (CI-friendly) |
| **PromptQualityAssert** | Fluent assertion API for JUnit tests |

## Agent Type Profiles
Different agent types have different quality priorities:
- **Extraction agents** — weight groundedness and output contract higher
- **Classification agents** — weight specificity higher
- **Formatting agents** — weight output contract higher
- Custom agent type profiles (dimension weights) are supported
- Custom rule authoring for individual dimensions is on the roadmap

## REST API
Exposes analysis via REST endpoint for non-Java teams or integration with Confluence. Builder-style API to build Agent profile and send for analysis.

## Integration
- **Maven dependency** — add to pom.xml
- **Basic usage** — import PromptQualityAnalyzer, create analyzer, run analysis, get report
- **JUnit** — use PromptQualityAssert for fluent assertion API
- **CI** — set quality threshold, fail build on regressions

## FAQ
- **No LLM API calls** — all analysis is rule-based and deterministic, runs entirely in-process
- **Dependencies** — only Jackson (jackson-databind) for JSON validation in Output Contract analyzer
- **Java 17** or higher required
- **Scoring** — each dimension produces 0.0 to 1.0, overall is weighted average based on agent type profile (e.g., EXTRACTION profile weights Groundedness at 0.25 and Specificity at 0.15)

## Roadmap

| Item | Status |
|---|---|
| Core analyzer with 8 dimensions | DONE |
| Agent type profiles | DONE |
| Fluent assertion for prompt quality testing | DONE |
| Built-in profiles: EXTRACTION, CLASSIFICATION, FORMATTING, REVIEW, DEFAULT | DONE |
| Custom rule authoring | PLANNED |
| Auto-fix suggestions | PLANNED |

## ECDF Mapping

| ECDF Dimension | How This Maps |
|---|---|
| **Thinks** | Innovative approach — treating prompts as code, bringing static analysis discipline to AI |
| **Designs** | Full architecture with extensible profiles, pluggable analyzers, CI integration |
| **Delivers** | Complete library shipped with 8 dimensions, agent profiles, JUnit API, REST API |
| **Controls** | Quality gates for AI prompts — same philosophy as Maven Mixin for code quality |
| **Influences** | Setting quality standards for AI prompt engineering across dbCLM |
| **Achieves** | Catches prompt regressions before production, deterministic quality enforcement |

## Relationship to Nexus AI
PromptLint complements Nexus AI by providing the quality assurance layer:
- Nexus AI = the agentic framework (how agents are built and orchestrated)
- PromptLint = the quality tooling (how prompts are tested and validated)
- Together they show end-to-end ownership of AI engineering at dbCLM

## Screenshots Reference
- PromptLint documentation: framework/IMG_3496.jpg through IMG_3500.jpg
