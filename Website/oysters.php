<!DOCTYPE html>
<html>
    <head>
        <title>Oyster's REU</title>
        <link rel="stylesheet" href="css\header.css">
        <link rel="stylesheet" href="css\general.css">
        <link rel="stylesheet" href="css\hero.css">
        <link rel="stylesheet" href="css\project.css">
        <link rel="stylesheet" href="css\slideshow.css">
        <link rel="stylesheet" href="css\upload.css">
        <link rel="stylesheet" href="css\bottom-footer.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Tiny5&display=swap" rel="stylesheet">
    `   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body style="height: 3000px;">
        <div class="header">
            <div class="left-section">
                <img class="su-icon" src="header-pics\images.jpg">
            </div>
            <div class="middle-section">
                <p class="tiny5-regular">
                    NSF REU: EXCERCISE
                </p>
            </div>
            <div class="right-section">
                <button class="hamburger-button">
                    MENU
                    <img class="hamburger-menu" src="header-pics/hamburger-menu.svg">
                </button>
                
            </div>
        </div>
        <!--Section for information we want people to know-->
        <div class="hero">
            <div class="hero-left-section">
                <div class="top-left-section">
                    <p class="headline">
                        <a id="Homepage">
                            Welcome to EXCERCISE
                        </a> 
                    </p>
                    <p class="sub-text">
                        (Explore Emerging Computing in Science and Engineering) is an interdisciplinary
                         project that explores emerging paradigms in parallel computing 
                         with data and compute-intensive applications in science and engineering.
                    </p>
                </div>
                <div class="b-left-section">
                    <a href="https://faculty.salisbury.edu/~ealu/REU/REU.html" target="_blank">
                    <button class="learn-button">
                        About EXCERCISE
                    </button>
                    </a>
                </div>
                
            </div>
            <div class="hero-right-section">
                <!--<img class="hero-pic" src="header-pics/channel-2.jpeg" alt="placeholder">-->
            </div>
            
        </div>
        <!--Goes in to depth on the projects that we are currently doing and what is to be expected from them-->
        <div class="project-section">
            <div class="project-left-section">
                <p class="project-head">
                    Our Project: Oyster Orientation
                </p>
                <div class="top-left-section">
                    <p class="project-sub-text">
                        We aim to build upon the previous work done on Oyster Orientation and Deep Learning Image Processing 
                        by Joshua Comfort, Ian Rudy, and Dr. Yunawei Jin. In the results, 
                        the research team was able to implement YOLOv5, a deep-learning detection model 
                        used to recognize and classify the oysters into 3 different states: slightly open, open, and closed. 
                        What we can improve is incorporate the updated version of YOLOv5, 
                        YOLOv8 and expand the use of the system to detect depth as well.
    
                    </p>
                </div>
                <div class="bottom-lft-section">
                    <a href="https://ianrudy.com/ManualDownloads/NSFREUFinalReport.pdf" target="_blank">
                        <button class="pdf-button">
                            PDF of Research
                        </button>
                    </a>    
                </div>
                
                
            </div>
            <div class="project-right-section">
                <img class="oyster-pic" src="header-pics/oysters.webp" alt="placeholder">
            </div>
            
        </div>
        <!--Aight format will be in the form of a form in HTML that requires the users information
        (first name, last name, email, etc) and has to be interactive (JS) so that we can output the 
        image with annotations, or email the image with annotations, (possibly roboflow embeded???)
        either way, I can do a set up of form in the center, and I'll have to do more research on 
        queries and all that-->
        <div class="upload-section">
            <p class="upload-title">
                Upload Image for Annotation
            </p>
            <div class="container" id="container">
                <div class="form signIn">
                    <form action="includes/register.php" method="post">
                        <h1>Create Account</h1>
                        <label class="font-head" for="FirstName">First name:</label><br>
                        <input class="text-box" type="text" id="FirstName" name="FirstName" class="text-box"><br>
                        <label class="font-head" for="LastName">Last name:</label><br>
                        <input class="text-box" type="text" id="LastName" name="LastName"><br>
                        <label class="font-head" for="email">Email:</label><br>
                        <input class="text-box" type="email" name="email" id="email"><br>
                        <label class="font-head" for="pwd">Password: </label><br>
                        <input class="text-box" type="password" id="pwd" name="pwd"><br>
                        <!-- <label class="font-head" for="myfile">Select an image:</label><br>
                        <input class="text-box" type="file" id="myfile" name="myfile"><br>
                        <label class="font-head" for="datetime">Date and time: </label><br>
                        <input class="text-box" type="datetime-local" id="datetime" name="datetime"><br>
                        <label class="font-head" for="message">Special request: </label><br>
                        <textarea class="text-box" name="message" id="message" rows="10" cols="30" style="transform: matrix(1, 0, 0, 1, 0, 0);">
                    
                        </textarea><br>-->
                        <button class="button" type="submit">Sign Up</button>
                    </form>
                </div>


                <div class="form upload-container">
                    <form action="">
                        <h1>Upload File</h1>
                        <input type="file" name="imgfile" accept="image/jpeg" id="imgfile">
                        <button id="submitBtn" >Submit</button>
                    </form>
                </div>
                <!--Creates the format that lays on top of different sections for form-->
                <div class="overlay-container">
                    <div class="overlay">
                        <div class="overlay-panel overlay-left">
                            <h1>Welcome!</h1>
                            <p>
                                To upload files, please enter your information
                            </p>
                            <button class="ghost" id="signIn">Sign In</button>
                        </div>
                        <div class="overlay-panel overlay-right">
                            <h1>Hello, Friend!</h1>
                            <p>
                                Please upload the file you want to annonate
                            </p>
                            <button class="ghost" id="upload">Upload Files</button>
                        </div>
                    </div>
                </div>
            </div>     
        </div>

        
        
        <!--<div class="slideshow-section">
            slideshow
            <div class="owl-show">
                <div class="ele1">
                    q
                </div>
                <div class="ele2">
                    q
                </div>
                <div class="ele3">
                    q
                </div>
                <div class="ele4">
                    qq
                </div>
            </div>
        </div>-->
        <div class="bottom">
            qq
            <div class="footer">
                <div class="footer-elements">
                    <img class="gull-icon" src="header-pics/gull2.png">
                </div>
                <div class="footer-elements">
                    <form method="get" action="#Homepage">
                        <button class="footer-links" type="submit">
                            HOME
                        </button>    
                    </form> 
                </div>
                <div class="footer-elements">
                    <form method="get" action="#Homepage">
                        <button class="footer-links" type="submit">
                            ABOUT
                        </button>    
                    </form> 
                </div>
                <div class="footer-elements">
                    <form method="get" action="#Homepage">
                        <button class="footer-links" type="submit">
                            PROJECTS
                        </button>    
                    </form>    
                </div>
            </div>
            <div class="social-links">
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src="header-pics\insta.png">
                    </button>    
                </div>
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src="header-pics\mail.png">
                    </button>    
                </div>
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src="header-pics\Linkedin.png">
                    </button>   
                </div>
            </div>
            <div class="ender">

            </div>
        </div>

        <script src="main.js"></script>
    </body>
</html>
