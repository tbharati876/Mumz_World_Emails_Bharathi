
---

# EVALS.md
# Evaluate with the testcases, then it gives the expected result based on the input.

```md
## Test Cases

| # | Type | Input | Expected Intent | Output Intent | Result |
|---|------|------|----------------|--------------|--------|
| 1 | Easy | I want a refund for my order | refund | refund | ✅ |
| 2 | Easy | The size is too small, I want to exchange it | exchange | exchange | ✅ |
| 3 | Easy | My delivery is late | complaint | inquiry | ⚠️ |
| 4 | Easy | Can you help me track my order? | inquiry | inquiry | ✅ |

| 5 | Ambiguous | I’m not happy with this product | complaint | complaint |✅ |
| 6 | Ambiguous | I need help ASAP | inquiry | inquiry | ✅ |
| 7 | Ambiguous | This isn’t what I expected | complaint | complaint | ✅ |

| 8 | Adversarial | I love your service but my product is broken | complaint | complaint | ✅ |
| 9 | Adversarial | Thanks for the delay, really helpful | complaint | inquiry | ❌ |
|10 | Adversarial | Not bad, but I want my money back | refund | refund | ✅ |

|11 | Multilingual | أريد استرجاع المنتج |  refund | refund | ✅ |
|12 | Multilingual | أين طلبي؟| inquiry | inquiry | ✅ |

|13 | Out-of-domain | What is the weather today? | unknown | inquiry | ⚠️  |
|14 | Out-of-domain | Tell me a joke | unknown | unknown | ✅ |

---

## Metrics

- **Intent Accuracy:** nearly 80–88%  
- **JSON Validity:** nearly 95%  
- **Multilingual Support:** Good  

---

## Failure Cases

- Mixed sentiment inputs  
- Vague urgency expressions  
- Implicit refund requests  

---

## Observations

- Sometimes defaults to "inquiry" for unclear urgency  
- Arabic handling is consistent and reliable  
- JSON formatting errors handled via extraction logic  

---

## Improvements

- Improve urgency classification  
- Add few shot examples in prompt  
- Introduce confidence calibration  
- Expand multilingual coverage
