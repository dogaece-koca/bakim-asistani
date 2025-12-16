# 🔧 AI-Powered Field Maintenance Agent

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%202.5-orange)
![Architecture](https://img.shields.io/badge/Architecture-Long%20Context%20Agent-green)

A state-aware, multimodal dialogue agent designed to assist field technicians with real-time maintenance and troubleshooting. Unlike traditional chatbots, this system acts as a **Senior Field Engineer**, utilizing **Google Gemini 2.5 Flash**'s massive context window to digest entire technical manuals instantly, enforcing strict safety protocols, and adapting its reasoning based on conversation history.

## 🚀 Live Demo
[Click here to view the Live App](https://maintenance-agent-jpfvkf7kjyoqrzwpsqsthy.streamlit.app)

## ✨ Key Features & Technical Innovations

### 🧠 Hybrid Knowledge Architecture
The system employs a tiered retrieval logic to prevent hallucinations:
* **Tier 1 (Official Manual):** Prioritizes the uploaded PDF to ensure compliance.
* **Tier 2 (General Knowledge Fallback):** Automatically switches to "General Engineering Knowledge" if the manual lacks specific repair steps, clearly tagging the source (e.g., `⚠️ SOURCE: GENERAL KNOWLEDGE`).

### 📖 Holistic Document Understanding (Long Context)
Instead of traditional RAG (chunking), this agent injects the **entire technical manual** into the model's context window. This preserves critical cross-references (e.g., linking an error code on page 50 to a wiring diagram on page 120) that split-search methods often miss.

### 🔄 State-Aware Troubleshooting (Memory)
The agent possesses **Conversational Memory**. It remembers previous steps and adapts its advice.
* *User:* "It didn't work."
* *Agent:* Acknowledges the failure and automatically **escalates** to advanced diagnostics (e.g., PCB inspection) instead of repeating the same basic steps.

### 🛡️ Protocol-Driven Safety
Every response is structurally enforced to follow a mandatory workflow:
1.  **🚨 Safety First:** Immediate risk warnings (High Voltage, Pressure, etc.).
2.  **🛠️ Tools Required:** Listing specific equipment needed.
3.  **📋 Step-by-Step Instructions:** Active, imperative commands.
4.  **✅ Verification:** How to confirm the fix.

### 📷 Native Multimodality (Visual Diagnosis)
Technicians can upload photos of faulty parts. The AI performs **pixel-level analysis** to identify defects (corrosion, burnt components, cracks) and correlates them with the manual's troubleshooting section.

### 🌍 Dynamic Localization (TR/EN)
Automatically detects the technician's language and adapts technical headers/terminology instantly.
* **Turkish Input** → Turkish Persona & Headers (ÖNCE GÜVENLİK, vb.)
* **English Input** → English Persona & Headers (SAFETY FIRST, etc.)

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Reasoning Engine:** Google Gemini 2.5 Flash (via `google-generativeai`)
* **Data Processing:** `pypdf` (Text extraction), `Pillow` (Image processing)
* **Architecture:** Long Context Injection + System Instruction Engineering

## ⚙️ Installation & Local Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dogaece-koca/bakim-asistani.git](https://github.com/dogaece-koca/bakim-asistani.git)
    cd bakim-asistani
    ```

2.  **Install requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Key:**
    * Get your API key from [Google AI Studio](https://aistudio.google.com/).
    * Create a `.streamlit/secrets.toml` file in the root directory:
    ```toml
    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

## 📖 How to Use

1.  **Upload Manual:** Open the sidebar and upload a service manual PDF.
2.  **Initialize:** The agent ingests the full document and adopts the "Senior Engineer" persona.
3.  **Ask or Show:** Type a problem (e.g., "Fridge leaking water") or upload a photo of the defect.
4.  **Iterate:** If a solution fails, say "It didn't work". The agent will remember the context and guide you through deeper inspection steps.

## 📸 Screenshots

<img width="945" height="445" alt="image" src="https://github.com/user-attachments/assets/665ad08d-dd17-4e43-ae36-61a3d0cd692a" />
<img width="1795" height="799" alt="image" src="https://github.com/user-attachments/assets/4aefeadf-7655-4ad0-9d66-90ca6dd4fbde" />
<img width="1810" height="803" alt="image" src="https://github.com/user-attachments/assets/e8b305b5-1c6a-41b6-b6d9-8990bdd0dab1" />
<img width="1807" height="816" alt="image" src="https://github.com/user-attachments/assets/0484be50-cfee-4f02-9d48-019ac9f3238f" />

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
