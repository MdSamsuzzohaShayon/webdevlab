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