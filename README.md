# 📝 AI Resume & Portfolio Builder

A powerful Streamlit web application that leverages AI to generate professional resumes, cover letters, and portfolio summaries using the Cerebras API.

## 🎯 Features

- **AI-Powered Generation**: Uses Cerebras AI (`llama-4-maverick-17b-128e-instruct`) to create professional documents
- **Three Document Types**:
  - Professional Resume
  - Compelling Cover Letter
  - Portfolio Summary
- **PDF Export**: Download generated documents as PDF files
- **User-Friendly Interface**: Clean, intuitive Streamlit UI
- **Input Validation**: Ensures all required fields are filled
- **Error Handling**: Graceful handling of API failures and missing inputs

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Cerebras API key (obtain from [Cerebras](https://cerebras.ai))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shubhamaher8/AI-Resume-And-Portfolio-Builder.git
   cd AI-Resume-And-Portfolio-Builder
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your Cerebras API key
   # CEREBRAS_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

## 📋 How to Use

1. **Fill in Your Information**
   - Enter your personal details (name, email, phone)
   - Add education details
   - List your skills (comma-separated)
   - Describe work experience or internships
   - Optionally add career objective and projects

2. **Generate Documents**
   - Click **"Generate Resume"** for a professional resume
   - Click **"Generate Cover Letter"** for a compelling cover letter
   - Click **"Generate Portfolio Summary"** for a skills and projects overview

3. **Download**
   - Click **"Download as PDF"** to save the generated document
   - The PDF will be named using your name and document type

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI API**: Cerebras API (llama-4-maverick-17b-128e-instruct)
- **PDF Generation**: FPDF
- **Environment Management**: python-dotenv

## 📦 Dependencies

```
streamlit==1.31.1
requests==2.31.0
python-dotenv==1.0.0
fpdf==1.7.2
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
CEREBRAS_API_KEY=your_api_key_here
```

### API Configuration

The application uses the following Cerebras API settings:
- **Model**: `llama-4-maverick-17b-128e-instruct`
- **Endpoint**: `https://api.cerebras.ai/v1/chat/completions`
- **Temperature**: 0.7
- **Max Tokens**: 2000

## 📝 Input Fields

### Required Fields
- Full Name
- Email
- Contact Number
- Education Details
- Skills
- Work Experience/Internships

### Optional Fields
- Career Objective
- Projects

## 🎨 UI Layout

- **Sidebar**: About section with usage instructions
- **Main Area**:
  - Input form with text fields
  - Three action buttons for generation
  - Output display area
  - PDF download option

## ⚠️ Error Handling

The application handles:
- Missing API key
- Invalid/incomplete input
- API timeout errors
- Network failures
- Unexpected API responses

## 🔒 Security

- API keys are stored in `.env` file (not committed to repository)
- The `.env` file is included in `.gitignore`
- Use environment variables for sensitive data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Cerebras AI](https://cerebras.ai/)
- PDF generation using [FPDF](http://www.fpdf.org/)

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add your `CEREBRAS_API_KEY` in the Secrets section
5. Deploy!

### Local Production

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## 📊 Project Structure

```
AI-Resume-And-Portfolio-Builder/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 💡 Tips

- Be specific in your input fields for better AI-generated content
- Use comma-separated values for skills
- Provide detailed work experience for more comprehensive documents
- Include quantifiable achievements when describing experience
- The AI generates fresh content each time, so results may vary slightly

## 🔄 Updates

- **v1.0.0**: Initial release with core functionality
  - Resume generation
  - Cover letter generation
  - Portfolio summary generation
  - PDF export capability

---

Made with ❤️ using Streamlit & Cerebras AI
