/* EXPANDER MENU */
const showMenu = (toggleId, navbarId, bodyId) => {
    const toggle = document.getElementById(toggleId),
    navbar = document.getElementById(navbarId),
    bodypadding = document.getElementById(bodyId)

    if( toggle && navbar ) {
        toggle.addEventListener('click', ()=>{
            navbar.classList.toggle('expander');

            bodypadding.classList.toggle('body-pd')
        })
    }
}
document.addEventListener('DOMContentLoaded', function () {
    // 페이지가 로딩될 때 자동으로 실행되어야 하는 코드
    showMenu('nav-toggle', 'navbar', 'body-pd');
});



