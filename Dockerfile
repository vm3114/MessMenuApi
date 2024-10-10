FROM python:3.10

# Install necessary packages
RUN apt-get update && apt-get install -y \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget vim xvfb libgbm1 libu2f-udev libvulkan1 && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/bin && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Install Google Chrome
RUN CHROME_SETUP=google-chrome.deb && \
    wget -q -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP || apt-get install -y -f && \
    rm $CHROME_SETUP

# Set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PATH="$PATH:/bin:/usr/bin"

WORKDIR /app

# Copy the application code and requirements file
COPY . /app

# Install Python dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
