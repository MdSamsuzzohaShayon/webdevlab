//console.log("Loading JavaScript")
// <a class="nav-link active" aria-current="page" href="/">Home</a>


//PROBLEM WITH PAGE LOADING
const navLink = document.querySelectorAll('.nav-link');
navLink.forEach((nl , i)=>{
    nl.addEventListener('click',e=>{
//        e.preventDefault();
        console.log(e.target);
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