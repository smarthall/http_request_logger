FROM python:3

COPY reflect.py /

EXPOSE 80
CMD ["python", "-u", "/reflect.py"]
