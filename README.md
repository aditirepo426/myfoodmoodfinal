# 🍽️ Food Mood App

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
- City and mood selection interface
- Restaurant results with ratings and pricing

## Contributing
Pull requests are welcome! Please feel free to contribute to this project.

## License
This project is open source and available under the MIT License.