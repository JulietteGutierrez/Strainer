function ValidateEmail(inputText){
    var mailformat = /\w@\w+.\w+/;
    if(inputText.value.match(mailformat)){
        return true;
    }
    else{
        return false;
    }
}

function onlyLetters(inputText){
    return inputText.match(/^[A-Za-z]+$/)
}
/**
 * Permite validar campos de un formulario de forma individual sobre evento onblur de cada elemento, entregando al final estado
 * con respecto a validación global del formulario; en caso de que sea válido, muestra dialogo de confirmación
 * @param {*} val -> ref. a nro de campo
 * @returns
 */
function validate(val) {
    let v1 = document.getElementById('fnombre');
    let v2 = document.getElementById('fapellido');
    let v3 = document.getElementById('femail');
    let v4 = document.getElementById('ftel');
    let v5 = document.getElementById('fasunto');
    let v6 = document.getElementById('fmensaje');

    let flag1,flag2,flag3,flag4,flag5,flag6;

    flag1= false;
    flag3= false;
    flag5= false;
    flag6= false;

    flag2= true;
    flag4= true;

    if(val==1 || val==0){
        const name = v1.value.trim()
        if(name == '' || !onlyLetters(name)) {
            v1.style.borderColor = 'red';
            flag1 = false;
        }
        else {
            v1.style.borderColor = 'green';
            flag1 = true;
        }
    }

    if((val===2 || val===0) && v2.value !== ''){
        flag2 = onlyLetters(v2.value)
        v2.style.borderColor = flag2? 'green': 'red'
    }

    if((val===4 || val===0) && v4.value !== ''){
        const value = +v4.value
        flag4 = typeof value === "number" && Number.isInteger(value) && value>1000000 
        v4.style.borderColor = flag4? 'green': 'red'
    }

    if(val==5 || val==0){
        if(v5.value.trim() == '') {
            v5.style.borderColor = 'red';
            flag5 = false;
        }
        else {
            v5.style.borderColor = 'green';
            flag5 = true;
        }
    }

    if(val==6 || val==0){
        if(v6.value.trim() == '') {
            v6.style.borderColor = 'red';
            flag6 = false;
        }
        else {
            v6.style.borderColor = 'green';
            flag6 = true;
        }
    }

    if(val==3 || val==0) {
        if(v3.value.trim() == '' || !ValidateEmail(v3)) {
            v3.style.borderColor = 'red';
            flag3 = false;
        }
        else {
            v3.style.borderColor = 'green';
            flag3 = true;
        }
    }

    let flag = flag1 && flag2 && flag3 && flag4 && flag5 && flag6;

    if(flag===true){
        if(confirm('Confirma el envío de su consulta?')){
            return flag;
        }
        else{
            return false;
        }
    }
    else{
        return flag;
    }



}