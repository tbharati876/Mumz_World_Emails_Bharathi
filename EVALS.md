
---

# EVALS.md

```md
# Evaluation

## Test Cases

| Input | Expected | Result |
|------|--------|--------|
| refund request | refund | ✅ |
| wrong size | exchange | ✅ |
| bad delivery | complaint | ✅ |
| urgent help | inquiry | ⚠️ |
| random question | unknown | ✅ |
| Arabic refund | refund | ✅ |

---

## Accuracy
~85%

---

## Failure Cases
- Very short inputs
- Mixed intent emails
- Out-of-domain queries

---

## Observations
- JSON sometimes malformed → fixed via extraction
- Arabic quality is good
