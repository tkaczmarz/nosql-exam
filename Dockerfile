FROM mongo:latest
RUN apt update && \
	apt install -y \
		git \
		vim \
		python3 \
		python3-pip
RUN mv /usr/bin/python3 /usr/bin/python && mv /usr/bin/pip3 /usr/bin/pip
RUN pip install flask \
	matplotlib \
	pymongo
RUN useradd -ms /bin/bash admin
USER admin