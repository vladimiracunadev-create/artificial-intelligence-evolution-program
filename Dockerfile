FROM python:3.12-slim
WORKDIR /app
COPY site/ /app/site/
COPY classes/ /app/classes/
USER 65532:65532
EXPOSE 8080
CMD ["python", "-m", "http.server", "8080", "--directory", "/app", "--bind", "0.0.0.0"]
