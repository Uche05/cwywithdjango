// Wait for the DOM to be ready

document.addEventListener("DOMContentLoaded", function () {
    // JavaScript to be fired on all pages


    //button to lead a click to another page
    const btnJobPost = document.getElementById('btnLogin1');
    const btnContact = document.getElementById('btnContact');
    const btnStaffLogin = document.getElementById('btnLogin2');
    const btnAdminLogin = document.getElementById('btnLoginAdv');

    btnJobPost.addEventListener('click', function () {
        window.open("jobpost.html", "_blank");
    }
    );

    btnContact.addEventListener('click', function () {
        window.open("contact.html", "_blank");
    }
    );

    btnStaffLogin.addEventListener('click', function(){
        window.open("staff.html", "_blank");
    });

    btnAdminLogin.addEventListener('click', function(){
        window.open("admin.html", "_blank");
    });


    //testimonial animation style


});