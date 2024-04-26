FROM python:3.8
ENV PYTHONUNBUFFERED 1
ARG HASTEXO_XBLOCK_GIT_REPOSITORY=https://github.com/hastexo/hastexo-xblock.git
ARG HASTEXO_XBLOCK_VERSION={{ HASTEXO_XBLOCK_VERSION }}
RUN git clone $HASTEXO_XBLOCK_GIT_REPOSITORY -b $HASTEXO_XBLOCK_VERSION ./hastexo-xblock
WORKDIR ./hastexo-xblock
RUN pip install --upgrade pip && \
    # install the XBlock in editable mode until we add support for the next Open edX release,
    # to avoid introducing a breaking change within the supported versions of this
    # plugin and the Hastexo XBlock for the Quince release.
    pip install -r requirements/base.txt --exists-action w -e .
EXPOSE 8095
CMD daphne -b 0.0.0.0 -p 8095 hastexo_guacamole_client.asgi:application
