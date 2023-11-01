$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data) {
      const translation = data.hello;
      $('#hello').text(translation);
    });
});
