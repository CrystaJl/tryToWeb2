
var textBox = document.getElementById('textbox')
var checkBox;

function showKeypadModal() {
    checkBox = document.activeElement;
    document.getElementById('keypadModal').style.display = 'block';
}


function checkPassword(){
    var timeToTurnOffDisplay = document.getElementById('timeToTurnOffDisplay');


    if (checkBox === document.getElementById("timeToTurnOffDisplay")) {
        if(textBox.value == '1234'){
            timeToTurnOffDisplay.placeholder = '12:30';
        }
    };

    if (checkBox === document.getElementById("timeToTurnOnWall")) {
        if(textBox.value == '1235'){
            timeToTurnOnWall.placeholder = '12:35';
        }
    }

}



function addNumber(number) {
    if (number === ',' && (textBox.value.indexOf(',') === -1 && textBox.value !== '')) {
        textBox.value += number;
    } else if (number !== ',') {
        textBox.value += number;
    }
}

function clearInput() {
    textBox.value = '';
}

function closeKeypad(){
    textBox.value = '';
    document.getElementById('keypadModal').style.display = 'none';
}

function deleteNumber(){
    textBox.value = textBox.value.slice(0, -1);
}

function submitInput() {
    checkPassword()
    clearInput();
    document.getElementById('keypadModal').style.display = 'none';
}

