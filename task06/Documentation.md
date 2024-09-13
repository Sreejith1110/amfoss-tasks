# Documentation for Flutter Ecommerce App
## Overview
Ihis is a sample or template project. This project is developed using Flutter so it can be used as a reference when building a flutter application. It can be the most helping when developing a online shopping apps .

## Functionality

## Models
#### category.dart
It is a code that is used to categories objects on id and name of the category ,link to an image in a category and if a category is selected. it uses category() to create and manage categories in the app.
#### data.dart
It is a code that stores information and data for the app like product information, categories, list of products in the cart and path to images used for preview.
#### product.dart
It is a code that creates specific details for the products such as id ,name,category,image,price,whether liked by the user and if it is selected.

### Product management features

#### Product Sorting
You can sort the product into categories using  ``Widget _categoryWidget()``  function . In the function, AppData.categoryList is used to get a list of categories and map() to convert each category into an product icon.
#### Search Functionality
You can search for items in the seach bar which is created using ``Widget _search()`` function. In the function, TextField() allows user to type in the search bar and _icon() is used to add a filter icon .
#### Product Listing
You can display a list of products using ``Widget _productWidget()`` function . In the function, GridView() is used to display the product in a grid ,map() is used to convert each product into a ProductCard widget, childAspectRatio:4/3 to set the shape of the productcard and crossAxisCount:1 shows onr product at a time.
#### Product Details
You can display product details in a new page using `` productDetailPage `` class in the product_detail.dart. In the class, Widget _appBar() function provides navigation button like back button and favourite button at the top of the application.widget _icon() ,widget _productImage(),Widget _categoryWidget(),Widget _thumbnail(),Widget _detailWidget(),Widget _availableSize(),Widget _sizeWidget(),etc functions are used to style and build the layout of the product detail page.

### Cart management features

#### Cart Item Display
You can build a list of cart items using ``Widget _cartItems()`` function. In this function, AppData.cartList function contains the items in the cart and _item() convert the items in the cart into a widget and store in a column using column().
#### Price calculation
You use ``Widget _price()`` function to view the items and its price and ``getPrice()`` function is used to calculate the total price by looping through each product multiplying with its quantity and returns the total price to the user.
#### Confirmation button
To confirm your purchase uses ``Widget _submitButton(BuildContext context)`` function. It creates a next button to proceed to the next step. In this function, TextButton and TitleText is used to make the conformation button.


### main.dart
It is used to organize and connect multiple components of the application . It structures and beautify the application along with integrating multiple parts of the application using import and widgets and classes.
