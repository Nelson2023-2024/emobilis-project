/*********************LOGIN VALIDATION**********************************/
const loginForm = document.getElementById('form-login')
const loginEmailInput = document.getElementById('email')
const loginPasswordInput = document.getElementById('password')

//errors
const errorLoginEmail = document.getElementById('error_login_email')
const errorLoginPassword = document.getElementById('error_login_password')

loginForm.addEventListener('submit', e =>{
    e.preventDefault()

    //email validation
    if(loginEmailInput.value.trim() ===""){
        errorLoginEmail.innerHTML = "please enter your email address"
    }

    //password validation
    if(loginPasswordInput.value.trim() === ""){
        errorLoginPassword.innerHTML = "please Enter your password"
    }

    if(loginEmailInput.value !== "" &&  loginPasswordInput.value !==""){
        loginForm.submit();
    }
})


//eye open 
const eye = document.getElementById('open');
eye.addEventListener('click', ()=>{
    eye.classList.toggle('bi-eye-fill')
    eye.classList.toggle('bi-eye-slash-fill')

    if(loginPasswordInput.type === 'text' && eye.classList.contains('bi-eye-fill')){
        loginPasswordInput.type = 'password'

    }
    else{
        loginPasswordInput.type = 'text'
    }
})



