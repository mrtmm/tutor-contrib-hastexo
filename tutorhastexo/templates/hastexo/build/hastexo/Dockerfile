FROM python:3.8
ENV PYTHONUNBUFFERED 1
ARG HASTEXO_XBLOCK_GIT_REPOSITORY=https://github.com/hastexo/hastexo-xblock.git
ARG HASTEXO_XBLOCK_VERSION={{ HASTEXO_XBLOCK_VERSION }}
ARG HASTEXO_ASGI_APPLICATION={{ HASTEXO_ASGI_APPLICATION }}
RUN git clone $HASTEXO_XBLOCK_GIT_REPOSITORY -b $HASTEXO_XBLOCK_VERSION ./hastexo-xblock
WORKDIR ./hastexo-xblock
RUN pip install --upgrade pip && \
    pip install -r requirements/base.txt --exists-action w
EXPOSE 8095
CMD daphne -b 0.0.0.0 -p 8095 $HASTEXO_ASGI_APPLICATION
