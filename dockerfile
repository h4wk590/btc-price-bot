# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /src

# Copy the Python script and requirements file into the container
COPY bitcoin_discord_webhook.py .
COPY requirements.txt .
COPY .env .

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Install cron inside the container
RUN apt-get update && apt-get -y install cron

# Copy the cron job configuration to the container
COPY cronjob /etc/cron.d/bitcoin_cron

# Give execute permissions to the cron job
RUN chmod 0644 /etc/cron.d/bitcoin_cron

# Apply cron job
RUN crontab /etc/cron.d/bitcoin_cron

# Run cron in the foreground to keep the container alive
CMD ["cron", "-f"]

