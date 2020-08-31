# DocuSign-Project

## Demo Display
![Home Page](https://raw.githubusercontent.com/AVS1508/DocuSign-Project/master/assets/Home-Page.png?token=AEZHRVQZB2ZSWR6NM2VROVS7K2OMG)
<div style="display:flex">

</div>
<p align="center">
<a href="https://github.com/AVS1508/DocuSign-Project">
    <img src="https://raw.githubusercontent.com/AVS1508/DocuSign-Project/master/assets/Donation-Form.png?token=AEZHRVTNPXUG3CCOBBW5SNS7K2ORC" alt="Donation Form"/>
    <img src="https://raw.githubusercontent.com/AVS1508/DocuSign-Project/master/assets/Volunteer-Form.png?token=AEZHRVUNSCBXYGRNFWYS7SS7K2OTI" alt="Volunteering Application"/>
</a>
</p>


## About
This is a hackathon project developed as a submission for DocuSign Good Code Hackathon 2020. The project aims to provide an interactive web application for NGOs to manage their incoming donations and volunteering sign-ups.

## Inspiration behind EForm
We wanted to create a fully scalable, deployable web app for non-profit NGOs like Room to Read, Pratham, Tosan, and many more, that managed the electronic signing of the required forms, such as volunteering applications and donation submissions. We wanted to do this to make sure the people found out the required information regarding the forms and submit them electronically without going to the organization in-person in these uncertain times of COVID-19. This application was the means of making sure that the functioning of the NGOs did not get tangibly affected as well as ensuring that people did not put themselves at unnecessary risk.

## What this Project Does
It asks the user to choose from one of the forms that the NGOs have chosen to upload. The user is then required to fill it. The form then gets converted into a PDF file and is used to invoke the DocuSign eSignature API, where we chose to use an embedded signing process. The user is then redirected to the DocuSign embedded signing ceremony and then redirected back to our web app. 

## How We Built It
We built the overall platform using Flask for the back-end and API integration, along with Jinja2 templates created using a blend of HTML and inline Python. The styles were largely based on Bootstrap UI with minimal alterations.

## Challenges We Ran Into
Initially, we were unable to connect our app with the DocuSign API and it took two of us to figure out what to do. The challenges were exacerbated due to our relative unfamiliarity with Flask, but we marched forwards with full attention and efforts until we made it through!

## Accomplishments that We're Proud of
We are proud of making a useful project which will be of use to countless NGOs that are struggling with their IT infrastructures and desperately needed a source of hope. We are expecting this project to shape out beautifully for our clients and hope they see our spark too!

## What We Learned
We learned how to work together as a team and help complement each other. It was our first time using GitHub in a collaborative fashion and we also learned a significant amount about integrating APIs into our back-end. We were all familiar with Python frameworks through Django but Flask's relative simplicity for our purposes made it an ideal choice, therefore we ended up reading through vast documentation to learn about Flask on the go.

## What's Next for EForm
We intend to continue working on this and append additional functionality and features to our project. We also aim to pitch this project to the local NGOs and affiliate ourselves with them!

## LICENSE

MIT License

Copyright (c) 2020 Aaditya Yadav, Aditya Vikram Singh, Ikshita Yadav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.