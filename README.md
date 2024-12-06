# EmailSniffer

**GmailFinder** is a Python tool that allows you to easily extract Gmail addresses from any public website. This tool can be used for web scraping, email research, or data gathering. With a simple and user-friendly interface built using Tkinter, GmailFinder makes it easy to find Gmail addresses from web pages.

---

## Features

- **Fast Gmail Address Extraction**: Automatically find Gmail addresses embedded in the content of a webpage.
- **User-Friendly GUI**: Built with Tkinter, providing a simple and clean graphical user interface.
- **Clipboard Support**: Copy extracted Gmail addresses directly to your clipboard for easy use.
- **Paste from Clipboard**: Allows users to easily paste URLs directly from the clipboard.
- **Cross-Platform**: Works on Windows, macOS, and Linux systems.
- **Lightweight and Easy to Use**: No need to deal with complex scraping setups—just paste a URL and get the results.

---

## How It Works

1. **Enter URL**: Paste the website URL you want to scan for Gmail addresses.
2. **Find Emails**: Click the **Find Gmail Addresses** button to search the webpage.
3. **Copy to Clipboard**: Copy the extracted Gmail addresses to your clipboard with a single click.

---

## Installation

### Prerequisites

Before running **GmailFinder**, you need to have Python 3.x installed on your computer.

### Steps

1. **Clone the repository**:
   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/sourabhdasp/EmailSniffer.git
   ```

2. **Install dependencies**:
   Navigate to the project directory and install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary Python libraries:
   - `requests` - For sending HTTP requests.
   - `beautifulsoup4` - For parsing HTML content.
   - `pyperclip` - For copying text to the clipboard.
   - `tkinter` - For building the graphical user interface.

3. **Run the application**:
   After installing the dependencies, you can run the application with:
   ```bash
   python EmailSniffer.py
   ```

---

## Usage

1. Open the **GmailFinder** application.
2. In the **Enter Website URL** field, paste the URL of the webpage you want to scrape for Gmail addresses.
3. Click the **Find Gmail Addresses** button to start the extraction process.
4. The Gmail addresses found will be displayed in the result area. You can click **Copy to Clipboard** to easily copy the results.

### Example

- **URL Input**: https://example.com
- **Output**:
  ```
  john.doe@gmail.com
  jane.smith@gmail.com
  ```

---

## Contributing

We welcome contributions to improve and expand the functionality of GmailFinder. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and test them.
4. Submit a pull request with a description of your changes.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- **BeautifulSoup**: Used for HTML parsing to extract Gmail addresses from web pages.
- **Requests**: Used to fetch the webpage content.
- **Tkinter**: Used for creating the GUI interface.
- **Pyperclip**: Used for clipboard functionality to copy extracted Gmail addresses.

---

## Keywords

`Gmail extractor`, `email scraper`, `web scraping`, `Python tool`, `Tkinter GUI`, `email collection`, `GmailFinder`

---

### Why This README Works:
1. **Clear Overview**: It immediately explains what the project does and its main features.
2. **Simple Setup Instructions**: Easy-to-follow installation instructions, so users can quickly get started.
3. **Practical Example**: Provides a basic usage example to help users understand the process.
4. **Contribution Guidelines**: Encourages contributions and explains how others can help improve the project.
5. **Attractive License and Acknowledgements**: Mentioning the MIT License and acknowledging the libraries used shows professionalism.

This README will help users understand how to use the project and contribute to it, while also providing clear installation and usage instructions.
