var spthy_editor = CodeMirror.fromTextArea(document.getElementById('spthy-content'), {
  lineNumbers: true,
  mode: "spthy"
});
var v_result = CodeMirror.fromTextArea(document.getElementById('v-result'), {
  lineNumbers: true,
  mode: "spthy"
})
v_result.setSize("60%", 200);
spthy_editor.setSize(500, 200);

// $(spthy_editor.getWrapperElement()).hide();

$("form").on("change", ".file-upload-field", function () {
  $(this).parent(".file-upload-wrapper").attr("data-text", $(this).val().replace(/.*(\/|\\)/, ''));
});

$(".file-upload-field").change(function () {
  var reader = new FileReader();
  // file-upload-field is defined in forms.py
  reader.readAsText($(".file-upload-field")[0].files[0], "UTF-8");
  reader.onload = function () { spthy_editor.setValue(reader.result); $("#spthy-content").text(reader.result); }
  // spthy_editor.setSize("100%", Infinity);
  $(spthy_editor.getWrapperElement()).show();
});

$(".form button").click(function (e) {
  e.preventDefault()// cancel form submission
  // alert('test!');
  if ($(this).attr("value") == "load model") {
    var filename = $('select#model-select').val();
    alert(filename);
    $.get('/load_file/', { 'filename': filename },
      function (response) {
        $(spthy_editor.getWrapperElement()).show();
        spthy_editor.setValue(response.file);
        $("#spthy-content").text(response.file);
      })
  }
  else if ($(this).attr("value") == "verification") {
    var buf = $('#spthy-content').val();
    alert(buf);
    $.get('/tamarin/',
      { 'buf': buf },
      function (response) { $('textarea#v-result').text(response.msg); v_result.setValue(response.msg); }
    );
  } else {

  }
});
