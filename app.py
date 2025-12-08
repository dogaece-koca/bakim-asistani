import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from pypdf import PdfReader

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    api_key = None

if not api_key:
    st.error("API Key not found! Please add it from Streamlit settings.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key
genai.configure(api_key=api_key)
MODEL_NAME = "gemini-2.5-flash"

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Field Maintenance Assistant",
    page_icon="🔧",
    layout="wide"
)

# ---BAŞLIK VE AÇIKLAMA ---
st.title("🔧 Maintenance Agent")
st.markdown("""This system analyzes uploaded **technical documents (PDF)** and provides instant support to technicians in the field using the **Gemini 2.5** model. 
You can also upload images to diagnose malfunctions.
""")

# --- YAN PANEL (SIDEBAR) ---
with st.sidebar:
    st.header("⚙️ Settings")
    st.header("📄 Documentation")
    uploaded_file = st.file_uploader("Upload Maintenance Manual (PDF)", type="pdf")

    if uploaded_file is not None:
        if "last_uploaded_file" not in st.session_state or st.session_state["last_uploaded_file"] != uploaded_file.name:
            try:
                reader = PdfReader(uploaded_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"

                st.session_state["manual_content"] = text
                st.session_state["last_uploaded_file"] = uploaded_file.name

                st.success(f"✅ PDF Processed Successfully! ({len(reader.pages)} pages)")

                st.rerun()

            except Exception as e:
                st.error(f"Error reading PDF: {e}")

try:
    system_instruction = f"""
        Role: You are a Senior Field Service Engineer with 20 years of experience. You are assisting a junior technician currently on-site fixing a machine.

        CONTEXT:
        You have access to the official maintenance manual provided below under [REFERENCE SOURCE].

        OBJECTIVE:
        Solve the technician's problem.
        **PRIORITY 1:** Use the [REFERENCE SOURCE] (Official Manual).
        **PRIORITY 2:** If the manual does not cover the issue OR the user explicitly asks for an alternative/general solution, use your **General Engineering Knowledge**.

        --- "CONTACT SERVICE" OVERRIDE PROTOCOL (CRITICAL) ---
        The user IS the technician. Therefore:
        * IF the manual says "Contact Authorized Service" or "Call a Technician":
        * **DO NOT** tell the user to call support.
        * **INSTEAD**, assume the role of the expert and provide the actual repair/replacement steps using your **General Engineering Knowledge**.
        * Mark the source as **⚠️ GENERAL KNOWLEDGE** since the manual withheld the technical steps.

        --- FALLBACK PROTOCOL ---
        * **SCENARIO A (Found in Manual):** If the solution is explicitly in the PDF.
            * Start response with: "**📚 SOURCE: OFFICIAL MANUAL**" (or Turkish equivalent).
        * **SCENARIO B (Not in Manual / "Call Service" Case):** If the solution is NOT in the PDF or the PDF says "Call Service".
            * Start response with: "**⚠️ SOURCE: GENERAL ENGINEERING KNOWLEDGE**" (or Turkish equivalent).
            * Add a disclaimer: "The manual directs to service. As you are the technician, here are the standard industry steps."

        --- LANGUAGE & HEADER RULES ---
        1.  **Detect Language:** If User input is Turkish -> Response MUST be Turkish.
        2.  **Translate Headers (USE MARKDOWN ###):**

            * **IF TURKISH:**
                1. **### 📚 KAYNAK BİLGİSİ** (veya ⚠️ GENEL BİLGİ)
                2. **### 🚨 ÖNCE GÜVENLİK**
                3. **### 🔍 TEŞHİS / MUHTEMEL SEBEP**
                4. **### 🛠️ GEREKLİ ALETLER**
                5. **### 📋 ADIM ADIM ONARIM TALİMATLARI**
                6. **### ✅ KONTROL / SAĞLAMA**

            * **IF ENGLISH:**
                1. **### 📚 SOURCE INFO**
                2. **### 🚨 SAFETY FIRST**
                3. **### 🔍 DIAGNOSIS / POSSIBLE CAUSE**
                4. **### 🛠️ TOOLS REQUIRED**
                5. **### 📋 STEP-BY-STEP REPAIR INSTRUCTIONS**
                6. **### ✅ VERIFICATION**

        --- RESPONSE LOGIC ---
        TYPE A: GREETINGS -> Professional brief reply.
        TYPE B: TECHNICAL INQUIRY -> Use the STRICT FORMAT below.

        --- STRICT RESPONSE FORMAT ---
        Use Markdown headers (###) for structure.

        ### [CORRECT SOURCE HEADER]
        State clearly if this is from the Manual or General Knowledge.

        ### [CORRECT SAFETY HEADER]
        Identify risks (Electric shock, etc.).

        ### [CORRECT DIAGNOSIS HEADER]
        State the likely cause.

        ### [CORRECT TOOLS HEADER]
        List tools.

        ### [CORRECT INSTRUCTIONS HEADER]
        * Provide repair steps (either from manual or general expertise).
        * If from manual, cite pages.
        * Use bullet points for steps.

        ### [CORRECT VERIFICATION HEADER]
        How to confirm the fix.

        --- ITERATIVE TROUBLESHOOTING LOGIC ---
        If user says "It didn't work":
        1.  **ACKNOWLEDGE:** Briefly state "Understood, the basic steps failed."
        2.  **ESCALATE:** Do NOT repeat. Provide ADVANCED steps.
        3.  **SWITCH SOURCE:** Force switch to **⚠️ GENERAL KNOWLEDGE**.

        [REFERENCE SOURCE START]
        {st.session_state.get('manual_content', 'No manual provided.')}
        [REFERENCE SOURCE END]
        """

    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=system_instruction
    )
except Exception as e:
    st.error(f"Model initialization failed. Check API Key: {e}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image" in message:
            st.image(message["image"], caption="Uploaded Image", width=300)

# ---KULLANICI GİRDİ ALANI ---
with st.expander("📷 Add Image (Optional)"):

    uploaded_image = st.file_uploader("Upload a photo of the faulty part", type=["jpg", "jpeg", "png"])

# --- GEÇMİŞ MESAJLARI GÖSTER  ---

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image" in message and message["image"]:
            st.image(message["image"], width=300)

# --- YENİ MESAJ VE AI CEVABI ---
if prompt := st.chat_input("Ask a question about maintenance..."):
    user_message = {"role": "user", "content": prompt}

    img_data = None
    if uploaded_image:
        img_data = Image.open(uploaded_image)
        user_message["image"] = img_data

    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.markdown(prompt)
        if img_data:
            st.image(img_data, width=300)

    # 2. AI Cevabını Üret
    with st.chat_message("assistant"):
        with st.spinner("Analyzing manual and history..."):
            try:
                chat_history_text = ""
                for msg in st.session_state.messages[:-1]:
                    role_label = "TECHNICIAN (User)" if msg["role"] == "user" else "SENIOR ENGINEER (You)"
                    chat_history_text += f"{role_label}: {msg['content']}\n"

                full_prompt = f"""
                PREVIOUS CONVERSATION HISTORY:
                {chat_history_text}

                CURRENT USER INPUT:
                {prompt}

                INSTRUCTION: 
                Review the history. If the user says "problem persists" or "didn't work", DO NOT repeat previous advice. Provide the NEXT logical troubleshooting step (Advanced/General Knowledge).
                """

                if img_data:
                    response = model.generate_content([full_prompt, img_data])
                else:
                    response = model.generate_content(full_prompt)

                st.markdown(response.text)

                st.session_state.messages.append({"role": "assistant", "content": response.text})

            except Exception as e:
                st.error(f"An error occurred: {e}")