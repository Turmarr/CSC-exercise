FROM python:3.12 as python

RUN pip install fastapi httpx "uvicorn[standard]" pydantic-settings

WORKDIR /app

ENV ID ""

ENV SECRET ""

COPY . /app

EXPOSE 8000:8000

CMD ["uvicorn", "src.main:app", "--reload"]