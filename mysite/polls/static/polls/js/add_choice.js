function addChoice(classSelector) {
    var choices = document.getElementsByClassName(classSelector);
    var numberOfChoices = choices.length;
    var choicelabelText = "Choice "
    choicelabelText += numberOfChoices + 1;
    var choicelabel = document.createTextNode(choicelabelText);
    var lastChoice = choices[numberOfChoices-1];
    var newp = document.createElement('p');
    var newlabel = document.createElement('label');
    var idLabel = "id_choice_";
    idLabel += numberOfChoices +1;
    newlabel.setAttribute("for", idLabel);
    newlabel.appendChild(choicelabel);
    console.log("Inner HTML of label:" + newlabel.textContent);
    newp.appendChild(newlabel);
    var inputElement = document.createElement('input');
    var inputNameAttribute = "choice_";
    inputNameAttribute += numberOfChoices + 1;
    inputElement.setAttribute("type", "text");
    inputElement.setAttribute("name", inputNameAttribute);
    inputElement.setAttribute("class", classSelector);
    inputElement.setAttribute("maxlength", "30");
    inputElement.setAttribute("minlength", "1");
    inputElement.setAttribute("id", idLabel);
    newp.appendChild(inputElement);
    var parent = lastChoice.parentNode;
    var realParent = parent.parentNode;
    var inputElement = realParent.lastChild.previousSibling;
    console.log(inputElement);
    realParent.insertBefore(newp, inputElement);
    //realParent.appendChild(newp);

}

var buttonAdder = document.getElementById("adder");
buttonAdder.addEventListener('click', function(){
    addChoice("choice");
},false);