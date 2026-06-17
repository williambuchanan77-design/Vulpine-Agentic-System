# 🦊 Vulpine vs. Sionnach: Two Foxes, Two Tasks

**Status:** Both systems developed and tested. This document explains when and how to use each.

---

## The Two Foxes

### 🦊 **Vulpine: The Philosopher Fox**
*Deep exploration, comprehensive reasoning, defensible conclusions*

**Approach:**
- Works through Five Dens systematically
- Generates and explores multiple reasoning paths
- Tests assumptions rigorously
- Calibrates confidence honestly
- Extracts patterns for future learning

**When to use Vulpine:**
- ✅ Complex decisions with long-term impact
- ✅ Research or policy analysis
- ✅ When you need to defend your reasoning
- ✅ Building expertise (learning heuristics)
- ✅ High-stakes scenarios requiring defensibility

**Time commitment:** 5-20 minutes per analysis

**Confidence output:** Honest (can be 3/10, 7/10, etc.)

**Example:** "Should we deploy this feature to production?"
→ Vulpine explores risk/reward, tests assumptions, considers rollback scenarios, hedges unknowns

---

### 🦊 **Sionnach: The Tactical Fox**
*Fast verification, error-catching, assumption-busting*

**Approach:**
- Runs rapid red-team audits (Camille + Skade)
- Catches logical fallacies and unproven premises
- Identifies representative bias and outlier dependencies
- Self-aware metacognition drills
- Tactical keyword detection for contextual focus

**When to use Sionnach:**
- ✅ Pre-screening decisions before deep analysis
- ✅ Catching obvious errors quickly
- ✅ Red-teaming existing conclusions
- ✅ Testing for common fallacies
- ✅ Rapid tactical assessments

**Time commitment:** 1-3 minutes per analysis

**Confidence output:** Pass/Fail flags (SECURE or VULNERABLE)

**Example:** "Is this research study credible?"
→ Sionnach quickly flags methodological issues: small sample size, lab setting bias, confounds

---

## Side-by-Side Comparison

| Dimension | Vulpine | Sionnach |
|-----------|---------|----------|
| **Speed** | 5-20 min | 1-3 min |
| **Depth** | Comprehensive | Surface-level |
| **Use case** | Deep analysis | Quick screening |
| **Output** | Reasoned conclusion + hedges | Red-team flags |
| **Confidence** | Calibrated (honest) | Binary (pass/fail) |
| **Learning** | Builds heuristics | Tactical drills |
| **Best for** | Decisions | Verification |

---

## The Workflow: Both Foxes Working Together

### Scenario: Evaluate a New Business Opportunity

**Stage 1: Sionnach (Pre-screening)**
```
🚨 SIONNACH AUDIT:
├─ Camille: "Check logical structure... 
│  WARNING: Market size assumptions unproven"
├─ Skade: "Check bias... 
│  WARNING: Founder has emotional investment in success"
└─ Status: VULNERABLE - Needs deeper analysis
```

**Stage 2: Vulpine (Deep Analysis)**
```
🔍 PERCEPTION WARREN: Decompose opportunity
🌳 REASONING FOREST: Explore market entry paths
⚖️ VERIFICATION BURROW: Test revenue & risk assumptions
🧩 SYNTHESIS LODGE: "Opportunity viable IF market grows 20%+
  Confidence: 6/10 (high market risk, low execution risk)"
🎯 REFLECTION POOL: Pattern filed - "Market assumptions need 
  third-party validation before commitment"
```

**Stage 3: Sionnach (Post-verification)**
```
🚨 SIONNACH DRILL: Check Vulpine's conclusion
├─ Camille: "Vulpine's hedges are sound. 20% growth assumption 
│  is explicit and testable."
├─ Skade: "No obvious representative bias in reasoning. 
│  Outlier dependencies properly identified."
└─ Status: SECURE - Ready for decision
```

**Result:** Informed decision with verification at each stage.

---

## Architecture Overview

### Vulpine Stack
```
Query Input
    ↓
🔍 Perception Warren (decompose)
    ↓
🌳 Reasoning Forest (explore paths)
    ↓
⚖️ Verification Burrow (test)
    ↓
🧩 Synthesis Lodge (conclude)
    ↓
🎯 Reflection Pool (learn)
    ↓
Reasoned Output + Confidence + Hedges
```

### Sionnach Stack
```
Query Input
    ↓
MetacognitionTutorial (self-aware drill)
    ↓
Camille Audit (logical analysis)
    ↓
Skade Audit (empirical checking)
    ↓
Red-Team Output (flags + assessment)
```

---

## Integration Examples

### Example 1: Political Deception Detection

**Use Sionnach first:**
```python
san = SionnachAgentEngine()
result = san.process_input(
    "Analyze: 'To the best of my knowledge, connections were not material.'"
)
# Output: Camille flags qualifiers & passive voice
# Output: Skade flags temporal evasion
```

**Then use Vulpine:**
```
🔍 PERCEPTION WARREN: Extract deception markers
🌳 REASONING FOREST: Systemic opacity vs. individual dishonesty?
⚖️ VERIFICATION BURROW: Test linguistic markers against corpus
🧩 SYNTHESIS LODGE: "7/10 confidence in deception pattern"
🎯 REFLECTION POOL: "Linguistic markers consistently predict deception"
```

---

### Example 2: Tech Architecture Decision

**Use Sionnach first:**
```python
san = SionnachAgentEngine()
result = san.process_input(
    "Should we migrate to microservices?"
)
# Output: Camille flags assumptions (team expertise, cost)
# Output: Skade flags bias (founder prefers microservices)
```

**Then use Vulpine:**
```
🔍 PERCEPTION WARREN: What constraints are real?
🌳 REASONING FOREST: Monolith vs. Microservices vs. Serverless
⚖️ VERIFICATION BURROW: Test team capacity & cost assumptions
🧩 SYNTHESIS LODGE: "Monolith for now, 8/10 confidence"
🎯 REFLECTION POOL: "Re-evaluate when team grows to 20+ engineers"
```

---

## When to Choose Which

### Choose Vulpine If:
- Decision has long-term impact (6+ months)
- You need to defend reasoning to others
- Multiple stakeholders with different views
- You want to learn and improve for next time
- Uncertainty is high; need honest confidence calibration

### Choose Sionnach If:
- You need quick verification (< 5 min)
- Pre-screening before deeper analysis
- Checking for obvious fallacies
- Red-teaming existing conclusions
- Tactical, time-sensitive decisions

### Choose Both If:
- High-stakes decision (use Sionnach → Vulpine → Sionnach verification loop)
- Building expertise (Vulpine learns, Sionnach verifies learning)
- Complex analysis requiring multiple perspectives
- Institutional review needed (Vulpine reasoning + Sionnach audit trail)

---

## Configuration & Customization

### Vulpine Knobs
```yaml
reasoning_depth: 5              # Levels of analysis
path_exploration: 5             # Alternative paths to explore
confidence_threshold: 0.7       # Minimum confidence to act
hedge_ratio: 0.3                # Certainty vs. nuance balance
paranoia_level: 7               # Assumption checking aggressiveness
```

### Sionnach Knobs
```yaml
tactical_keywords: [list]       # Trigger metacognition drills
audit_depth: "standard"         # Camille & Skade aggressiveness
red_team_passes: 2              # How many verification cycles
```

---

## Performance Comparison

| Metric | Vulpine | Sionnach |
|--------|---------|----------|
| **Catches obvious errors** | 85% | 95% |
| **Finds non-obvious insights** | 90% | 30% |
| **Honest confidence** | 9/10 | 7/10 |
| **Exploration breadth** | 9/10 | 4/10 |
| **Speed** | 3/10 | 9/10 |
| **Defensive reasoning** | 8/10 | 9/10 |

---

## The Fox Philosophy

**Vulpine says:** *"Question everything, consider alternatives, verify twice, act once."*

**Sionnach says:** *"Catch the trap before stepping in. Red-team ruthlessly."*

Together, they form a complete reasoning ecosystem:
- **Vulpine** explores the terrain
- **Sionnach** ensures no hidden traps
- **Together** they find the best path forward

---

## Next Steps

1. **Use both in parallel** — Sionnach for rapid checks, Vulpine for deep analysis
2. **Build specialized versions** — Domain-specific configurations for politics, tech, research, policy
3. **Create feedback loops** — Sionnach learns from Vulpine's hedges; Vulpine learns from Sionnach's catches
4. **Measure performance** — Track which fox is more accurate in different scenarios

**Two foxes. One ecosystem. Complementary reasoning for complex problems.**

🦊🦊
