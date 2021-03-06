function getSteps() {
    var steps = document.getElementById('steps_input').value;
    return steps;
}

function getHref(a, s = getSteps()) {
    console.log('/'+ a +'/'+ s);
    return '/'+ a +'/'+ s;
}
function setHrefs(){
    document.getElementById('turn_left_button').href = getHref("turn_left");
    document.getElementById('turn_right_button').href = getHref("turn_right");
}

