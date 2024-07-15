
//imports the function with the return html code
import Upload from './Upload.js';
import Hero from './Hero.js';
import Project from './Project.js';
import Header from './Header.js';
import Bottom from './Bottom.js';
import '.././css/general.css'



function Website() {
  

//-------------------------------------------------------------------------------------------------
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
        <div onLoad={loadPosts()}>
            <Header></Header>
            <Hero></Hero>
            <Project></Project>
            <Upload></Upload>
            <Bottom></Bottom>
        </div>

    )
}

export default Website