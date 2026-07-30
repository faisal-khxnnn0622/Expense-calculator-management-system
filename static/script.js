// Welcome Message

console.log("Expense Calculator Management System Loaded");


// Confirm Delete

function confirmDelete(){

    return confirm("Are you sure you want to delete this expense?");

}


// Apply confirmation to delete buttons

window.onload = function(){

    let deleteButtons=document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(function(btn){

        btn.onclick=function(){

            return confirmDelete();

        }

    });

}


// Input Validation

let forms=document.querySelectorAll("form");

forms.forEach(function(form){

    form.addEventListener("submit",function(e){

        let amount=document.querySelector("input[name='amount']");

        if(amount){

            if(parseFloat(amount.value)<=0){

                alert("Amount must be greater than zero.");

                e.preventDefault();

            }

        }

    });

});