# Fancy Restaurant Menu

A modern, responsive web application to manage a restaurant menu, allowing users to **add**, **edit**, and **delete** food items. Built with **Flask**, **MongoDB**, and **Bootstrap**, featuring a sleek and animated UI.

## Demo

The application is live at: [https://muppidivenkatabalaji-22bcb7289-1.onrender.com](https://muppidivenkatabalaji-22bcb7289-1.onrender.com)

---

## Features

* Add new food items with **name**, **price**, **category**, and **type** (Veg/Non-Veg).
* Edit existing food items.
* Delete food items.
* Responsive and animated UI using **Bootstrap** and **Animate.css**.
* Real-time MongoDB database integration.

---

## Technologies Used

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS, Bootstrap, Animate.css, Font Awesome
* **Database**: MongoDB (Atlas)
* **Deployment**: Render

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/fancy-restaurant-menu.git
cd fancy-restaurant-menu
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup MongoDB**

* Use MongoDB Atlas or local MongoDB.
* Replace the MongoDB connection string in `app.py`:

```python
client = MongoClient("YOUR_MONGODB_CONNECTION_STRING")
```

5. **Run the application**

```bash
python app.py
```

* Visit `http://127.0.0.1:5000` in your browser.

---

## Usage

* Click **Add New Dish** to add a food item.
* Use **Edit** to update details.
* Use **Delete** to remove a dish.
* The home page displays all items dynamically from the MongoDB database.

---

## Project Structure

```
Fancy-Restaurant-Menu/
│
├── templates/
│   ├── index.html      # Home page displaying all food items
│   ├── add.html        # Form to add a new food item
│   └── edit.html       # Form to edit an existing food item
│
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.
