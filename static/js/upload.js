$("form").on("change", ".file-upload-field", function(){
    $(this).parent(".file-upload-wrapper").attr("data-text", $(this).val().replace(/.*(\/|\\)/, '') );
});
$(".file-upload-field").change(function(){
    var reader = new FileReader();
    reader.onload = function(e){
      $("#js-textarea").val(e.target.result);
    };
    reader.readAsText($(".file-upload-field")[0].files[0], "UTF-8");
});
