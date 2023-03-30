FROM python:3.8.13

WORKDIR /spacecraftserver4flask

# Copy src files
COPY .. .
#ADD . /SpacecraftServer4Flask

# Install depsrequirements.txt
#RUN   pip3 install pipenv && pipenv install
#RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r requirements.txt

## package
#RUN pipenv install setuptools wheel --dev
#RUN python setup.py sdist bdist_wheel
#RUN pipenv install dist/chatbot_server-1.0.0-py3-none-any.whl --force-reinstall

# Expose port 5000
EXPOSE 9000

# Start the server
ENTRYPOINT ["python", "-m","app"]
#CMD ["gunicorn","-c","gunicorn.conf.py","app:main"]