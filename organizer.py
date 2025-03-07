import os
import shutil
import google.generativeai as genai
import magic
import pdfminer.high_level
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: Missing Gemini API Key. Please set it in .env file.")
    exit()

genai.configure(api_key="API_KEY")

# Define paths
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# Categories based on file types
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Others": []
}


def get_file_category(file_path):
    """Categorizes a file using Gemini AI."""
    try:
        mime = magic.Magic(mime=True).from_file(file_path)
        file_ext = os.path.splitext(file_path)[1].lower()
        
        for category, extensions in CATEGORIES.items():
            if file_ext in extensions:
                return category
        
        # AI-based categorization for unknown types
        response = genai.chat.completions.create(
            model="gemini-pro",
            messages=[{"role": "user", "content": f"What category does this file belong to? {file_ext}"}]
        )
        return response.choices[0].message['content']
    
    except Exception as e:
        print(f"Error categorizing {file_path}: {e}")
        return "Others"

def organize_downloads():
    """Organizes the Downloads folder."""
    if not os.path.exists(DOWNLOADS_FOLDER):
        print("Downloads folder not found.")
        return
    
    for file_name in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file_name)
        
        if os.path.isfile(file_path):
            category = get_file_category(file_path)
            category_folder = os.path.join(DOWNLOADS_FOLDER, category)
            
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, file_name))
            print(f"Moved: {file_name} → {category}/")

if __name__ == "__main__":
    organize_downloads()
