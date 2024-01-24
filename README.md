# GeminiPro-Streamlit-App

## Prerequisites
------------------------------------
To setup the application, follow the steps given below:

1. Clone the repository to your local machine.

2. Install the required dependencies:
   ```
   pip install python-dotenv
   pip install google-generativeai
   pip install streamlit
   ```

3. Obtain an API key from Google AI Studio and add it to the `.env` file in the project directory.
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

## Usage
-----------
To use the application, follow the steps given below:

1. Run the `app_qa.py` to understand about text-only prompts processed using gemini-pro model, as follows:
   ```
   streamlit run app_qa.py
   ```

2. Run the `app_vision.py` to understand about text and image prompts processed using gemini-pro-vision model, as follows:
   ```
   streamlit run app_vision.py
   ```

![image](https://github.com/amzadb/GeminiPro-Streamlit-App/assets/11292254/4a38163b-9e3b-4603-b223-fdb1d9747f81)
