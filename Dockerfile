FROM python:3.12 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip3 install --user -r requirements.txt

# second stage
FROM python:3.12-slim
WORKDIR /code

# copy only the dependencies that are needed for our application and the source files
COPY --from=builder /root/.local /root/.local
COPY ./source .

# update PATH
ENV PATH=/root/.local:$PATH

# make sure you include the -u flag to have our stdout logged
# CMD [ "python", "-u", "./main.py" ]
EXPOSE 8080
# CMD [ "bash", "./run.sh" ]
CMD [ "python", "app.py" ]
