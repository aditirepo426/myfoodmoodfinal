from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Foursquare API configuration
FOURSQUARE_API_KEY = 'DF0NBSQXQ142JIEYVGPCP05ESHEMVVYO5ZVNPQDWWQQPABYB'
FOURSQUARE_BASE_URL = 'https://places-api.foursquare.com/places/search'

# Cities list
CITIES = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
    'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
    'Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Nashik'
]

# Moods configuration
MOODS = {
    'happy': {
        'label': 'Happy 😊',
        'keywords': ['dessert', 'ice cream', 'cafe', 'bakery']
    },
    'sad': {
        'label': 'Sad 😢',
        'keywords': ['comfort food', 'pizza', 'burger', 'chocolate']
    },
    'relaxed': {
        'label': 'Relaxed 😌',
        'keywords': ['tea', 'coffee', 'spa cuisine', 'healthy']
    },
    'angry': {
        'label': 'Angry 😠',
        'keywords': ['spicy', 'hot wings', 'barbecue', 'grill']
    },
    'frustrated': {
        'label': 'Frustrated 😤',
        'keywords': ['fast food', 'takeout', 'delivery', 'quick']
    }
}

# Mock restaurant data for fallback
MOCK_RESTAURANTS = {
    'happy': [
        {'name': 'Sweet Dreams Bakery', 'category': 'Bakery', 'rating': 4.5, 'price': 2, 'address': '123 Main St'},
        {'name': 'Sunny Side Café', 'category': 'Café', 'rating': 4.3, 'price': 2, 'address': '456 Oak Ave'},
        {'name': 'Rainbow Ice Cream', 'category': 'Dessert', 'rating': 4.7, 'price': 1, 'address': '789 Pine Rd'},
        {'name': 'Joy\'s Cupcakes', 'category': 'Bakery', 'rating': 4.4, 'price': 2, 'address': '321 Happy St'}
    ],
    'sad': [
        {'name': 'Comfort Kitchen', 'category': 'Comfort Food', 'rating': 4.4, 'price': 2, 'address': '321 Elm St'},
        {'name': 'Mama\'s Pizza Palace', 'category': 'Pizza', 'rating': 4.2, 'price': 2, 'address': '654 Maple Dr'},
        {'name': 'Cozy Burger Joint', 'category': 'Burger', 'rating': 4.1, 'price': 2, 'address': '987 Cedar Ln'},
        {'name': 'Soul Food Diner', 'category': 'Comfort Food', 'rating': 4.3, 'price': 2, 'address': '159 Comfort Ave'}
    ],
    'relaxed': [
        {'name': 'Zen Tea House', 'category': 'Tea House', 'rating': 4.6, 'price': 2, 'address': '147 Bamboo St'},
        {'name': 'Peaceful Greens', 'category': 'Healthy', 'rating': 4.4, 'price': 3, 'address': '258 Lotus Ave'},
        {'name': 'Tranquil Coffee', 'category': 'Coffee Shop', 'rating': 4.3, 'price': 2, 'address': '369 Sage Rd'},
        {'name': 'Mindful Meals', 'category': 'Healthy', 'rating': 4.5, 'price': 3, 'address': '741 Calm St'}
    ],
    'angry': [
        {'name': 'Fire Wings Grill', 'category': 'Wings', 'rating': 4.2, 'price': 2, 'address': '741 Spice St'},
        {'name': 'Dragon\'s Breath BBQ', 'category': 'Barbecue', 'rating': 4.5, 'price': 3, 'address': '852 Heat Ave'},
        {'name': 'Inferno Grill', 'category': 'Grill', 'rating': 4.1, 'price': 3, 'address': '963 Flame Rd'},
        {'name': 'Blazing Hot Pot', 'category': 'Spicy', 'rating': 4.3, 'price': 3, 'address': '147 Fire Ln'}
    ],
    'frustrated': [
        {'name': 'Quick Bites Express', 'category': 'Fast Food', 'rating': 3.9, 'price': 1, 'address': '159 Rush St'},
        {'name': 'Speedy Delivery', 'category': 'Takeout', 'rating': 4.0, 'price': 1, 'address': '357 Fast Ave'},
        {'name': 'Instant Eats', 'category': 'Quick Service', 'rating': 3.8, 'price': 1, 'address': '468 Swift Rd'},
        {'name': 'Flash Food', 'category': 'Fast Food', 'rating': 3.7, 'price': 1, 'address': '258 Quick St'}
    ]
}

def get_restaurants_from_foursquare(city, mood):
    """Get restaurants from Foursquare API"""
    try:
        mood_config = MOODS.get(mood, {})
        query = mood_config.get('keywords', ['restaurant'])[0]
        
        headers = {
            'accept': 'application/json',
            'X-Places-Api-Version': '2025-06-17',
            'authorization': f'Bearer {FOURSQUARE_API_KEY}'
        }
        
        params = {
            'query': query,
            'near': city,
            'limit': 10
        }
        
        response = requests.get(FOURSQUARE_BASE_URL, headers=headers, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            restaurants = []
            
            for place in data.get('results', []):
                restaurant = {
                    'name': place.get('name', 'Unknown'),
                    'category': place.get('categories', [{}])[0].get('name', 'Restaurant') if place.get('categories') else 'Restaurant',
                    'rating': round(place.get('rating', 4.0) / 2, 1) if place.get('rating') else 4.0,  # Convert 10-scale to 5-scale
                    'price': place.get('price', 2),
                    'address': place.get('location', {}).get('formatted_address', f'{city}')
                }
                restaurants.append(restaurant)
            
            return restaurants
        else:
            print(f"Foursquare API error: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except Exception as e:
        print(f"Error fetching from Foursquare: {e}")
        return None

def get_mock_restaurants(city, mood):
    """Get mock restaurant data"""
    restaurants = MOCK_RESTAURANTS.get(mood, [])
    # Add city to address for mock data
    for restaurant in restaurants:
        restaurant['address'] = f"{restaurant['address']}, {city}"
    return restaurants

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'login':
            email = request.form.get('email')
            password = request.form.get('password')
            
            if email and password:
                # Simple login validation (in real app, check against database)
                session['user'] = {
                    'name': email.split('@')[0],
                    'email': email
                }
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error='Please fill in all fields')
                
        elif action == 'signup':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            
            if name and email and password:
                # Simple signup (in real app, save to database)
                session['user'] = {
                    'name': name,
                    'email': email
                }
                return redirect(url_for('home'))
            else:
                return render_template('login.html', error='Please fill in all fields')
    
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('home.html', 
                         user=session['user'], 
                         cities=CITIES, 
                         moods=MOODS)

@app.route('/search', methods=['POST'])
def search():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    city = request.form.get('city')
    mood = request.form.get('mood')
    
    if not city or not mood:
        return redirect(url_for('home'))
    
    # Try to get restaurants from Foursquare API
    restaurants = get_restaurants_from_foursquare(city, mood)
    
    # If API fails, use mock data
    if not restaurants:
        print("Using mock data as fallback")
        restaurants = get_mock_restaurants(city, mood)
    
    return render_template('results.html', 
                         restaurants=restaurants,
                         city=city,
                         mood=mood,
                         mood_label=MOODS[mood]['label'],
                         user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(error):
    return render_template('login.html', error='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('login.html', error='Internal server error'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)