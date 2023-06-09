function ShowText(){
    var text_geometry = document.getElementById('geometry').value;
    var text_color = document.getElementById("color").value;
    var length = text_geometry.length;

    var message_for_user = "Мне нравится: " + text_geometry + '\n' + "Цвет: " + text_color + '\n' + "Длина фигуры: " + length;
    alert(message_for_user);
}