<h1>Introduction: </h1>

Introducing TextUtils, a dynamic web application crafted on the Django framework that empowers users to effortlessly manipulate and enhance their text content. This versatile tool offers a range of essential text processing functions, including the removal of punctuations for cleaner prose, uppercase conversion for impactful messaging, new line removal, space removal for concise formatting, and a character count feature to keep tabs on textual length. TextUtils is deployed on AWS seamlessly, utilizing both manual and automated methods through Docker, ensuring a robust and efficient deployment process. 

<h1>Manually Deployment:</h1>

<h2>Step 1: Cloning the Project</h2>

Clone the project repository to get started. 

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.001.png)

<h2>Step 2: Installing Django</h2>

Install Django to environment to proceed with the setup. 

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.002.png)

<h2>Step 3: Migrating pkgs</h2>

Migrate packages for Django to finalize the configuration with following command:

		`python3 manage.py migrate`


![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.003.png)

<h2>Step 4: Running the Server</h2>

Launch the server with the following command:  

`python3 manage.py runserver 0.0.0.0:8001`

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.004.png)

<h2>Step 5: Adding Security Rules </h2>

In the Adding security rule menu of ec2 instance, a security rule is introduced by adding port in inbound rule menu. 

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.005.jpeg)

<h2>Step 6: Resolving Error </h2>

To resolve a disallowed host error, I permitted all hosts by setting `ALLOWED_HOSTS = ["*"]` in the Django project's settings. This configuration allows the application to accept requests from any host.

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.006.png)

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.007.png)

After this Application is now running   

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.008.jpeg)

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.009.png)

<h1>Automatically Deployment (By using Dockers):</h1>

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.010.png)

<h2>Step 1: Installing Docker </h2>

Successfully installed Docker using the command: 

`sudo apt install docker.io`. 

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.011.png)

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.012.png)

<h2>Step 2: Creatinng Docker File: </h2>

The Dockerfile has been created, as shown below in snapshot. 

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.013.png)

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.014.png)

<h2>Step 3: Building Docker file </h2>

Docker file is built by following command as shown below: 

`sudo docker build . -t textu  ls`

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.015.png)

<h2>Step 4: Running by using Docker </h2>

Docker file is run by following command as shown below: 

`sudo docker run -p 8001:8001 f4a25014498`

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.016.png)

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.017.jpeg)

For Running in background, you can use following code: 

`sudo docker run -d -p 8001:8001 f4a25014498`

![](./pics/Aspose.Words.a18c0a1f-eb93-436e-a56a-beca753b3aaf.018.png)
