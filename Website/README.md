# WEBSITE SHELLFISH PROJECT

This directory contains information regarding our central website for this REU project deep learning image processing with oyster farms. This Website was built by using the ReactJS application 
in order to combine the backends necessary to post information on both forms to their respective locations (Google Storage and MySQL).

In order to implement the code, there are a few pre-requisite packages and applications to download before running/changing the website.

## Packages
First, I have the packages on GitHub, but more than likely you'll need to download them on your own. Create a package by entering `npm init --y` into the terminal, and select your preferred license and name. Personally, I chose the MIT license.

Next, we need to install packages such as express, mysql2, cors, Axios, nodemon,  in Javascript. They will handle the file transfer, input into MySQL, handle the backend API, and make changes easier respectively. 
To do this, enter `npm install express mysql2 cors nodemon axios`

To access the Google storage, input the packages for Google Cloud and multer with `npm i multer` and `npm i @google-could/storage` in the terminal. 

Within the package, go into the `"scripts"` section and input `"start" : "nodemon index.js"` to start running the backend js page.

start the backend server file, `index.js` in this case, (NOT WITHIN THE REACTJS DIR) by running the command `npm run dev` in the terminal

To start the react app, input `npx create-react-app (DIR_NAME)` in the terminal. Once you do that, make sure the files are in the right spots and you'll be set to run the website!

*Note: The ReactJS responds directly to the App.js file, the index files created within the creat don't serve a purpose in this project
and the web_structure directory is used for organization. If you run into any errors, the 2 most likely solutions are making sure your ports line up
(the post for the forms should listen to the backend port, not the front end) and make sure you use syntax specific to ReactJS,
although it is a JAvaScrpit Application, syntax from either do not mix well together.*
