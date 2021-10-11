//console.log("Loading JavaScript")
// <a class="nav-link active" aria-current="page" href="/">Home</a>


//PROBLEM WITH PAGE LOADING
const navLink = document.querySelectorAll('.nav-link');
navLink.forEach((nl , i)=>{
    nl.addEventListener('click',e=>{
//        e.preventDefault();
//        console.log(e.target);
//         navLink.forEach(rmNL=>{
//            if(rmNL.classList.contains("active")){
//                 rmNL.classList.remove('active');
//            };
//        });
        const selectedNavLink = e.target;
        selectedNavLink.classList.add("active");
        selectedNavLink.setAttribute("aria-current", "page");

    });
});






//SHOWING TAB CONTENT
const tutorialTitle = document.querySelectorAll(".title-nav-link");
const tutorialDesc = document.querySelectorAll('.tutorial-desc');
const tabContent = document.getElementById("v-pills-tabContent");


tutorialDesc.forEach(td => td.classList.remove('active'));
const firstDescElement = tabContent.querySelector("[num='1']");
firstDescElement.classList.add('active');
//console.log(firstDescElement);


tutorialTitle.forEach((tt, i)=>{
    tt.addEventListener('click', (e)=>{
        tutorialDesc.forEach(td => td.classList.remove('active'));
        const selectedTutorialNum =e.target.getAttribute('num');
//        console.log(e.target.getAttribute('num'));
        const selectedTutorial = tabContent.querySelector(`[num='${selectedTutorialNum}']`);
//        console.log(selectedTutorial);
        selectedTutorial.classList.add('active');
    });
});



function getId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);

    return (match && match[2].length === 11)
      ? match[2]
      : null;
}

const videoId = getId('http://www.youtube.com/watch?v=zbYf5_S7oJo');
const iframeMarkup = '<iframe width="560" height="315" src="//www.youtube.com/embed/'
    + videoId + '" frameborder="0" allowfullscreen></iframe>';

//const videoURL = '{{ tutorials }}';
//console.log("Video utl - ",videoURL)


//console.log('Video ID:', videoId)