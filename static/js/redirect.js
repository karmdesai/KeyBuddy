// When "loginButton" is clicked
document.getElementById("loginButton").onsubmit = function () {redirectUser()};

function redirectUser ()
{
  // Redirect to the 'message.html' page
  location.href = "../../message.html";
}
