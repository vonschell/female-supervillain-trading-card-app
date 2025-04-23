$(document).ready(() => {
  document.getElementById('form').onsubmit = handleAddForm;
});

function handleAddForm(event) {
  event.preventDefault();

  var name = $("input[name='name']").val();
  var description = $("input[name='description']").val();
  var interests = $("input[name='interests']").val();
  var url = $("input[name='url']").val();

  $.post("/api/villains/add", {
    "name": name,
    "description": description,
    "interests": interests,
    "url": url,
    "date_added": new Date()
  }, function (data) {
    if (data.errors !== undefined) {
      document.getElementById("errors").innerHTML = data.errors.map((error) => (`<div class="error">${error}</div>`)).join("");
    } else {
      window.location = "/";
    }
  })

  return false;
}