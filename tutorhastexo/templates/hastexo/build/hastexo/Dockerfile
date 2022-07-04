FROM python:3.8
ENV PYTHONUNBUFFERED 1
ARG HASTEXO_XBLOCK_GIT_REPOSITORY=https://github.com/hastexo/hastexo-xblock.git
ARG HASTEXO_XBLOCK_VERSION={{ HASTEXO_XBLOCK_VERSION }}
RUN git clone $HASTEXO_XBLOCK_GIT_REPOSITORY -b $HASTEXO_XBLOCK_VERSION ./hastexo-xblock
WORKDIR ./hastexo-xblock
RUN pip install --upgrade pip && \
    pip install -r requirements/base.txt --exists-action w

RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/supervisor /var/log/supervisor /var/daphne
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8095
CMD ["/usr/bin/supervisord"]
