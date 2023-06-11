# Kivy App with MySQL Database Integration

This code represents a Kivy application that integrates with a MySQL database. It provides a graphical user interface (GUI) for managing customer records. The app allows users to submit customer names to the database, retrieve and display customer records, and perform other related tasks.

## Dependencies

To run this application, you need to have the following dependencies installed:

* Kivy: A Python framework for developing multi-touch applications.
* mysql-connector-python: A Python driver for connecting to MySQL databases.

You can install these dependencies using pip:

`pip install kivy mysql-connector-python`


## Application Structure

The application is organized into several classes, each representing a different screen or component of the app. Here's an overview of the main classes:

* `MainWindow`: Represents the main screen of the application.
* `DonatorLogin`: Represents the screen for donor login functionality.
* `ReceiverLogin`: Represents the screen for receiver login functionality.
* `ReceiverSearch`: Represents the screen for searching receivers.
* `DonatorMainScreen`: Represents the main screen for donors.
* `SellOrder`: Represents the screen for placing sell orders.
* `TotalDonations`: Represents the screen for displaying total donations.
* `TaxExempt`: Represents the screen for handling tax exemptions.
* `ImageButton`: A custom widget that combines a button behavior with an image.
* `WindowManager`: Manages the transitions between screens.
* `MyGrid`: A custom widget representing a grid layout.
* `myWidget`: A custom widget used in the app.
* `MyApp`: The main application class.

## MySQL Database Integration

The application integrates with a MySQL database to store customer records. The database connection is established in the `build` method of the `MyApp` class. It connects to a local MySQL server using the provided credentials and selects the appropriate database.

The `submit` method is responsible for inserting customer names into the database. It retrieves the customer name from the GUI input field, constructs an SQL command with the name as a parameter, and executes the command using the MySQL cursor. After the insertion, it clears the input field.

The `show_records` method retrieves all customer records from the database and displays them in a label on the GUI. It fetches the records using an SQL query and iterates over them to construct a string representation. Finally, it sets the label's text to the constructed string.

## GUI Design

The GUI is defined in a separate Kivy language file named `my.kv`, which is loaded using `Builder.load_file()` in the `build` method of the `MyApp` class. The layout and design of the screens are defined in this file using a declarative syntax.

The GUI includes various screens for different functionalities, such as donor login, receiver login, search, sell orders, total donations, and tax exemptions. It also includes buttons, labels, and input fields for user interaction.

## Running the Application

To run the application, execute the Python script containing the code. It will launch the Kivy app and display the main window with the integrated GUI. You can interact with the app by clicking buttons, entering data into input fields, and observing the displayed information.

Note that to connect to the MySQL database successfully, you need to ensure that the MySQL server is running and that the provided database credentials are correct.

## Additional Notes

* The application code assumes that you have a local MySQL server set up and accessible with the provided credentials. If you have a different setup, make sure to modify the code accordingly.
* The code provided here does not include error handling or robust input validation. In a production environment, it is essential to implement appropriate error handling to handle potential exceptions and ensure data integrity.

Feel free to explore the code, modify it, and adapt it to your specific requirements.
