 FROM python:3.6.8
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /app
 WORKDIR /app
 COPY requirements.txt /app/
 RUN pip install -r requirements.txt
 RUN groupadd -g 999 appuser && \
     useradd -r -u 999 -g appuser appuser
 RUN chown appuser /app
 USER appuser