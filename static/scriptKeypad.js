var usersData = {};
var textBox = document.getElementById('password');
var checkBox;

function loadUserData() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'users.json', true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            usersData = JSON.parse(xhr.responseText);
        } else {
            console.error('Failed to load user data');
        }
    };
    xhr.send();
}

window.onload = loadUserData;

function showKeypadModal() {
    checkBox = document.activeElement;
    document.getElementById('keypadModal').style.display = 'block';
}

function checkPassword() {
    var selectedUser = document.getElementById('users').value;
    var enteredPassword = textBox.value;

    if (usersData[selectedUser] && usersData[selectedUser].password === enteredPassword) {
        replaceSelectWithValues();
    } else {
        alert("Incorrect password");
    }
}

function replaceSelectWithValues() {
    var usersSelect = document.getElementById('users');
    var parent = usersSelect.parentNode;

    var minValueDiv = document.createElement('div');
    minValueDiv.className = 'mnValue';
    minValueDiv.innerHTML = '<p>min:</p><label id="minValue">0</label>';

    var maxValueDiv = document.createElement('div');
    maxValueDiv.className = 'mxValue';
    maxValueDiv.innerHTML = '<p>max:</p><label id="maxValue">50</label>';

    parent.replaceChild(minValueDiv, usersSelect);
    parent.appendChild(maxValueDiv);
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

function closeKeypad() {
    clearInput();
    document.getElementById('keypadModal').style.display = 'none';
}

function deleteNumber() {
    textBox.value = textBox.value.slice(0, -1);
}

function submitLogin() {
    clearInput();
    replaceSelectWithValues();
}

document.querySelector('.keypad button[onclick="submitLogin()"]').onclick = submitLogin;
