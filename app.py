import gradio as gr

from RAG_Pipeline.pipeline import ask_question


def chatbot(question):
    """
    Run the Corrective RAG pipeline and prepare the UI output.
    """

    answer, retrieved_chunks, rewritten_query = ask_question(question)

    # Collect unique source documents
    sources = []

    for chunk in retrieved_chunks:

        source = f"{chunk['folder']} / {chunk['file_name']}"

        if source not in sources:
            sources.append(source)

    source_text = "\n".join(sources)

    # Query rewrite status
    if rewritten_query is None:

        status = "✅ Original Query Used"
        rewritten_query = "No query rewriting was required."

    else:

        status = "🔄 Query Rewritten"

    return answer, rewritten_query, status, source_text


# ---------------------- CSS ----------------------

css = """

.gradio-container{
    max-width:1100px !important;
    margin:auto;
}

footer{
    visibility:hidden;
}

"""


# ---------------------- UI ----------------------

with gr.Blocks(
    title="Corrective RAG System"
) as demo:

    gr.Markdown("""
# 🤖 Corrective RAG System

### Intelligent Document Question Answering

This system retrieves relevant document chunks, evaluates their quality,
rewrites the query when necessary, and generates reliable answers using
verified context only.
""")

    # Suggested Questions
    with gr.Accordion("💡 Suggested Questions", open=True):

        gr.Markdown("""
- What are the admission requirements for new students?
- What scholarships are available for students?
- What are the tuition payment policies?
""")

    # ---------------------- Input ----------------------

    question = gr.Textbox(
        label="💬 Ask Your Question",
        placeholder="Example: What are the admission requirements for new students?",
        lines=3
    )

    # ---------------------- Buttons ----------------------

    with gr.Row():

        ask_btn = gr.Button(
            "🚀 Generate Answer",
            variant="primary"
        )

    # ---------------------- Outputs ----------------------

    answer = gr.Textbox(
        label="🤖 Generated Answer",
        lines=10,
        interactive=False
    )

    status = gr.Textbox(
        label="📊 Retrieval Status",
        interactive=False
    )

    rewritten = gr.Textbox(
        label="🔄 Rewritten Query",
        lines=2,
        interactive=False
    )

    with gr.Accordion("📄 Source Documents", open=False):

        sources = gr.Textbox(
            lines=6,
            interactive=False
        )

    # ---------------------- Clear Button ----------------------

    clear_btn = gr.ClearButton(
        components=[
            question,
            answer,
            status,
            rewritten,
            sources
        ],
        value="🗑 Clear"
    )

    # ---------------------- Events ----------------------

    ask_btn.click(
        fn=chatbot,
        inputs=question,
        outputs=[
            answer,
            rewritten,
            status,
            sources
        ]
    )

# ---------------------- Launch ----------------------

demo.launch(
    css=css,
    theme=gr.themes.Soft()
)