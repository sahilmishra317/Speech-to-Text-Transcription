# 🎤 Speech-to-Text Transcription

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Transform spoken words into written text with this intuitive web application! Built with Python and Streamlit, this tool leverages Google's powerful Speech Recognition API to deliver accurate transcriptions from audio files or live microphone recordings.

## ✨ Features

- **📁 Audio File Upload**: Transcribe pre-recorded audio files in WAV, AIFF, or FLAC formats
- **🎙️ Live Microphone Recording**: Record directly from your microphone with customizable duration (3-20 seconds)
- **🎯 Smart Microphone Selection**: Choose from available input devices for optimal recording
- **⬇️ Download Transcriptions**: Save your results as .txt files for easy sharing and storage
- **🔧 Noise Calibration**: Automatic background noise adjustment for clearer recordings
- **⚡ Real-time Feedback**: Live status updates during recording and transcription
- **🛡️ Error Handling**: Comprehensive error messages for troubleshooting
- **📱 Responsive Design**: Clean, modern UI that works on desktop and mobile

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Active internet connection (required for Google Speech API)
- Microphone access (for recording feature)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sahilmishra317/Speech-to-Text-Transcription.git
   cd Speech-to-Text-Transcription
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📖 Usage

### Transcribing Audio Files
1. Click on the **"📁 Upload Audio File"** tab
2. Upload your audio file (WAV, AIFF, or FLAC)
3. Click **"🔠 Transcribe Uploaded File"**
4. View and download your transcription

### Recording from Microphone
1. Switch to the **"🎙️ Record from Microphone"** tab
2. Select your preferred microphone from the dropdown
3. Adjust recording duration using the slider
4. Click **"▶️ Start Recording"** and speak clearly
5. Wait for transcription to complete
6. Download the result if needed

### Windows Microphone Setup
If recording doesn't work on Windows:
- Go to **Settings → Privacy → Microphone**
- Enable **"Allow desktop apps to access your microphone"**

## 🛠️ Technical Details

- **Framework**: Streamlit for the web interface
- **Speech Engine**: Google Speech Recognition API
- **Audio Processing**: SpeechRecognition library with PyAudio support
- **Supported Formats**: WAV, AIFF, FLAC for file uploads
- **Output**: Plain text transcriptions with download capability

## 📋 Requirements

- `streamlit`
- `speechrecognition`
- `pyaudio` (for microphone access)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 About

This project was developed as part of an internship program, demonstrating the integration of speech recognition technology with modern web frameworks.

---

**Made with ❤️ using Python and Streamlit**</content>
<parameter name="filePath">c:\Users\Lenovo\OneDrive\Desktop\Speech-to-Text Transcription\README.md