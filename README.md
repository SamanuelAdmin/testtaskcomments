<h1>Test task from dZENcode company</h1>

Task (junior):
[Python_removed.pdf](https://github.com/user-attachments/files/17494590/Python_removed.pdf)

User documentation (ukr.):

https://github.com/user-attachments/assets/8b5d8897-b2cc-42fd-b9c6-26eb03eb7f75



<div>
  <h2>How to start a server (<strong>using docker</strong>)</h2>

  <ol>
    <li>Download and install <a href="https://www.docker.com/">docker</a></li>
    <li><a href="https://drive.google.com/file/d/1yRHdZGhnbpGEvpOcAQZYuaKPd6Sw1wBO/view?usp=sharing">Download docker image of this project</a></li>
    <li>
      Load an object using <br><code>docker load -i [image name]</code>
    </li> 
    <li>Check, if image has been loaded successfully by <br><code>docker images</code></li>
    <li>Run a container using <br><code>docker run -p 8000:8000 testtask</code></li>
  </ol>

  <i>And now your server is on <code>localhost:8000</code></i>
</div>

<strong>DEFAULT ADMIN CREDENTIALS <code>admin : admin</code></strong>

<br>Small video about final product: <a href="https://www.youtube.com/watch?v=w2r8siSsj40">https://www.youtube.com/watch?v=w2r8siSsj40</a>

<br><br>
Docker file:
```
FROM python:3.12
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
VOLUME ["/app/media"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
