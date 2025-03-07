#📝 AI Downloads Organizer
📌 Overview
The AI Downloads Organizer is a Python script that automatically organizes files in your Downloads folder into categorized subfolders based on their file type. It leverages Google Gemini AI for intelligent categorization of unknown file types.

⚡ Features
✅ Automatically sorts files into categories (Images, Documents, Videos, Music, Archives, Code, etc.)
✅ Uses Google Gemini AI for intelligent file classification
✅ Moves files to respective folders within Downloads
✅ Easy to set up and use

📂 Folder Structure
bash
Copy
Edit
📁 AI-Downloads-Organizer
 ┣ 📜 organizer.py       # Main script
 ┣ 📜 .env               # Stores API key
 ┣ 📜 README.md          # Project documentation
 ┗ 📜 requirements.txt   # Required dependencies
🔧 Setup & Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/abhishek21121a/AI-Downloads-Organizer.git
cd AI-Downloads-Organizer
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Key
Create a .env file in the project root and add:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
5️⃣ Run the Script
sh
Copy
Edit
python organizer.py
📜 How It Works
1️⃣ Scans the Downloads folder for files
2️⃣ Identifies file types using Python & Gemini AI
3️⃣ Moves files into respective category folders
4️⃣ Keeps your Downloads folder clean & organized

🛠 Technologies Used
🔹 Python
🔹 Google Gemini AI
🔹 PDFMiner
🔹 Python-Magic
🔹 Dotenv

📌 Example Output
makefile
Copy
Edit
Moved: report.pdf → Documents/
Moved: photo.jpg → Images/
Moved: song.mp3 → Music/
📬 Contributing
Feel free to contribute by submitting a Pull Request! 😊
