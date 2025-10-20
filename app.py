import streamlit as st
import requests
import os
from dotenv import load_dotenv
from fpdf import FPDF
import tempfile
import re

# Configure page
st.set_page_config(
    page_title="AI Resume & Portfolio Builder",
    page_icon="📝",
    layout="wide"
)

# Unified API Key Access for Local and Cloud
load_dotenv()
try:
    CEREBRAS_API_KEY = st.secrets["CEREBRAS_API_KEY"]
except Exception:
    CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")

CEREBRAS_API_URL = "https://api.cerebras.ai/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b"


def generate_ai_content(prompt_text):
    """
    Generate AI content using Cerebras API
    
    Args:
        prompt_text (str): The prompt to send to the AI
        
    Returns:
        str: Generated content or error message
    """
    if not CEREBRAS_API_KEY:
        return "⚠️ Error: CEREBRAS_API_KEY not found. Please set it in your .env file."
    
    headers = {
        "Authorization": f"Bearer {CEREBRAS_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are a professional career advisor and content writer specializing in resumes, cover letters, and portfolios."
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        "temperature": 0.7,
        "max_tokens": 2000
    }
    
    try:
        response = requests.post(CEREBRAS_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        content = data['choices'][0]['message']['content']
        return content
    
    except requests.exceptions.Timeout:
        return "⚠️ Error: Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: API request failed - {str(e)}"
    except KeyError:
        return "⚠️ Error: Unexpected API response format."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def construct_resume_prompt(user_data):
    """Construct a prompt for resume generation"""
    prompt = f"""Create a professional resume for the following candidate:

Name: {user_data['name']}
Email: {user_data['email']}
Phone: {user_data['phone']}

Career Objective:
{user_data.get('objective', 'Seeking a challenging position to utilize my skills and contribute to organizational growth.')}

Education:
{user_data['education']}

Skills:
{user_data['skills']}

Work Experience:
{user_data['experience']}

Projects:
{user_data.get('projects', 'N/A')}

Please format this as a professional resume with clear sections, bullet points, and proper structure. Make it ATS-friendly and impactful."""
    return prompt


def construct_cover_letter_prompt(user_data):
    """Construct a prompt for cover letter generation"""
    prompt = f"""Write a professional cover letter for the following candidate:

Name: {user_data['name']}
Email: {user_data['email']}
Phone: {user_data['phone']}

Education: {user_data['education']}
Skills: {user_data['skills']}
Experience: {user_data['experience']}
Career Objective: {user_data.get('objective', 'Seeking opportunities to grow professionally')}

Create a compelling cover letter that highlights their strengths, expresses enthusiasm, and explains why they would be a great fit for potential employers. Keep it professional and concise (around 3-4 paragraphs)."""
    return prompt


def construct_portfolio_prompt(user_data):
    """Construct a prompt for portfolio summary generation"""
    prompt = f"""Create a brief portfolio summary for:

Name: {user_data['name']}
Skills: {user_data['skills']}
Projects: {user_data.get('projects', 'N/A')}
Experience: {user_data['experience']}
Education: {user_data['education']}

Write a concise portfolio summary that showcases their technical skills, key projects, and professional accomplishments. This should serve as an overview of their capabilities and expertise. Format it professionally with clear sections."""
    return prompt


def strip_markdown(md_text):
    # Remove basic markdown formatting for plain text output
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', md_text)  # bold
    text = re.sub(r'\*(.*?)\*', r'\1', text)         # italic
    text = re.sub(r'`(.*?)`', r'\1', text)           # inline code
    text = re.sub(r'^#+\s?', '', text, flags=re.MULTILINE)  # headers
    text = re.sub(r'^-\s?', '', text, flags=re.MULTILINE)   # lists
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)         # links
    return text


def generate_pdf(content, filename):
    """
    Generate a PDF from text content
    
    Args:
        content (str): Text content to convert to PDF
        filename (str): Name for the PDF file
        
    Returns:
        str: Path to the generated PDF file
    """
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        
        # Strip markdown before writing
        plain_content = strip_markdown(content)
        for line in plain_content.split('\n'):
            if line.strip():
                # Handle special characters
                line = line.encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 8, line)
            else:
                pdf.ln(4)
        
        # Save to temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', mode='wb')
        pdf.output(temp_file.name)
        temp_file.close()
        
        return temp_file.name
    
    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")
        return None


def validate_inputs(user_data):
    """Validate that required fields are filled"""
    required_fields = ['name', 'email', 'phone', 'education', 'skills', 'experience']
    missing_fields = [field for field in required_fields if not user_data.get(field, '').strip()]
    
    if missing_fields:
        return False, f"Please fill in the following required fields: {', '.join(missing_fields)}"
    return True, ""


# Main App UI
def main():
    # Sidebar
    with st.sidebar:
        st.title("ℹ️ About")
        st.info("AI-powered tool to generate professional resumes, cover letters, and portfolio summaries using AI Assistant.")
        st.markdown("---")
        st.markdown("### How to use:")
        st.markdown("1. Fill in your details")
        st.markdown("2. Click a generate button")
        st.markdown("3. Download as PDF (optional)")
    
    # Main Title
    st.title("📝 AI Resume & Portfolio Builder")
    st.markdown("### Create professional documents with AI assistance")
    st.markdown("---")
    
    # Input Form
    st.header("📋 Your Information")
    
    # Stack all input fields vertically
    name = st.text_input("Full Name *", placeholder="John Doe")
    email = st.text_input("Email *", placeholder="john.doe@example.com")
    phone = st.text_input("Contact Number *", placeholder="+1 234 567 8900")
    objective = st.text_area("Career Objective (optional)", 
                             placeholder="Brief description of your career goals...",
                             height=100)
    education = st.text_area("Education Details *", 
                            placeholder="e.g., B.Sc. Computer Science, XYZ University (2020-2024)",
                            height=100)
    skills = st.text_area("Skills (comma-separated) *", 
                         placeholder="Python, JavaScript, Machine Learning, etc.",
                         height=100)
    experience = st.text_area("Work Experience / Internships *", 
                             placeholder="Describe your work experience, internships, or relevant roles...",
                             height=120)
    projects = st.text_area("Projects (optional)", 
                           placeholder="Describe your key projects with brief descriptions...",
                           height=120)
    st.markdown("---")
    
    # Prepare user data
    user_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'objective': objective,
        'education': education,
        'skills': skills,
        'experience': experience,
        'projects': projects
    }
    
    # Action Buttons
    st.header("🚀 Generate Documents")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        generate_resume = st.button("📄 Generate Resume", use_container_width=True, type="primary")
    
    with col2:
        generate_cover = st.button("✉️ Generate Cover Letter", use_container_width=True, type="primary")
    
    with col3:
        generate_portfolio = st.button("💼 Generate Portfolio Summary", use_container_width=True, type="primary")
    
    st.markdown("---")
    
    # Initialize session state for storing generated content
    if 'generated_content' not in st.session_state:
        st.session_state.generated_content = None
    if 'content_type' not in st.session_state:
        st.session_state.content_type = None
    
    # Handle Resume Generation
    if generate_resume:
        is_valid, error_msg = validate_inputs(user_data)
        if not is_valid:
            st.error(error_msg)
        else:
            with st.spinner("🤖 Generating your resume... This may take a few seconds."):
                prompt = construct_resume_prompt(user_data)
                content = generate_ai_content(prompt)
                st.session_state.generated_content = content
                st.session_state.content_type = "Resume"
    
    # Handle Cover Letter Generation
    if generate_cover:
        is_valid, error_msg = validate_inputs(user_data)
        if not is_valid:
            st.error(error_msg)
        else:
            with st.spinner("🤖 Generating your cover letter... This may take a few seconds."):
                prompt = construct_cover_letter_prompt(user_data)
                content = generate_ai_content(prompt)
                st.session_state.generated_content = content
                st.session_state.content_type = "Cover Letter"
    
    # Handle Portfolio Generation
    if generate_portfolio:
        is_valid, error_msg = validate_inputs(user_data)
        if not is_valid:
            st.error(error_msg)
        else:
            with st.spinner("🤖 Generating your portfolio summary... This may take a few seconds."):
                prompt = construct_portfolio_prompt(user_data)
                content = generate_ai_content(prompt)
                st.session_state.generated_content = content
                st.session_state.content_type = "Portfolio Summary"
    
    # Display Generated Content
    if st.session_state.generated_content:
        st.header(f"✨ Generated {st.session_state.content_type}")
        
        # Display content in a styled container
        with st.container():
            st.markdown(st.session_state.generated_content)
        
        st.markdown("---")
        
        # Download as PDF button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            # Use st.download_button directly, no extra button appears
            pdf_bytes = None
            if st.session_state.generated_content:
                # Generate PDF bytes in memory
                pdf_path = generate_pdf(
                    st.session_state.generated_content, 
                    f"{st.session_state.content_type.lower().replace(' ', '_')}.pdf"
                )
                if pdf_path:
                    with open(pdf_path, 'rb') as pdf_file:
                        pdf_bytes = pdf_file.read()
                # Clean up temp file
                try:
                    os.unlink(pdf_path)
                except:
                    pass

            if pdf_bytes:
                st.download_button(
                    label="📥 Download as PDF",
                    data=pdf_bytes,
                    file_name=f"{name.replace(' ', '_')}_{st.session_state.content_type.replace(' ', '_')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        
        with col2:
            if st.button("🔄 Clear Output", use_container_width=True):
                st.session_state.generated_content = None
                st.session_state.content_type = None
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Built with ❤️ using Streamlit</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
