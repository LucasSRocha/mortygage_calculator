FROM python:3.10

ENV PYTHONWARNINGS ignore
ENV PYTHONUNBUFFERED 1


COPY Makefile pyproject.toml poetry.lock ./
RUN make _base_pip && poetry config virtualenvs.create false && make dependencies 

WORKDIR /webapps

COPY . /webapps/

EXPOSE 8000

CMD ["./run_web.sh"]