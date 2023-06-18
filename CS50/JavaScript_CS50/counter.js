// variable name and data variable cant be the same name

// variable that will save the number how many count you did.
//if there is no item in 'counter' local storage
if (!localStorage.getItem("counter")) {
  localStorage.setItem("counter", 0);
}

//   function count()
function count() {
  let counter = localStorage.getItem("counter");
  counter++;
  document.querySelector("h1").innerHTML = counter;

  localStorage.setItem("counter", counter);

  if (counter % 10 == 0) {
    //This is template literal ` ${values}`
    alert(`Count is now ${counter}`);
  }
}

// This is an Add Event Listener
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("h1").innerHTML = localStorage.getItem("counter");
  document.querySelector("button").onclick = count;
  //count is the function

  // setInterval(count, 1000); // Run count every 1000 milliseconds
});
