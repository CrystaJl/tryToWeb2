var currentUser = "{{ current_user }}";
var userLevels = {
    Guest: 0,
    God: 5,
    User1: 1,
    User2: 2,
    User3: 3,
    User4: 4
};

var textBox = document.getElementById('password');
var checkBox;

function showKeypadModal() {
    checkBox = document.activeElement;
    var requiredLevel = checkBox.getAttribute('data-level');
    if (userLevels[currentUser] >= requiredLevel) {
        document.getElementById('keypadModal2').style.display = 'block';
    } else {
        document.getElementById('keypadModal').style.display = 'block';
    }
}

function submitLogin() {
    var selectedUser = document.getElementById('users').value;
    var password = textBox.value;
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: selectedUser,
            password: password
        })
    }).then(response => response.json()).then(data => {
        if (data.success) {
            currentUser = selectedUser;
            document.getElementById('user').textContent = currentUser;
            document.getElementById('password').value = 'Correct Password';
            if (userLevels[currentUser] >= 1) {
                document.getElementById('keypadModal2').style.display = 'block';
            } else {
                document.getElementById('keypadModal').style.display = 'block';
            }
            document.getElementById('loginModal').style.display = 'none';
        } else {
            alert('Incorrect password');
            clearInput();
        }
    });
}

function clearInput() {
    textBox.value = '';
    document.getElementById('keypadModal').style.display = 'none';
}

function closeKeypad() {
    textBox.value = '';
    document.getElementById('keypadModal').style.display = 'none';
    document.getElementById('keypadModal2').style.display = 'none';
}

function deleteNumber() {
    if (textBox) {
        textBox.value = textBox.value.slice(0, -1);
        var keypadModal = document.getElementById('keypadModal');
        if (keypadModal) {
            keypadModal.style.display = 'none';
        }
        var loginModal = document.getElementById('loginModal');
        if (loginModal) {
            loginModal.style.display = 'none';
        }
    }
}

function checkPassword() {
    // Проверка пароля и установка значений, если необходимо
}

function addNumber(number) {
    if (number === ',' && (textBox.value.indexOf(',') === -1 && textBox.value !== '')) {
        textBox.value += number;
    } else if (number !== ',') {
        textBox.value += number;
    }
}

// Функция изменения цвета и проверки доступа
function changeFill(activeClass) {
    const motors = document.querySelectorAll('.motor');
    motors.forEach(motor => {
        if (motor.classList.contains(activeClass)) {
            motor.setAttribute('fill', 'red');
            motor.setAttribute('stroke', 'red');
            motor.setAttribute('data-value', activeClass);
            levelPass = activeClass;
        } else {
            motor.setAttribute('fill', 'gray');
            motor.setAttribute('stroke', 'gray');
        }
    });

    const inputs = document.querySelectorAll('.textbox_inputs input[type="text"]');
    inputs.forEach(input => input.value = '');

    if (userLevels[currentUser] >= levelPass) {
        document.getElementById('keypadModal2').style.display = 'block';
    } else {
        document.getElementById('keypadModal').style.display = 'block';
    }
}