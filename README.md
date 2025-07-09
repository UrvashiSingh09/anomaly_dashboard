# 🚨 Anomaly Detection Dashboard

A web-based dashboard built using Django and Pandas that automatically detects anomalies in datasets. This tool is ideal for monitoring and visualizing irregularities in time series or tabular data.

---

## 📌 Features

- 📊 Real-time anomaly detection
- 🧠 Data processing with `pandas`
- 🌐 Interactive front-end using HTML/CSS
- 🔌 Backend built on Django framework
- 💡 Simple UI to display detected anomalies
- 📁 CSV file upload and visualization

---

## 🔧 Technologies Used

- Python 3.13
- Django
- Pandas
- HTML/CSS
- Bootstrap (optional for styling)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/anomaly-detection-dashboard.git
cd anomaly-detection-dashboard
2. Set Up Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, manually install:

bash
Copy
Edit
pip install django pandas
4. Run the Server
bash
Copy
Edit
python manage.py runserver
Visit http://localhost:8000 to see the dashboard.

📁 Project Structure
csharp
Copy
Edit
anomaly_detection/
├── anomaly_dashboard/      # Django project settings
│   └── urls.py
├── dashboard/              # Main app
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── anomaly_data.csv        # Sample dataset
├── manage.py
└── README.md

📷 Screenshots<img width="1470" alt="Screenshot 2025-07-10 at 00 28 59" src="https://github.com/user-attachments/assets/c890174b-be2d-4097-88f5-5e23326e71e8" />

✍️ Author
Urvashi Singh
📧 urvashisingh082004@gmail.com
🔗 LinkedIn

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

