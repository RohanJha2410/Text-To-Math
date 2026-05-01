import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.chains import LLMMathChain, LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents import AgentType, AgentExecutor
from langchain_core.tools import Tool
from langchain_classic.agents import initialize_agent
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
load_dotenv()


## Set upi the Stramlit app
st.set_page_config(page_title="Text To Math Problem Solver And Data Search Assistant",page_icon="🧮")
st.title("Text To Math Problem Solver Using OpenAI")

groq_api_key=os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

llm=ChatGroq(model="openai/gpt-oss-120b",groq_api_key=groq_api_key)


# initializig  the tools
wikipedia_wrapper=WikipediaAPIWrapper()

def wikipedia_func(query: str) -> str:
    return wikipedia_wrapper.run(query)

wikipedia_tool=Tool(
    name='Wikipedia',
    func=wikipedia_func,
    description='A tool for searching the internet to find the various information on the topics mentioned'
)

# initialise the math tool
math_prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""You are a strict math expression generator. 
Given a math problem, you must output a single mathematical expression that solves the problem.
The expression must be valid for Python's numexpr library.


Question: {question}
"""
)

math_chain=LLMMathChain.from_llm(llm=llm, prompt=math_prompt_template)

def calculator_func(query: str) -> str:
    return math_chain.run(query)

calculator_tool=Tool(
    name='Calculator',
    func=calculator_func,
    description='A tool for answering math related questions. Only input mathematical expression needs to be provided.'
)

prompt="""
You are a agent tasked for solving users mathematical question. Logically arrive at the solution and provide a detailed explanation and display it pointwise for the question below
Question: {question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=['question'],
    template=prompt
)

## Combine all the tools in chain

chain=LLMChain(llm=llm,prompt=prompt_template)

def reasoning_func(query: str) -> str:
    return chain.run(query)

reasoning_tool=Tool(
    name='Reasoning Tool',
    func=reasoning_func,
    description='A tool for answering logic-based and reasoning questions.'
)

# initialise the agents
assistant_agent=initialize_agent(
    tools=[wikipedia_tool, calculator_tool, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a Math chatbot who can answer all your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])


## LEts start the interaction
question=st.text_area("Enter your question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("Find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")


