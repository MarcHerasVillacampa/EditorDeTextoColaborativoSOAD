
var del = false;
var lastPointer=-1;
document.addEventListener("keyup", KeyCheck); //al presionar una tecla llama keycheck
function KeyCheck(event)
{
    var KeyID = event.keyCode;
    //Comprueba que el texteare este seleccionado
    if (document.activeElement.id != "text") return;

    text_area = document.getElementById("text");
    text = text_area.value;
    pointer = text_area.selectionStart;

    switch(KeyID)
    {
        case 8:
            erease(pointer)
        break; 
        case 37:
        break;
        case 38:
        break;
        case 39:
        break;
        case 40:
        break;
        default:
            // write(pointer-1,String.fromCharCode(KeyID))
            // write2()
        break;
    }
    
}

function erease(pointer)
{    
    eel.erease(pointer,"d");
}

// function write(pointer,text)
// {    
//     eel.edit("i",pointer,text);
//     setText(text);
// }

function write2()
{           
    text_area = document.getElementById("text");
    text = text_area.value;
    pointer = text_area.selectionStart;
    if(pointer<lastPointer)
    {
        // alert(pointer," ",lastPointer)
    }
    else
    {
        // alert("eeeepa"+pointer+" "+lastPointer);

        if(pointer!=0)
        {
            text = text.substring(pointer-1,pointer);
        }
        eel.edit("i",pointer-1,text);
        
        setText(text);
    }
    lastPointer = pointer;

}

function setText(text)
{
    document.getElementById("debugger").innerHTML = text
}
