## Maths at Light Speed

I wrote a script:

    var a = ""
    for (let i = 0; i < 5; i++) {
        a += document.getElementById('calc-number-1').children[i].innerHTML
    }

    var b = ""
    for (let i = 0; i < 5; i++) {
        b += document.getElementById('calc-number-2').children[i].innerHTML
    }

    a = parseInt(a)
    b = parseInt(b)

    c = a+b

    document.getElementById('letter-1').value= c
    document.getElementById('testbtn').click()	

And changed 

    <input type="submit" value="Submit Answer" class="btn">

into

    <input type="submit" value="Submit Answer" class="btn" id="testbtn">

Then this is unauthodox and temporary but I clicked to generate a code then spammed the script in the chrome console and got it first try! Lucky i guess :))