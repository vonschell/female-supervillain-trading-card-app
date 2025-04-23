$(document).ready(() => {
  document.getElementById('form').onsubmit = handleDeleteForm;
});

function handleDeleteForm(event) {
  event.preventDefault();
  var name = $("input[name='name']").val();
  $.post("/api/villains/delete", {
    "name": name
  }, function (data) {
    if (data.errors !== undefined) {
      document.getElementById("errors").innerHTML = data.errors.map((error) => (`<div class="error">${error}</div>`)).join("");
    } else {
      window.location = "/";
    }
  });
  return false;
}