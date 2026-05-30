function generatePassword(){

    let length =
    document.getElementById("length").value;

    let chars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";

    let password = "";

    for(let i=0;i<length;i++){

        password += chars.charAt(
            Math.floor(Math.random()*chars.length)
        );
    }

    document.getElementById("result").innerText =
    password;
}