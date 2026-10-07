import streamlit as st

from rag_pipeline import generate_answer


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="LearnAI | AI Teaching Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* =========================================
       GLOBAL
       ========================================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 50%,
            #f8fafc 100%
        );
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 5rem;
        max-width: 1250px;
    }


    /* =========================================
       SIDEBAR
       ========================================= */

    [data-testid="stSidebar"] {
        background: #f1f5f9;
    }

    .sidebar-logo {
        font-size: 25px;
        font-weight: 800;
        color: #312e81;
        margin-bottom: 4px;
    }

    .sidebar-subtitle {
        font-size: 13px;
        color: #64748b;
    }

    .status-card {
        padding: 9px 12px;
        margin: 7px 0;
        border-radius: 10px;
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #166534;
        font-size: 13px;
    }


    /* =========================================
       HERO
       ========================================= */

    .hero-container {
        padding: 38px 42px;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #312e81 0%,
            #4338ca 45%,
            #6366f1 100%
        );
        box-shadow: 0 18px 45px rgba(49, 46, 129, 0.25);
        margin-bottom: 28px;
    }

    .hero-small {
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #c7d2fe;
        margin-bottom: 8px;
    }

    .hero-title {
        font-size: 44px;
        font-weight: 850;
        color: white;
        margin: 0;
        line-height: 1.1;
    }

    .hero-description {
        color: #e0e7ff;
        font-size: 17px;
        line-height: 1.6;
        margin-top: 12px;
        max-width: 800px;
    }


    /* =========================================
       FEATURE CARDS
       ========================================= */

    .feature-card {
        background: white;
        padding: 22px 16px;
        border-radius: 18px;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 7px 24px rgba(15, 23, 42, 0.06);
        min-height: 145px;
    }

    .feature-icon {
        font-size: 30px;
        margin-bottom: 8px;
    }

    .feature-title {
        font-size: 16px;
        font-weight: 750;
        color: #0f172a;
    }

    .feature-description {
        font-size: 13px;
        color: #64748b;
        margin-top: 5px;
    }


    /* =========================================
       SECTION TITLE
       ========================================= */

    .section-heading {
        font-size: 24px;
        font-weight: 800;
        color: #0f172a;
        margin-top: 30px;
        margin-bottom: 12px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 15px;
    }


    /* =========================================
       SOURCE CARDS
       ========================================= */

    .source-card {
        padding: 13px 16px;
        border-radius: 12px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        margin-bottom: 8px;
    }

    .source-topic {
        font-weight: 700;
        color: #3730a3;
    }

    .source-file {
        font-size: 13px;
        color: #64748b;
        margin-top: 3px;
    }


    /* =========================================
       INFO BOX
       ========================================= */

    .info-box {
        padding: 18px 20px;
        border-radius: 16px;
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        margin-top: 25px;
    }


    /* =========================================
       FOOTER
       ========================================= */

    .footer {
        text-align: center;
        padding: 35px 0 10px;
        color: #64748b;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">🎓 LearnAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'RAG-Based AI Teaching Assistant'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🧭 Navigation")

    st.markdown("""
    💬 **Ask Question**

    📚 **Lecture Material**

    ℹ️ **About Project**
    """)

    st.divider()

    st.markdown("### 🟢 System Status")

    st.markdown(
        '<div class="status-card">🟢 RAG Engine Online</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-card">🟢 ChromaDB Connected</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-card">🟢 Gemini AI Connected</div>',
        unsafe_allow_html=True
    )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption(
        "Whisper • Sentence Transformers • "
        "ChromaDB • Gemini • Streamlit"
    )


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-container">
<div class="hero-small">AI-POWERED LEARNING PLATFORM</div>
<div class="hero-title">🎓 LearnAI</div>
<div class="hero-description">
RAG-Based AI Teaching Assistant
<br>
Ask questions from your educational lectures
and receive context-aware AI explanations.
</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# FEATURE CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎥</div>
        <div class="feature-title">Lecture Based</div>
        <div class="feature-description">
            Answers from educational material
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">RAG Powered</div>
        <div class="feature-description">
            Retrieval-Augmented Generation
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔎</div>
        <div class="feature-title">Semantic Search</div>
        <div class="feature-description">
            Meaning-based retrieval
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Gemini AI</div>
        <div class="feature-description">
            Natural language explanations
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# ASK SECTION
# =========================================================

st.markdown(
    '<div class="section-heading">💬 Ask Your Lecture</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Ask questions related to the lecture material and '
    'let LearnAI retrieve the most relevant information.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SUGGESTED QUESTIONS
# =========================================================

st.markdown(
    "#### 💡 Suggested Questions"
)

q1, q2 = st.columns(2)

suggested_question = None

with q1:
    if st.button(
        "🔹 What are quantum numbers?",
        use_container_width=True
    ):
        suggested_question = "What are quantum numbers?"

with q2:
    if st.button(
        "🔹 Explain quantum physics",
        use_container_width=True
    ):
        suggested_question = "Explain quantum physics"


q3, q4 = st.columns(2)

with q3:
    if st.button(
        "🔹 What is quantum computing?",
        use_container_width=True
    ):
        suggested_question = "What is quantum computing?"

with q4:
    if st.button(
        "🔹 Explain quantum numbers simply",
        use_container_width=True
    ):
        suggested_question = "Explain quantum numbers simply"


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):
            st.markdown(
                message["content"]
            )

    else:

        with st.chat_message(
            "assistant",
            avatar="🎓"
        ):

            st.markdown(
                message["content"]
            )

            # ---------------------------------------------
            # SOURCES
            # ---------------------------------------------

            if "sources" in message:

                with st.expander(
                    "📚 View Retrieved Lecture Sources"
                ):

                    sources = message["sources"]

                    if sources:

                        for i, source in enumerate(
                            sources,
                            start=1
                        ):

                            topic = source.get(
                                "topic",
                                "Unknown Topic"
                            )

                            filename = source.get(
                                "filename",
                                "Unknown Chunk"
                            )

                            st.markdown(
                                f"""
                                **{i}. 📚 {topic}**

                                📄 `{filename}`
                                """
                            )

                    else:

                        st.info(
                            "No source information available."
                        )


# =========================================================
# USER QUESTION INPUT
# =========================================================

question = st.chat_input(
    "💬 Ask something about your lectures..."
)


# =========================================================
# HANDLE SUGGESTED QUESTION
# =========================================================

if suggested_question:

    question = suggested_question


# =========================================================
# PROCESS QUESTION
# =========================================================

if question:

    # =====================================================
    # DISPLAY USER QUESTION
    # =====================================================

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(question)


    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # =====================================================
    # GENERATE AI RESPONSE
    # =====================================================

    with st.chat_message(
        "assistant",
        avatar="🎓"
    ):

        with st.spinner(
            "🔎 Searching lecture material..."
        ):

            try:

                result = generate_answer(
                    question
                )

                answer = result["answer"]

                metadatas = result["metadatas"]


                # -----------------------------------------
                # AI ANSWER
                # -----------------------------------------

                st.markdown(
                    answer
                )


                # -----------------------------------------
                # SOURCES
                # -----------------------------------------

                with st.expander(
                    "📚 View Retrieved Lecture Sources"
                ):

                    for i, source in enumerate(
                        metadatas,
                        start=1
                    ):

                        topic = source.get(
                            "topic",
                            "Unknown Topic"
                        )

                        filename = source.get(
                            "filename",
                            "Unknown Chunk"
                        )

                        st.markdown(
                            f"""
                            **{i}. 📚 {topic}**

                            📄 `{filename}`
                            """
                        )


                # -----------------------------------------
                # SAVE AI MESSAGE
                # -----------------------------------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": metadatas
                    }
                )


            except Exception as e:

                st.error(
                    "⚠️ Unable to generate an answer."
                )

                st.caption(
                    f"Technical details: {str(e)}"
                )


# =========================================================
# HOW THE SYSTEM WORKS
# =========================================================

st.markdown(
    '<div class="section-heading">🧠 How LearnAI Works</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">

    <b>1. 🎥 Lecture Videos</b><br>
    Educational videos are processed using Whisper AI.

    <br><br>

    <b>2. 📝 Text Processing</b><br>
    Transcripts are divided into smaller overlapping chunks.

    <br><br>

    <b>3. 🔢 Semantic Embeddings</b><br>
    Sentence Transformers convert lecture chunks into
    numerical representations.

    <br><br>

    <b>4. 🗄️ ChromaDB</b><br>
    Embeddings are stored in a vector database for
    semantic similarity search.

    <br><br>

    <b>5. 🤖 Gemini AI</b><br>
    Relevant lecture information is provided to Gemini,
    which generates the final student-friendly answer.

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    🎓 <b>LearnAI</b> — RAG-Based AI Teaching Assistant

    <br><br>

    Whisper • Sentence Transformers • ChromaDB •
    Gemini • Streamlit

    <br><br>

    <i>Making recorded lectures interactive and searchable.</i>

    </div>
    """,
    unsafe_allow_html=True
)