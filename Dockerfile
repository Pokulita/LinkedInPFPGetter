FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    wget curl unzip xvfb libxi6 libgconf-2-4 libdbus-glib-1-2 \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y firefox-esr

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz" && \
    tar -xzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/bin/ && \
    rm geckodriver-v0.30.0-linux64.tar.gz

ENV FIREFOX_BIN="/usr/bin/firefox"
ENV GECKODRIVER_BIN="/usr/bin/geckodriver"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "getter_script.py"]
