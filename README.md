<img width="1921" height="909" alt="FOOD MOOD LIST OF CITIES" src="https://github.com/user-attachments/assets/7b0b9063-c7a7-4373-b649-6ed98e235ebc" /># 🍽️ Food Mood App

A Flask web application that recommends restaurants based on your current mood and location.

## Features
- 🔐 User authentication (login/signup)
- 🏙️ City selection from major cities
- 😊 Mood-based food recommendations (Happy, Sad, Relaxed, Angry, Frustrated)
- 🍴 Integration with Foursquare Places API
- 📱 Responsive design with Bootstrap
- ⭐ Restaurant ratings and price levels

## Technologies Used
- Flask (Python web framework)
- Bootstrap 5 (Frontend styling)
- Foursquare Places API
- HTML/CSS/JavaScript

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/food-mood-app.git
   cd food-mood-app
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # OR
   source venv/bin/activate  # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to: `http://localhost:5000`

## Usage
1. Sign up or login to your account
2. Select your city from the dropdown
3. Choose your current mood
4. Click "Find Food Places" to get personalized restaurant recommendations
5. Browse through the results with ratings, prices, and locations

## API Integration
This app uses the Foursquare Places API to fetch real restaurant data based on location and food preferences.

## Screenshots
- Login/Signup page with mood-based theme
- <img width="1921" height="889" alt="FOOD MOOD LOGIN" src="https://github.com/user-attachments/assets/da89ea45-8438-4cfe-86bb-3711d3ff29de" />
<img width="1921" height="898" alt="FOOD MOOD SIGN UP" src="https://github.com/user-attachments/assets/a5dcc09f-d371-4d34-b2e8-f6b35821ebd6" />
<img width="1920" height="909" alt="FOOD MOOD WELCOME" src="https://github.com/user-attachments/assets/cf94a7bc-082b-486e-8db1-1b81b7182077" />

- City and mood selection interface
- <img width="1921" height="909" alt="FOOD MOOD LIST OF CITIES" src="https://github.com/user-attachments/assets/584d3a2d-d24a-4bd4-b2f1-c95fd0d7cf8a" />

- Restaurant results with ratings and pricing
<img width="1921" height="892" alt="FOOD MOOD RESULTS" src="https://github.com/user-attachments/assets/c2d0bacc-1cee-4d62-bfa2-b3c4aab5625e" />

## Contributing
Pull requests are welcome! Please feel free to contribute to this project.

## License
This project is open source and available under the MIT License.
