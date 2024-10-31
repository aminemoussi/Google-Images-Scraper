# Interactive Google Images Scraper

A Python web scraping program that downloads images from Google Images search results with user-controlled scrolling and customizable download settings. Built using Selenium WebDriver and BeautifulSoup4.

## 🌟 Features

- Interactive scrolling control
- Customizable number of images to download
- Configurable image loading timeout
- Custom save location and file naming
- Automatic thumbnail detection and full-size image retrieval
- Progress tracking and timing statistics
- Error handling and retry mechanisms

## 📋 Prerequisites

- Python 3.x
- Chrome WebDriver
- Required Python packages:
  ```bash
  selenium
  beautifulsoup4
  requests
  ```

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aminemoussi/Google-Images-Scraper.git
   ```

2. Install dependencies:
   ```bash
   pip install selenium beautifulsoup4 requests
   ```

3. Download and setup ChromeDriver:
   - Download from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) or [ChromeDriver Downloads](https://www.chromedriverdownload.com/en/downloads/chromedriver-130-download#google_vignette)
   -  Note that it is absolutely crucial to pick the right Chrome Driver Version that is COMPATIBLE with your version of Chrome (I have included the Chrome Driver version 130 which is compatible with Chrome version 130)
   - Run the `chromedriver.exe` file and Update: 
      -`chrome_driver_path`
      -`url` path if you wish to scrape another page.

## 🎯 Usage

1. Run the script:
   ```python
   python main.py
   ```

2. Follow the interactive prompts:
   - Scroll the page to load as many images as you wish
   - Enter the number of images you want to download
   - Set maximum wait time for image loading
   - Specify save location and file naming

## 💻 Interactive Steps

1. **Page Scrolling**:
   ```
   "Scroll down if you want to generate more images, press enter when you are done... "
   ```

2. **Image Selection**:
   ```
   "Number of images generated in the page: [X]"
   "How much you want: "
   ```

3. **Configuration**:
   ```
   "Enter the max time to wait for an image to load: "
   "Where to save it (folder path): "
   "What to name it (file name): "
   ```

## 🔄 Process Flow

1. Opens Google Images search
2. Allows manual scrolling for image loading
3. Counts available images
4. Takes user input for download parameters
5. Downloads images with progress tracking
6. Provides completion summary with timing

## ⚙️ Key Functions

### Main Components:
- Selenium WebDriver setup
- BeautifulSoup parsing
- Interactive user input handling
- Image downloading system
- Progress tracking
- Error handling

## 🚫 Error Handling

The script handles various errors:
- Invalid image counts
- Loading timeouts
- Download failures
- Thumbnail conversion issues

## ⚠️ Limitations

- Requires manual scrolling
- Subject to Google's rate limiting
- Depends on stable internet connection
- May need updates for Google UI changes in the Future

## 📝 Notes

- Images are downloaded sequentially
- Every 25th container is typically skipped (related searches)
- Progress is displayed in real-time
- Final summary shows total downloads and time elapsed

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
