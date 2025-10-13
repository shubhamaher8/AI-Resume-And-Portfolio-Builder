# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- Cerebras API key from https://cerebras.ai

## Installation (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
# CEREBRAS_API_KEY=your_actual_api_key_here
```

### 3. Run the Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## How to Use

1. **Fill in your details** in the form (required fields marked with *)
2. **Click a generate button**:
   - 📄 Generate Resume
   - ✉️ Generate Cover Letter  
   - 💼 Generate Portfolio Summary
3. **View the AI-generated content**
4. **Download as PDF** (optional)

## Required Fields
- Full Name
- Email
- Contact Number
- Education Details
- Skills (comma-separated)
- Work Experience/Internships

## Optional Fields
- Career Objective
- Projects

## Troubleshooting

### "API key not found" error
- Make sure you created the `.env` file
- Verify your API key is set correctly in `.env`

### "API request failed" error
- Check your internet connection
- Verify your Cerebras API key is valid
- Ensure you have API credits available

### Import errors
- Run `pip install -r requirements.txt` again
- Ensure you're using Python 3.8 or higher

## Project Structure
```
AI-Resume-And-Portfolio-Builder/
├── app.py                      # Main application
├── requirements.txt            # Dependencies
├── .env.example               # Environment template
├── .env                       # Your API key (create this)
├── README.md                  # Full documentation
├── FEATURES.md                # Feature details
├── DEMO_OUTPUT_EXAMPLES.md    # Sample outputs
└── QUICKSTART.md             # This file
```

## Key Features
✅ AI-powered document generation  
✅ Professional Streamlit UI  
✅ PDF export functionality  
✅ Input validation  
✅ Error handling  
✅ Session state management  

## Support
- Check README.md for detailed instructions
- Review FEATURES.md for technical details
- See DEMO_OUTPUT_EXAMPLES.md for sample outputs

---

**Ready to build your professional documents with AI!** 🎉
