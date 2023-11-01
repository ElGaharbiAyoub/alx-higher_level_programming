$(document).ready(function () {
  function translateHello() {
    var languageCode = $("#language_code").val();

    $.get(
      "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode,
      function (data) {
        $("#hello").text(data.hello);
      }
    );
  }

  $("#btn_translate").on("click", function () {
    translateHello();
  });

  $("#language_code").on("keyup", function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
