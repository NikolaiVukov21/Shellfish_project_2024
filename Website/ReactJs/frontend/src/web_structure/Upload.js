import React, { useState } from 'react';
import axios from 'axios';
import '.././css/upload.css';


function Upload() {
    
    
    const container = document.getElementById('container');

    const [isSignUp, setSignUp] = useState(true);
    const signInButton = () => {
        setSignUp(true);
    }
    const uploadButton = () => {
        setSignUp(false);
    }
    
    //pulls values from the form code using function form Reactt called useState
    const [values, setValues] = useState({
        firstName: '',
        lastName: '',
        email: '',
        pwd: ''
    })
    // handleChange function
    const handleChange = (e) => {
        setValues({...values, [e.target.name]:[e.target.value]})
    }
    //onSubmit calls  handleSubmit function when the submit button is pressed
    const handleSubmit = (event) => {
        event.preventDefault();
        //calls the axios API
        axios.post('http://localhost:8083/postvalue', values)   
        .then(res => console.log("Registered Successfully!"))
        .catch(err => console.log(err));
    }
    //----------------------------------------------------------------------------------------------------------------------------------------
    function uuidv4() {
        return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
          (
            c ^
            (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
          ).toString(16)
        );
      }
      
      const actionSubmit = (e) => {
        let postid = uuidv4();
        let inputElem = document.getElementById("imgfile");
        let file = inputElem.files[0];
        // Create new file so we can rename the file
        let blob = file.slice(0, file.size, "image/jpeg");
        let newFile = new File([blob], `${postid}_post.jpeg`, { type: "image/jpeg" });
        // Build the form data - You can add other input values to this i.e descriptions, make sure img is appended last
        // Port listening to backend instead of frontend
        let formData = new FormData();
        formData.append("imgfile", newFile);
        fetch("http://localhost:8083/upload", {
          method: "POST",
          body: formData,
        })
          .then((res) => res.text())
          .then(loadPosts());
      };
      // Loads the posts on page load
      // make sure posts is listening to the backend, not the front end
      function loadPosts() {
        fetch("http://localhost:8083/upload")
          .then((res) => res.text())
          .then((x) => {
            for (let y = 0; y < x[0].length; y++) {
              console.log(x[0][y]);
              const newimg = document.createElement("img");
              newimg.setAttribute(
                "src",
                "https://storage.googleapis.com/test_bucket_abc123/" + x[0][y].id
              );
              newimg.setAttribute("width", 50);
              newimg.setAttribute("height", 50);
              document.getElementById("images").appendChild(newimg);
            }
          });
      }

    return (
        <div name="Uploads" className="upload-section">
            <p class="upload-title">Upload Image for Annotation</p>
        <div className={`container ${isSignUp ? "right-panel-active" : ""}`} id="container">
            <div className="form-container signIn">
                <form onSubmit={handleSubmit}>
                    <h1>Create Account</h1>
                    <label className="font-head" htmlFor="firstName">First name:</label><br/>
                    <input className="text-box" type="text" id="firstName" name="firstName" onChange={handleChange}/><br/>
                    <label className="font-head" htmlFor="lName">Last name:</label><br/>
                    <input className="text-box" type="text" id="lastName" name="lastName" onChange={handleChange}/><br/>
                    <label className="font-head" htmlFor="email">Email:</label><br/>
                    <input className="text-box" type="email" name="email" id="email" onChange={handleChange}/><br/>
                    <label className="font-head" htmlFor="pwd">Password: </label><br/>
                    <input className="text-box" type="password" id="pwd" name="pwd" onChange={handleChange}/><br/>
    
                    <button className="s-button" type="submit">Sign Up</button>
                </form>
            </div>


            <div className="form-container upload-container">
                <form action="#">
                    <h1>Upload File</h1>
                    <input type="file" name="imgfile" accept="image/jpeg" id="imgfile"/>
                    <button className="s-button" id="submitBtn" onClick={actionSubmit}>Submit</button>
                    <div className="" id="images" style={{display: "none"}}></div>
                </form>
            </div>
                
             
            <div className="overlay-container">
                
                <div className="overlay">
                    <div className="overlay-panel overlay-left">
                        <h1>Welcome!</h1>
                        <p>
                            To upload files, please enter your information
                        </p>
                        <button className="ghost" id="signIn" onClick={uploadButton}>Sign In</button>
                    </div>
                    <div className="overlay-panel overlay-right">
                        <h1>Hello, Friend!</h1>
                        <p>
                            Please upload the file you want to annonate
                        </p>
                        <button className="ghost" id="download" onClick={signInButton}>Upload Files</button>
                    </div>
                </div>

            </div>
               
        </div>
        
        </div>
    )
    
}

export default Upload