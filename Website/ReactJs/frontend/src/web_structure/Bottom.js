import '.././css/bottom-footer.css'

function Bottom() {
    return (
        <div class="bottom">
            qq
            <div class="footer">
                <div class="footer-elements">
                    <img class="gull-icon" src="./pics/gull2.png"/>
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
                        <img class="social-icons" src="./pics\insta.png"/>
                    </button>    
                </div>
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src="./pics\mail.png"/>
                    </button>    
                </div>
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src="./pics\Linkedin.png"/>
                    </button>   
                </div>
            </div>
            <div class="ender">

            </div>
        </div>
    )

    
}

export default Bottom