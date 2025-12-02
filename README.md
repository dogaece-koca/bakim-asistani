# 🔧 AI-Powered Field Maintenance Agent

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%202.5-orange)

An intelligent, multimodal dialogue system designed to assist field technicians with real-time maintenance and troubleshooting. Powered by **Google Gemini 2.5 Flash**, this application utilizes **RAG (Retrieval-Augmented Generation)** to provide accurate answers based on uploaded technical manuals.

## 🚀 Live Demo
[Click here to view the Live App][https://bakim-asistani.streamlit.app](https://bakim-asistani-jpfvkf7kjyoqrzwpsqsthy.streamlit.app/) 

## ✨ Key Features

* **📄 Dynamic RAG System:** Upload any technical manual (PDF), and the AI instantly becomes an expert on that specific device.
* **📷 Multimodal Analysis:** Technicians can upload photos of faulty parts. The AI analyzes the visual data alongside the technical manual to diagnose issues.
* **🌍 Bilingual Support (TR/EN):** Automatically detects the language of the query.
    * Asks in **English** → Replies in **English**.
    * Asks in **Turkish** → Replies in **Turkish**.
* **⚡ High Performance:** Uses `gemini-2.5-flash` for low-latency responses, crucial for field operations.
* **📱 Mobile Friendly:** Designed with Streamlit to work seamlessly on tablets and smartphones used by field agents.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Model:** Google Gemini 2.5 Flash (via `google-generativeai`)
* **PDF Processing:** `pypdf`
* **Image Processing:** `Pillow` (PIL)

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

1.  **Upload Manual:** Open the sidebar and upload a PDF file (e.g., a refrigerator service manual).
2.  **Wait for Processing:** The system will extract text and memorize the content.
3.  **Ask a Question:** Type your technical question in the chat box.
4.  **Upload Image (Optional):** If you see a damaged part or an unknown error icon, upload its photo to get a visual diagnosis.

## 📸 Screenshots

<img width="1867" height="827" alt="image" src="https://github.com/user-attachments/assets/ac8b4895-dbd0-4b8c-b5fd-8bf0cfd163f9" />
<img width="1862" height="827" alt="image" src="https://github.com/user-attachments/assets/ba4d549d-8541-4297-99df-21d2c2d62dc1" />

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
