$.get("/api/", function (data) {
  console.log(data)
})

$.get("/api/villains/", function (data) {
  for (let i in data) {
    $(".content").append('<div class="card"><h2 class="card-name">' + data[i].name + '</h2><img src="' + data[i].url + '" class="card-image"/><div class="card-body"><p class="card-description">' + data[i].description + '</p><h4>Interests</h4><p class="card-interests">' + data[i].interests + '</p><p class="card-date-added">Date added: ' + data[i].date_added + '</p></div></div>')
  }
})