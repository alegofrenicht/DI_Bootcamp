let chances = 0
function playTheGame(){
    let ask = confirm('Wanna play a game?')
    if (!ask){
        alert('No problem, Goodbye')
    }
    else {
        let userNumber = Number(prompt('Enter a number between 0 and 10: '))
        if (isNaN(userNumber)){
            alert('Sorry Not a number, Goodbye')
        }
        else {
            if ( userNumber < 0 || userNumber > 10){
                alert('Sorry it’s not a good number, Goodbye')
            }
            else{
            let computerNumber = Math.random() * 10
                computerNumber = Math.round(computerNumber)
            compareNumbers(userNumber, computerNumber)
                }
            }
        }
    }

function compareNumbers(userNumber,computerNumber){
    if (userNumber === computerNumber){
        alert('WINNER')
        return
    }
    else {
        chances += 1;
        if (chances > 3) {
            alert('out of chances');
            return;
        }

        if (userNumber > computerNumber) {
            alert('Your number is bigger then the computer’s, guess again');
        }
        else {
            alert('Your number is smaller then the computer’s, guess again');
        }
        userNumber = Number(prompt('Enter a number between 0 and 10'));
        compareNumbers(userNumber,computerNumber);
    }
}


