import '.././css/bottom-footer.css'
import gull from '.././pics/gull2.png'
import insta from '.././pics/insta.png'
import email from '.././pics/mail.png'
import linkedin from '.././pics/Linkedin.png'

function Bottom() {
    return (
        <div class="bottom">
            qq
            <div class="footer">
                <div class="footer-elements">
                    <img class="gull-icon" src={gull}/>
                </div>
                <div class="footer-elements">
                    <form method="get" action="#Homepage" style={{backgroundColor: "black"}}>
                        <button class="footer-links" type="submit">
                            HOME
                        </button>    
                    </form> 
                </div>
                <div class="footer-elements">
                    <form method="get" action="#Homepage" style={{backgroundColor: "black"}}>
                        <button class="footer-links" type="submit">
                            ABOUT
                        </button>    
                    </form> 
                </div>
                <div class="footer-elements">
                    <form method="get" action="#Homepage" style={{backgroundColor: "black"}}>
                        <button class="footer-links" type="submit">
                            PROJECTS
                        </button>    
                    </form>    
                </div>
            </div>
            <div class="social-links">
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src={insta}/>
                    </button>    
                </div>
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src={email}/>
                    </button>    
                </div>
                <div class="social-link-element">
                    <button class="Social-button">
                        <img class="social-icons" src={linkedin}/>
                    </button>   
                </div>
            </div>
            <div class="ender">

            </div>
        </div>
    )

    
}

export default Bottom
