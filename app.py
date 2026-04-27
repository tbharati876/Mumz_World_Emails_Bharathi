# 1. INSTALL


# 2. SET OPEN API KEY and AUTH TOKEN

import os

os.environ["OPENROUTER_API_KEY"] = "Paste Open Router API Key here"
os.environ["NGROK_AUTH_TOKEN"] = "Paste you ngrok auth token here"

# 3. CREATE app.py

app_code = """
import streamlit as st
import requests
import json
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_email(email_text):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f\"\"\"
You are an AI system.

Return ONLY valid JSON. No text before or after.

Format:
{{
  "intent": "refund | exchange | complaint | inquiry | escalate | unknown",
  "urgency": "low | medium | high",
  "confidence": number between 0 and 1,
  "reasoning": "short explanation",
  "reply_en": "response in English",
  "reply_ar": "response in Arabic"
}}

If unsure, use "unknown".

Email:
{email_text}
\"\"\"

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    res = requests.post(url, headers=headers, json=data)

    try:
        result = res.json()
        content = result['choices'][0]['message']['content']

        # Extract JSON safely
        start = content.find("{")
        end = content.rfind("}") + 1
        json_str = content[start:end]

        return json.loads(json_str)

    except Exception as e:
        return {
            "error": "JSON parsing failed",
            "raw_output": content if 'content' in locals() else str(res.text)
        }


# UI

st.set_page_config(page_title="AI Mumz World Emails", layout="wide")

st.title("AI MUMZ World Emails📩 ")
st.markdown("Analyze emails (EN + AR)💬")

email = st.text_area("Enter your email", height=150)

if st.button("Analyze🔍"):
    if not email.strip():
        st.warning("Please enter an email")
    else:
        with st.spinner("Analyzing..."):
            result = analyze_email(email)

        if "error" in result:
            st.error("Parsing failed")
            st.text(result.get("raw_output", ""))
        else:
            col1, col2, col3 = st.columns(3)

            col1.metric("Intent🎯", result["intent"])
            col2.metric("Urgency⏳", result["urgency"])
            col3.metric("Confidence📊", result["confidence"])

            st.progress(result["confidence"])

            st.subheader("Reply (English)")
            st.write(result["reply_en"])

            st.subheader("Reply (Arabic)")
            st.write(result["reply_ar"])

            st.subheader("Reasoning📝")
            st.write(result["reasoning"])

            with st.expander("Raw JSON🗂️"):
                st.json(result)
"""

with open("app.py", "w") as f:
    f.write(app_code)

print("app.py created")

# 4. RUN STREAMLIT APP

!streamlit run app.py &>/content/logs.txt &
print("Streamlit running...")

# 5. START NGROK

from pyngrok import ngrok
ngrok.set_auth_token(os.environ["NGROK_AUTH_TOKEN"])
public_url = ngrok.connect(8501)
print("App is live", public_url)
