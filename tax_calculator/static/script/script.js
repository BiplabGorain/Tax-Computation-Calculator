var currentTab = 0;
showTab(currentTab);

function showTab(n) {
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";

  // Scroll to the top of the current tab when shown
  x[n].scrollIntoView();
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");

  if (n == 1 && !validateForm()) return false;
  x[currentTab].style.display = "none";

  currentTab = currentTab + n;
  if (currentTab >= x.length) {
    document.getElementById("regForm").submit();
    return false;
  }

  showTab(currentTab);
}

function validateForm() {
  var x,
    y,
    i,
    valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByClassName("req");

  for (i = 0; i < y.length; i++) {
    if (y[i].value == "" || y[i].value == "0") {
      y[i].classList.add("invalid");
      valid = false;
    }
  }
  return valid;
}

// Add a focus event listener to scroll the focused input into view
var inputFields = document.getElementsByTagName("input");
for (var i = 0; i < inputFields.length; i++) {
  inputFields[i].addEventListener("focus", function () {
    this.classList.add("scroll-into-view");
  });
  inputFields[i].addEventListener("blur", function () {
    this.classList.remove("scroll-into-view");
  });
}
