# MathsGPT: Text To Math Problem Solver And Data Search Assistant

MathsGPT is a Streamlit-based AI application designed to act as a powerful math problem solver and an intelligent reasoning assistant. Powered by LangChain and Groq API, it seamlessly combines mathematical computation, logic-based reasoning, and Wikipedia search to provide detailed and accurate answers to user queries.

## 🚀 Features

- **Math Problem Solving**: Leverages LangChain's `LLMMathChain` and Python's `numexpr` library to accurately compute complex mathematical expressions.
- **Logic & Reasoning**: Uses a dedicated reasoning tool to break down logic-based questions and provide step-by-step, detailed explanations.
- **Wikipedia Integration**: Integrates the Wikipedia API to search the internet and provide relevant factual information on various topics.
- **Interactive Chat UI**: Built with Streamlit, the app offers a user-friendly conversational interface with step-by-step thought processes displayed during query execution.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Orchestration**: [LangChain](https://python.langchain.com/) (`langchain`, `langchain-groq`, `langchain-community`, `langchain-classic`)
- **Language Model**: Groq API (`ChatGroq`)
- **Math Evaluation**: `numexpr`
- **Data Source**: Wikipedia API Wrapper

## ⚙️ Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/RohanJha2410/Text-To-Math.git
cd Text-To-Math
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory of the project and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application
Start the Streamlit development server:
```bash
streamlit run app.py
```

## 💡 Usage

1. Open your browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
2. You will be greeted by the Math Chatbot assistant.
3. Type your mathematical problem or reasoning question in the text area.
4. Click **"Find my answer"** and watch the assistant break down the problem step-by-step before providing the final answer.

## 📂 Project Structure

- `app.py`: The main entry point of the Streamlit application containing the UI logic and LangChain agent initialization.
- `requirements.txt`: List of Python dependencies required to run the application.
- `.env`: Environment variables file (you need to create this) for securely storing API keys.
