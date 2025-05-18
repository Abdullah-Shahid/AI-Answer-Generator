from google import genai
import pyttsx3

# --- Gemini (Google Generative AI) Setup ---
def sendtoGemini(topic):
    client = genai.Client(api_key="YOUR_API_KEY_HERE")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents= f"Generate answer for this question '{topic}' in single paragraph. Only generate answer don't say here is... etc. Also don't use bold or italic. Only write it in paragraph form.",
    ) 
    generated_text = response.text.strip() 
    return generated_text


# Initialize the TTS engine
engine = pyttsx3.init()

# --- Text-to-Speech Setup ---
def speak(text):
    engine.say(text)
    engine.runAndWait()


# main part
while True:
    try:
        topic = input("Enter your question: ")
        print(f"Here is the answer:\n{sendtoGemini(topic)}")
        speak(sendtoGemini(topic))
        break
    except Exception as e:
        print("Following Error occured: {0}".format(e))
        print("Please Try Again..")
