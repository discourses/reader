# Dockerfile

# A python runtime base image
FROM python:3.6-buster

# pip
RUN pip install --upgrade pip

# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app
RUN mkdir /app/data
COPY requirements.txt /app
RUN pip install --requirement /app/requirements.txt

# Specific COPY
COPY src /app/src
COPY config.py /app/config.py

# Port
EXPOSE 8050

# Create mountpoint
VOLUME /app/data

# ENTRYPOINT
ENTRYPOINT ["python"]

# CMD
CMD ["src/main.py"]
