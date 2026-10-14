from langchain_core.prompts import PromptTemplate

# Create a reusable prompt template
# The placeholders inside {} will be replaced later
# with actual user inputs

template = PromptTemplate(

    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with:
"Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",

    # Variables that must be provided when using the template
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],

    # Validate that all variables used in the template
    # actually exist in input_variables
    validate_template=True
)

# Save the prompt template as a JSON file
# so it can be reused later without rewriting the prompt

template.save("template.json")