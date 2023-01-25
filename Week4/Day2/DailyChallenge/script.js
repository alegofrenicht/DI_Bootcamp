// Instructions
// 1. Prompt the user for several words (separated by commas).
// 2. Put the words into an array.
// 3. Console.log the words one per line, in a rectangular frame as seen below.
// 4. Check out the Hints and Requirements below.

function frame() {
    let sentence = prompt('enter several words separating them with commas:')
    sentence = sentence.split(', ')
    let max_length = 0
    for (word of sentence) {
        if (word.length > Number(max_length)) {
            max_length = word.length
        }
    }
    let count = sentence.length
    console.log('*'.repeat(max_length + 4))
    for (word of sentence) {
        if (count === 0) {
            break
        } else {
            console.log('*' + ' ' + word + ' '.repeat(max_length - (word.length - 1)) + '*')
        }
        count--
    }
    console.log('*'.repeat(max_length + 4))
}

frame()