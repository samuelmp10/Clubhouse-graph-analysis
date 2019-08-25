FROM alpine:3.7


RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN apk add --no-cache curl

RUN apk add --update nodejs nodejs-npm


RUN npm install http-server -g

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev


COPY requirements.txt /usr/src/app/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
RUN pip install numpy==1.14.5

COPY api-get.sh /usr/src/app/
COPY obtencion.py /usr/src/app/
COPY nx.py /usr/src/app/
COPY run.sh /usr/src/app/
COPY ./web/clubhouse.html /usr/src/app/web/
COPY ./web/clubhouse_comm.html /usr/src/app/web/
#RUN mkdir /usr/src/app/images/
ADD ./images/ /usr/src/app/
COPY ./images/test.txt /usr/src/app/images/
CMD sh /usr/src/app/run.sh $APITOKEN
