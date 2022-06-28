FROM tiangolo/uvicorn-gunicorn:python3.8
LABEL maintainer="luoqian@rongshantech.com"

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN sed -i "s/deb.debian.org/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list
RUN sed -i "s/security.debian.org/mirrors.bfsu.edu.cn/g" /etc/apt/sources.list
RUN apt update  && apt install -y redis-server vim && mkdir -p /opt
COPY . /app
ENV ENV prd
COPY requirement.txt /tmp/requirements.txt
ADD endpoint.sh /opt
WORKDIR /app
RUN chmod 777 /opt/endpoint.sh

RUN pip install --no-cache-dir -r /tmp/requirements.txt -i http://mirrors.cloud.aliyuncs.com/pypi/simple/ --trusted-host mirrors.cloud.aliyuncs.com
RUN ls -alh

EXPOSE 8000

CMD ["/bin/sh", "-c", "/opt/endpoint.sh"]
