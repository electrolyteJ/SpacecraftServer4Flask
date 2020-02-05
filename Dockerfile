FROM python:3.7.3

WORKDIR /SpacecraftServer4Flask

# Copy src files
#COPY . .
ADD . /app

# Install deps
RUN   pip3 install pipenv && pipenv install
#RUN pip3 install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# Expose port 5000
EXPOSE 9000

# Start the server
ENTRYPOINT [ "bash", "bootstrap"]