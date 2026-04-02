import streamlit as st
import speech_recognition as sr
import io
import time

st.set_page_config(page_title="Speech-to-Text Transcriber", page_icon="🎤", layout="centered")

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
body { font-family: 'Segoe UI', sans-serif; }
.stButton>button {
    background: linear-gradient(135deg, #6C63FF, #3B82F6);
    color: white; border: none; border-radius: 8px;
    padding: 0.5rem 1.5rem; font-size: 1rem; font-weight: 600;
    transition: 0.2s;
}
.stButton>button:hover { opacity: 0.85; transform: scale(1.02); }
.stTabs [data-baseweb="tab"] { font-size: 1rem; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

st.title("🎤 Speech-to-Text Transcriber")
st.write("Convert audio recordings into text using Python's **SpeechRecognition** library.")
st.markdown("---")

r = sr.Recognizer()

# ── Get available microphone names ──────────────────────────────────────────
@st.cache_data
def get_mic_list():
    try:
        return sr.Microphone.list_microphone_names()
    except Exception:
        return []

mic_list = get_mic_list()

tab1, tab2 = st.tabs(["📁 Upload Audio File", "🎙️ Record from Microphone"])

# ══════════════════════════════════════════════════════════════
# TAB 1 – Upload Audio File
# ══════════════════════════════════════════════════════════════
with tab1:
    st.subheader("Upload an Audio File")
    st.info("📌 Supported formats: **WAV**, **AIFF**, **FLAC**")

    audio_file = st.file_uploader("Choose an audio file", type=["wav", "aiff", "flac"])

    if audio_file:
        st.audio(audio_file)

    if st.button("🔠 Transcribe Uploaded File", key="btn_upload"):
        if audio_file is None:
            st.warning("⚠️ Please upload an audio file first.")
        else:
            with st.spinner("Transcribing... please wait."):
                try:
                    audio_bytes = audio_file.read()
                    audio_io = io.BytesIO(audio_bytes)
                    with sr.AudioFile(audio_io) as source:
                        audio_data = r.record(source)
                    text = r.recognize_google(audio_data)
                    st.success("✅ Transcription Complete!")
                    st.text_area("📝 Transcribed Text", text, height=180)
                    st.download_button(
                        label="⬇️ Download as .txt",
                        data=text,
                        file_name="transcription.txt",
                        mime="text/plain"
                    )
                except sr.UnknownValueError:
                    st.error("❌ Could not understand the audio. Try a clearer recording or a different file.")
                except sr.RequestError as e:
                    st.error(f"❌ Google API error: {e}\n\nMake sure you have an active internet connection.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

# ══════════════════════════════════════════════════════════════
# TAB 2 – Record from Microphone
# ══════════════════════════════════════════════════════════════
with tab2:
    st.subheader("Record Directly from Microphone")

    # ── Windows Privacy Warning ──────────────────────────────
    st.warning("""
⚠️ **Windows Microphone Privacy Check**  
If nothing is recorded, go to:  
**Start → Settings → Privacy → Microphone → Allow desktop apps to access your microphone → ON**
""")

    # ── Microphone Selector ──────────────────────────────────
    input_mics = [name for name in mic_list if "output" not in name.lower()
                  and "speaker" not in name.lower()
                  and "headphone" not in name.lower()
                  and "pc speaker" not in name.lower()]

    if input_mics:
        selected_mic_name = st.selectbox("🎙️ Select Microphone", input_mics)
        mic_index = mic_list.index(selected_mic_name)
    else:
        st.error("No input microphone found.")
        mic_index = None

    duration = st.slider("⏱️ Recording duration (seconds)", min_value=3, max_value=20, value=8)

    if st.button("▶️ Start Recording", key="btn_record") and mic_index is not None:
        status_box = st.empty()

        try:
            with sr.Microphone(device_index=mic_index) as source:
                status_box.info("🔧 Calibrating for background noise (1 sec)...")
                r.adjust_for_ambient_noise(source, duration=1)

                status_box.success(f"🎙️ **Listening! Speak now... ({duration} seconds)**")
                audio_data = r.listen(source, timeout=duration + 2, phrase_time_limit=duration)

            status_box.info("⏳ Transcribing your speech...")
            text = r.recognize_google(audio_data)
            status_box.empty()

            st.success("✅ Transcription Complete!")
            st.text_area("📝 Transcribed Text", text, height=180)
            st.download_button(
                label="⬇️ Download as .txt",
                data=text,
                file_name="microphone_transcription.txt",
                mime="text/plain"
            )

        except sr.WaitTimeoutError:
            status_box.error("⏰ Timed out — no speech detected. Try speaking louder or check your microphone settings.")
        except sr.UnknownValueError:
            status_box.error("❌ Could not understand the audio. Try again and speak clearly.")
        except sr.RequestError as e:
            status_box.error(f"❌ Google API error: {e}\n\nCheck your internet connection.")
        except OSError as e:
            status_box.error(f"❌ Microphone access failed: {e}")
        except Exception as e:
            status_box.error(f"❌ Unexpected error: {e}")

st.markdown("---")
st.caption("🎓 Internship Project | Speech-to-Text Transcription using Python SpeechRecognition")
