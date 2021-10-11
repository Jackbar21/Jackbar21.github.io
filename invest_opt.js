// Bond Money
let VBTLX_MONEY = 0.0;
let VBTLX_PERCENT = 0.10;

// Stocks Money
let VTWAX_MONEY = 3000.0;
let VTWAX_PERCENT = 0.90;

// Used for indexing JS Objects in
// an easier-to-read fashion.
const MONEY = 0;
const PERCENT = 1;

// Will determine base for the
// algorithm (i.e. 0.01 finds the
// optimal investment penny-by-penny.)
const DISCREPANCY_CONSTANT = 0.01;

let object_of_stocks = {
    "VBTLX": [VBTLX_MONEY, VBTLX_PERCENT],
    "VTWAX": [VTWAX_MONEY, VTWAX_PERCENT]
}

let final_object = {}

//document.querySelectorAll("");

document.addEventListener("DOMContentLoaded", function() {

    // By default, submit button is disabled
    /*document.querySelector("#submit").disabled = true;

    document.querySelector("#task").onkeyup = function() {
        if (document.querySelector("#task").value.length > 0)
        {
            document.querySelector("#submit").disabled = false;
        }
        else
        {
            document.querySelector("#submit").disabled = true;
        }
    }*/
    
    document.querySelector("form").onsubmit = function() {

        const task = document.querySelector("#task").value;
        console.log(task);

        const list_item = document.createElement("input");
        list_item.innerHTML = task;

        document.querySelector("#tasks").append(list_item);
        document.querySelector("#form").append(list_item);

        document.querySelector("#task").value = "";

        document.querySelector("#submit").disabled = true;

        // Stop form from submitting
        return false;
    }

});