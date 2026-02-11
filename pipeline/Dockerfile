FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

# RUN pip install pandas pyarrow

WORKDIR /code
#Alternative to using WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"
 
COPY pyproject.toml .python-version uv.lock ./





#Ensure that the same dependecies are installed from uv.lock and virtual environment
RUN uv sync --locked 

COPY pipeline.py .

# ENTRYPOINT ["uv", "run", "python", "pipeline.py" ]
# When using ENV PATH above, you dont need "uv". See below
ENTRYPOINT ["python", "pipeline.py" ]