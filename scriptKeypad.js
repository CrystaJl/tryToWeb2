
var textBox = document.getElementById('textbox')


function showKeypadModal() {
    document.getElementById('keypadModal').style.display = 'block';
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
    clearInput();
    document.getElementById('keypadModal').style.display = 'none';
}
