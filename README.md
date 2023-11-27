# Twitter URL Composer

Twitter URL Composer is a web application that allows users to create action URLs for Twitter, such as following a user, sending direct messages, or tweeting pre-populated text.

![Twitter URL Composer](https://dhfzdqrudbfdfjgjlcjt.supabase.co/storage/v1/object/public/cdn/Screenshot%202023-11-25%20at%201.59.01%20AM.png)

## Features

- **Create Twitter Action URLs**: Generate URLs for various Twitter actions quickly.
- **Copy to Clipboard**: Easily copy the generated URLs to the clipboard with a click.
- **Loading Animation**: Enjoy a smooth experience with visual feedback while the app fetches data.
- **Responsive Design**: Use the app comfortably on any device, with a layout that adjusts to your screen size.

## How to Use

Visit the web app, choose an action from the dropdown menu, input the required information, and hit submit. The app will generate a Twitter URL for you to use.

## Installation

To set up the Twitter URL Composer locally, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/c9obvi/twitter-url-composer.git
    ```
2. Navigate to the project directory:
    ```
    cd twitter-url-composer
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the Flask app:
    ```
    flask run
    ```
  > [!TIP]
   If you run into jinja2 / flask issues: 
   ```
   pip install --upgrade flask jinja2
   ```

## Contributing

Contributions to the Twitter URL Composer are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
