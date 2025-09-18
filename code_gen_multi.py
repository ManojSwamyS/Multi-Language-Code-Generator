import os
import google.generativeai as genai
import streamlit as st

# Configure the API key directly with the updated key
genai.configure(api_key="AIzaSyDZB0MFp5qBltsEb3N7X41fOgFc8eFl5BM")

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.5-pro')

def generate_code_from_prompt_and_lang(prompt, language):
    """
    Generates code in a specified language using the Gemini API.
    
    Args:
        prompt (str): A natural language description of the code to generate.
        language (str): The desired programming language (e.g., "Python", "C", "Java").
    
    Returns:
        str: The generated code.
    """
    try:
        # Construct a clear and specific prompt for the model
        full_prompt = (
            f"Write a {language} code snippet for the following request. "
            "Only provide the code, without any extra explanations or conversational text. "
            f"The request is: {prompt}"
        )
        
        # Call the API to generate content
        response = model.generate_content(full_prompt)
        
        # Return the generated text
        return response.text
        
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("💻 Multi-Language Code Generator ")
st.write("Generate code in C, Java, or Python using Gemini AI. ✨")

prompt = st.text_input("Enter your code request (e.g., 'Write a function to reverse a string.')")
language = st.selectbox("Select programming language", ["C", "C++", "C#", "Java", "Python"])

if st.button("Generate Code"):
    if prompt:
        with st.spinner("Generating code..."):
            code = generate_code_from_prompt_and_lang(prompt, language)
        st.session_state.generated_code = code
        st.session_state.original_prompt = prompt
        st.session_state.language = language
    else:
        st.error("Please enter a prompt.")

# Display generated code if available
if 'generated_code' in st.session_state:
    st.subheader(f"🔧 Generated {st.session_state.language} Code:")
    st.code(st.session_state.generated_code, language=st.session_state.language.lower())

# Refinement section
if 'generated_code' in st.session_state:
    st.subheader("🔄 Refine the Generated Code")
    additional_specs = st.text_area("Enter additional specifications or modifications (e.g., 'Make it more efficient' or 'Add comments')")
    if st.button("🔄 Refine Code"):
        if additional_specs:
            combined_prompt = f"{st.session_state.original_prompt}. Additional specifications: {additional_specs}"
            with st.spinner("Refining code..."):
                refined_code = generate_code_from_prompt_and_lang(combined_prompt, st.session_state.language)
            st.session_state.refined_code = refined_code
        else:
            st.error("Please enter additional specifications.")

# Display refined code if available
if 'refined_code' in st.session_state:
    st.subheader(f"✨ Refined {st.session_state.language} Code:")
    st.code(st.session_state.refined_code, language=st.session_state.language.lower())
